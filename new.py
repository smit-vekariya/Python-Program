def po(n):
    string="my name is smit"
    new_string = string[:n-1]+string[n:]
    print(new_string)
        
posi=int(input("Enter:"))
po(posi)