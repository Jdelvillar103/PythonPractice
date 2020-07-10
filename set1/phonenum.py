def isPhoneNumber(txt):
    if len(txt) !=12:
        return False
    for i in range(0,3):
       if not txt[i].isdecimal():
        return False
    if txt[3] !='-':
        return False
    for i in range(4,7):
           if not txt[i].isdecimal():
            return False
    if txt[7] !='-':
        return False
    for i in range(8,12):
           if not txt[i].isdecimal():
            return False
    return True

print(isPhoneNumber('bloop'))