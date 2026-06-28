from flask import Flask, render_template, session, request
import secrets

app = Flask(__name__,static_folder='static/')
app.secret_key = secrets.token_bytes()

items = {5427: ("我的世界2023 Point", 1337),
         5428: ("傅說對決 Back Point", 1024),
         5429: ("尬許Point", 4096),
         5430: ("FLAG Point", 2147483648),
         5431: ("買喀Point", 65536),
         5432: ("送你哈密Point", -0.05)}


@app.route("/")
def home():
    if 'money' not in session:
        session['money'] = 65536
    if 'stuff' not in session:
        session['stuff'] = []
    return render_template("index.html", items=items)

@app.route("/orders")
def orders():
    if 'money' not in session:
        session['money'] = 65536
    if 'stuff' not in session:
        session['stuff'] = []
    return render_template("orders.html")

@app.route("/reset")
def reset_data():
    if 'money' in session:
        session['money'] = 65536
    if 'stuff' in session:
        session['stuff'] = []
    return f"<script>alert(`成功重置資料`); location='/'</script>"


@app.route("/item/<int:item_id>")
def view_item(item_id):
    return render_template("item.html", item=items[item_id], item_id=item_id)


@app.route("/buy", methods=['POST'])
def buy_item():
    cost = float(request.form.get("cost"))
    item_id = int(request.form.get("item_id"))
    if cost > session['money']:
        return "<script>alert(`你沒有足夠的摳摳 Q_Q`); location.href='/';</script>"
    session['money'] -= cost
    session['stuff'].append(items[item_id])
    return f"<script>alert(`成功購買 {items[item_id][0]} 一個!`); location='/'</script>"


if __name__ == "__main__":
    app.run(debug=True)
