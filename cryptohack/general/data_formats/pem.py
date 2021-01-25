from pwn import *
from Crypto.Util.number import bytes_to_long

with open("privacy_enhanced_mail.pem", 'r') as f:
    lines = f.read().splitlines() 

begin = "-----BEGIN RSA PRIVATE KEY-----"
end = "-----END RSA PRIVATE KEY-----"

key = ""

i = lines.index(begin) + 1
while lines[i] != end:
    key += lines[i]
    i += 1

with open("cert.der", 'wb') as f:
    f.write(b64d(key))

private_exponent = "\
7c3b1d534f299b43c1260876303c0a\
95be17bf91a5df2f1cacda7c75a023\
6e4f81e1210d27c0126fb34d80f27a\
41a4d7e48ca7c5b0e78878b19fd0d6\
c0bf6830fb8a4401b16d938ad54c4d\
0b356862056cb0554eb2ab8390ad18\
25b31dafbf2fc05d194f38c2f22420\
d3210ada0230242640cae005eb85cb\
c8dcca1825ea7496d9b170c5cbfe35\
4fe19a63102b82f38d5d7c25173520\
8b83a54240927f899848c16a5fe70c\
e950daff7bf9f4b71b598101a52048\
cd30c16cb994330b10592d2c95d4d0\
e579f5287ff74a88268d0389698c8f\
7b9ae813f39246893d02661cf08d9c\
bcec9f722cf76d0e96f1e17737e29e\
ce8676767cb6e1df0dbd2d731ed848\
b1"

print(int(private_exponent, 16))
