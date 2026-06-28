from flask import Flask, request, jsonify, render_template
import docker
import os

app = Flask(__name__)
CONF_PATH = "/data/nginx.conf"
NGINX_CONTAINER = "nginx_server"

client = docker.from_env()


def nginx_exec(cmd: list[str]) -> tuple[int, str]:
    container = client.containers.get(NGINX_CONTAINER)
    code, output = container.exec_run(cmd)
    return code, output.decode()


@app.get("/")
def index():
    with open(CONF_PATH) as f:
        content = f.read()
    return render_template("index.html", content=content)


@app.post("/save")
def save():
    content = request.json.get("content", "")

    # 先寫入暫存檔驗證語法
    tmp = CONF_PATH + ".tmp"
    with open(tmp, "w") as f:
        f.write(content)

    code, output = nginx_exec(["nginx", "-t", "-c", "/etc/nginx/nginx.conf.tmp"])
    if code != 0:
        os.remove(tmp)
        return jsonify(ok=False, msg=output)

    # 驗證通過 → 覆蓋正式檔並 reload
    os.replace(tmp, CONF_PATH)
    _, reload_out = nginx_exec(["nginx", "-s", "reload"])
    return jsonify(ok=True, msg="儲存並重載成功\n" + reload_out)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
