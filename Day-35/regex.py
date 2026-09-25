
import re

pattern = r'[aeiou0-9]'   #{10} is 10 digits
pattern2 = r'h.t'
pattern3 = r'^[a-z]'
pattern4 = r'[a-z]$' #endswith
pattern5 = r'ab*' #ab+ means atleast one or more
pattern6 = r'^(91|0)'
pattern7 = r'^[0-9]{2}'


text1 = '12codegnan2026'
text2 = 'codegnan2026'
text3 = '4355667456'
text4 = 'java,python@c:flask_mysql&django'
text5 = 'Hand loom hot hit hat hood wood hatch wood8'
text6 = 'a ab abbb abbbbbbbbbb aaaabbbbbbbbbbbbbbb aabaaaa'
text7 = '0914356789'
text8 = 'fdsgdhfh45667gfhgjDFGHFJDD'


res1 = re.match(pattern,text2)
res2 = re.search(pattern,text1)
res3 = re.findall(pattern,text1)
res4 = re.finditer(pattern,text1)
res5 = re.fullmatch(pattern,text3)
res6 = re.split(pattern,text4)
res7 = re.sub(pattern,'*',text4)
res8 = re.findall(pattern2,text5)
res9 = re.findall(pattern3,text5)
res10 = re.findall(pattern4,text5)
res11 = re.findall(pattern5,text6)
res12 = re.findall(pattern6,text7)
res13 = re.findall(pattern7,text8)

for i in res4:
    print(i.group(), i.start())

print(res1.group() if res1 else 'Pattern not matched')
print(res2.group() if res2 else 'Pattern not matched')
print(res2)
print(res3)
print(res5.group() if res5 else 'Pattern not matched')
print(res6)
print(res7)
print(res8)
print(res9)
print(res10)
print(res11)
print(res12)
print(res13)

#name validation
name = input('Enter your name: ')
pattern8 = r'^[a-zA-Z]{2,25}( [a-zA-Z]{2,25})+$'

res14 = re.fullmatch(pattern8,name)

print('Valid Name' if res14 else 'Invalid Name')

#Email Validation
mail = input('Enter your mail: ')
pattern9 = r'^[a-zA-Z._0-9]+@[a-zA-Z._0-9]+\.[a-z]{2,}$'

res15 = re.fullmatch(pattern9,mail)

print('Valid Email' if res15 else 'Invalid Email')
