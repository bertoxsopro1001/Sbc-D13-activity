user_input, emty_list,emty_str,special_char,emty_str2 = input("Enter Inputs : "), [], "",[",", "-", "%", "&", "!", "?","."],""
for i in user_input:
    if i in special_char:
        emty_list.append(emty_str)
        emty_str = ""
    else:
        emty_str += i
emty_list.append(emty_str)

print(emty_list)