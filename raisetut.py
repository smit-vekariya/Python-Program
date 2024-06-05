"""a=input("Enter your name:")
b=int(input("Enter you income"))
if b==0:
    raise Exception("stop becases 0.")
if a.isnumeric():
    raise Exception("number are not allowed.")

print(f"hellow {a}")"""
c=input("Enter your name:")
try:
    print(a)
except Exception as e:
    if c=="smit":
        print("smit is blockd")
    print("Exception hendeld")