lock1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def caesar(lock):
    key = ""
    for i in lock:
        n = ord(i)
        print(n)
        if ord(i) < 121 and ord(i) > 96:
            n = ord(i) + 2
        elif ord(i) > 120:
            n = ord(i) - 26 + 2
        s = chr(n)
        key = key + s
    print(key)
caesar(lock1)
caesar("map")