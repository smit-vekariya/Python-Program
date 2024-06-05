def Student(fname,lname,**user):
    user['Frist name']=fname
    user['last name']=lname
    return user

if __name__=="__main__":
    MyStu=Student('smit','vekariya',location='rakot')
    print(MyStu)
    
