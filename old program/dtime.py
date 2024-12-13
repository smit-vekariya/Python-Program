client_list={1:"smit",2:"nayan",3:"parth"}
rule_list={1:"Exercise",2:"diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("client name is:")
    for key,value in client_list.items():
        print("press:" ,key, "for ",value,"\n")
    print("Select client name:")
    client_name=int(input())

    print("selected client is:",client_list[client_name],"\n")

    print("press 1 for rule.")
    print("press 2 for retrieve.")

    op=int(input())

    if op is 1:
        for key,value in rule_list.items():
            print("press:",key,"for ",value,"\n")
        print("Selectyour choice:")
        rule_name=int(input())
        print("selected job is:",rule_list[rule_name],"\n")
        f=open(client_list[client_name]+"_"+rule_list[rule_name]+".txt","a")
        while True:
            print("Enter",rule_list[rule_name],"\n", end="")
            mytext=input()
            f.write("["+str(getdate())+"]:"+mytext+"\n")
            k=input("Add more?(y/n):")
            if k == "n":
                break
        f.close()
    elif op is 2:
        for key,value in rule_list.items():
            print("press",key,"to retrieve",value,"\n",end="")
        rule_name=int(input())
        print(client_list[client_name],"-",rule_list[rule_name],"Report:","\n",end="")
        f=open(client_list[client_name]+"_"+rule_list[rule_name]+".txt","rt")
        contents=f.readlines()
        for line in contents:
            print(line,end="")
        f.close()


    else:
        print("Invalid input!!!")
    
except Exception as e:
    print("Wrong onput!!")