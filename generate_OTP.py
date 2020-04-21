import random

f = open("OTP", "w")

#generowanie klucza
key = ""
for i in range(2000):
    x = random.randint(0, 255)
    key += str(x)
    if i <1999:
        key += " "

print(key)
f.write(key)
f.close()


