from OpenSSL import crypto
import requests

keys = crypto.PKey()
keys.generate_key(crypto.TYPE_RSA, 4096)

name = "Salva"
ip = requests.get('http://ip.42.pl/raw').text
pubKey = crypto.dump_publickey(crypto.FILETYPE_PEM, keys)

url = "http://127.0.0.1:8000/users/add/"
payload = {"name": name, "ip": ip, "pubKey": pubKey}

r = requests.post(url, data=payload)
print("Status: {0}\nResponse: {1}".format(r, r.text))
