import requests
from base64 import encodebytes, b64encode
from xml.etree import ElementTree
from Crypto.Cipher import AES
import qrcode
import sys

def encode(msg : str):
    return b64encode(msg.encode(encoding='utf-8')).decode()

def encrypt(msg, secret):
    iv = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    cipher = AES.new(secret.encode(encoding='utf-8'), AES.MODE_CBC, iv)
    def fill_padding(msg):
        padding_sz = 16
        pad =  lambda s: s + (padding_sz - len(s) % padding_sz) * chr(padding_sz - len(s) % padding_sz)
        return pad(msg).encode()      
    return encodebytes(cipher.encrypt(fill_padding(msg))).decode().strip()


if __name__ == "__main__":
    # 학번
    rid = ""
    # 비밀번호
    pw = ""
    # 전화번호
    tel_no =  ""
    try:
        rid = sys.argv[1]
        pw = sys.argv[2]
        tel_no = sys.argv[3]
    except:
        print("python poc.py [학번] [비밀번호] [전화번호]")
        exit(1)
    real_id = f"0{rid}"
    base_url = "https://mobileid.kw.ac.kr"

    with requests.session() as s:
        r = s.post(base_url + "/mobile/MA/xml_user_key.php", {
            'user_id' : encode(real_id)
        })
        

        secret = ElementTree.fromstring(r.text).find("item").find("sec_key").text
        r = s.post(base_url + '/mobile/MA/xml_login_and.php', {
            'real_id' : encode(real_id),
            'rid': encode(rid),
            'device_gb': 'A',
            'tel_no': tel_no,
            'pass_wd': encrypt(pw, secret) 
        })
        with open("./test.xml", "w", encoding="utf-8") as f:
            f.write(r.text)

        auth = ElementTree.fromstring(r.text).find("item").find("auth_key").text
        r = s.post(base_url + '/mobile/MA/xml_userInfo_auth.php', {
            'real_id': encode(real_id),
            'auth_key': auth,
            'new_check': "Y"   
        })
        qr = ElementTree.fromstring(r.text).find("item").find("qr_code").text
        img = qrcode.make(qr)
        img.save("qr.png")