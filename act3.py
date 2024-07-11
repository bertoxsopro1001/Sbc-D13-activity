user,keeys,emty_l,Emty_Str  = input("Enter words: "), ["Un", "Re"],[],""

i = 0
while i < len(user):
    check = user[i:i+2]  
    if check in keeys:
        if Emty_Str:
            emty_l.append("##" + Emty_Str)
        emty_l.append(check)
        Emty_Str = ""
        i += 2 
    else:
        Emty_Str += user[i]
        i += 1

if Emty_Str:
    emty_l.append("##" + Emty_Str)

print(emty_l)
