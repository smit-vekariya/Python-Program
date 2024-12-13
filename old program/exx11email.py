import re
str='''
 Director (International Affairs)
Mr. Rajen Chatterjee
 : rajen.chatterjee@alliance.edu.in
 : +91 80 3093 8075

 Director (Admissions)
Mr. Abhay Chebbi
 : abhay.chebbi@alliance.edu.in
 : +91 9663646464

 Human Resources Department
 : hrd@alliance.edu.in
 : +91 80 3093 8210 / 8204'''
 
mail=re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]",str)
print(mail)