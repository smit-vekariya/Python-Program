"""
vowel=['a','e','i','o','u']
str1="my nameaaa is smit"
a=0
for c in str1:
    if c in vowel:
        if c=='a':
            a=a+1
                
    
print(a)
"""
vowels="aeiou"
str1="my nameaaa is smit"
srt1=str1.casefold()
count= {}.fromkeys(vowels,0)

    
for i in str1:
    if i in count:
        count[i]+=1
print(count)
