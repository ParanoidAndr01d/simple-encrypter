# -*- coding: utf-8 -*-
"""simple encrypter

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dd2y6aPZUFS56DBRtKyfZHvuf74FXndE
"""

import hashlib

string = str(input("Hello. Please enter the string you would like to encrypt: "))

encoded = string.encode()
string_md5 = hashlib.md5(encoded)
string_sha1 = hashlib.sha1(encoded)
string_sha2 = hashlib.sha256(encoded)
string_sha3 = hashlib.sha384(encoded)

print("MD5: ", string_md5.hexdigest())
print("SHA1: ", string_sha1.hexdigest())
print("SHA256: ", string_sha2.hexdigest())
print("SHA384: ", string_sha3.hexdigest())