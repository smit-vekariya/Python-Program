filename="python.txt"
with open(filename) as files:
    lines=files.readlines()
pi_string=''
for line in lines:
    pi_string+= line.rstrip()
print(len(pi_string))