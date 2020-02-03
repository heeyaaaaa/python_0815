text = '''
park 800905-1049118
kim 700905-1059119
'''
result = []
for line in text.split('\n'):
    for word in line.split(" "):
        if len(word)==14:
            result.append(word[:7]+'*'*7)

result


import re


text = '''
park 800905-1049118 sfasfsfsfsafsaf
kim 700905-1059119sfsfsdfsfsdfafsdf
gslkjelijfoijeflsjlfjskdlflskfd
'''

p = re.compile("\d+\-\d+")
print(p.findall(text))



text = '''abc defabc'''

p = re.compile('abc')
p.findall(text)

result = p.search(text)

if result:
    print(result)

text = "010-1234-5678"

p = re.compile(r"-")
m = p.sub("@@",text)

print(m)

text = '''내가 그린 기린 그림은 잘 그린 기린 그림이고
네가 그린 기린 그림은 잘 못 그린 기린 그림이다.'''
p = re.compile(r"기린")
m = re.findall(p, text)
print(len(m))


text = "babc afc aaaaaaaaa 010-9333-4299-  ABC"

p = re.compile(r"[a-zA-z]+")
p.findall(text)

p = re.compile(r"[0-9]+")
p.findall(text)

p = re.compile(r"^[^0-9-]+")
p.findall(text)

p = re.compile(r"[a|b|c]+")
p.findall(text)


text = """
a1.xlsx
b1.xlsx
c1.xlsx
"""

p = re.compile(r"[ab0-9]{2}.xlsx")
p.findall(text)


p = re.compile(r"[ab]\d.xlsx")
p.findall(text)


text = """
Brayden Jo 010-8212-1212 brayden.jo@outlook.com
Lukas Yoo 01087671212 lukas.yoo@gmail.com
"""

p = re.compile(r"\w+.\w+@\w+.\w+")
p.findall(text)

p = re.compile(r"\d+-?\d+-?\d+")
p.findall(text)

