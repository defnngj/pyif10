from Crypto.Cipher import AES

# 加密
obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
message = "The answer is no"   #{"id":1, "name":"jack ma"}"
ciphertext = obj.encrypt(message.encode('utf-8'))
print(ciphertext)


# # 解密
# obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
# s = obj2.decrypt(ciphertext).decode()
# print(s)

def add(a, b):
    return a + b


bbb = lambda a, b: a + b + a

print(add(1,2))
print(bbb(1,2))