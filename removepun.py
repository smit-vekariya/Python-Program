pun='''!@#$%^&*()_+-=}{[]|\":<>?/.,;'''
mtstr="Heloo!!!! My:]} Name is ^&^smit"
strr=""

for mt in mtstr:
    if mt not in pun:
        strr=strr+mt
        
print(strr)