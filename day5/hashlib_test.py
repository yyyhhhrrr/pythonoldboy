#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import hashlib,hmac
m = hashlib.md5()
m.update(b"hello")
print(m.hexdigest()) # 16进制

h=hmac.new(b"123","样".encode(encoding="utf-8"))
print(h.digest())
print(h.hexdigest()) # 双层加密