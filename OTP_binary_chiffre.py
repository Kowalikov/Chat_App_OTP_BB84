
def chiffOTP(text, OTPfile):

    f = open(OTPfile, 'r')
    key = f.read()
    key_list = key.split(" ")
    chmess = ''
    ts = list(text)

    for i in range(len(text)):
        chmess += chr(int(ord(ts[i]) ^ int(key_list[i])))

    return chmess

def dechiffOTP(chmess, OTPfile):

    f = open(OTPfile, 'r')
    key = f.read()
    key_list = key.split(" ")
    chmesse = list(chmess)
    unmess = ''

    for i in range(len(chmess)):
        unmess += chr(int(ord(chmesse[i]) ^ int(key_list[i])))

    return unmess




