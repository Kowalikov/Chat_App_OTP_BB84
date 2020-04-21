import random

def conv(text):
    tl = list(text)
    ota = []
    ots = ""
    for i in range(len(text)):
        ota.append(ord(tl[i]))
        ots += str(ota[i])
        if i < len(text)-1:
            ots+= " "
    return ots

def chiffOTP(text, OTPfile):
    #if text > 2000
    f = open(OTPfile, 'r')
    key = f.read()
    key_list = key.split(" ")
    ts = list(text)
    te = []
    tes = ""
    for i in range(len(text)):
        te.append(ord(ts[i]))
        te[i] = (te[i]+int(key_list[i]))%256
        tes += str(te[i])
        if i < len(text)-1:
            tes += " "
    f.close()
    return tes

def dechiffOTP(tes, OTPfile):
    ts = ""
    f = open(OTPfile, 'r')
    key = f.read()
    key_list = key.split(" ")
    tes_list = tes.split(" ")
    for i in range(len(tes_list)):
        te = (int(tes_list[i])-int(key_list[i]))%256
        ts += chr(te)
    f.close()
    return ts



"""#test funkcji
msg = "morgen"
print(msg)
msg_chiff = chiffOTP(msg, "OTP")
print(msg_chiff, type(msg_chiff))
msg_ch_bit = bytes(msg_chiff, "utf-8")
msg_chiff2 = msg_ch_bit.decode("utf8")
msg_dechiff = dechiffOTP( msg_chiff2, "OTP")
print(msg_dechiff)

"""

