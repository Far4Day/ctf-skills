#!/usr/bin/python
# Script Rules - Hacking N Roll V 2017
# Flag: hnrv{pontodelpotro}
import hashlib
hashlist, filelist = {}, {}

def get_text(path):
    return open(path, 'r').readlines()

for number in range(1,665):
    hashlist.update({hashlib.sha1(str.encode(str(number))).hexdigest():number})
    filelist.update({number:hashlib.sha1(str.encode(str(number))).hexdigest()})
flag = []
for number in range(1, 665):
    try:
        flag.append(get_text(
                filelist.get(hashlist.get(filelist.get(number)))))
    except:
        continue
string = ""
for char in flag:
    hex_to_text = chr(int(''.join(char),16))
    string+= hex_to_text
after = string.split("{")[1]
print("Flag: hnrv{" + str(after.split("}")[0])+ "}")
