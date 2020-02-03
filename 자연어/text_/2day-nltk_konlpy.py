text = 'Abc'

print(text.lower())
print(text.upper())

print(text.isupper())
print(text.islower())

print(text.upper().isupper())

from bs4 import BeautifulSoup as bs

import requests

url = "https://www.nytimes.com/2020/01/13/technology/oyo-hotel-india-softbank.html"
response = requests.get(url)

html = response.text
soup = bs(html, 'html5lib')
tags = soup.select("#story > section > div:nth-of-type(1) > div > p")

text = ""
for tag in tags:
    text+=tag.text

print(text)

#######################stopwords##########################
import nltk

nltk.download('stopwords')


from nltk.corpus import stopwords

eng_stopwords = stopwords.words('english')
print(eng_stopwords)

len(eng_stopwords)

words = ["설", "연휴", "민족", "대이동", "시작", "늘어", "교통량",
         "교통사고", "특히", "자동차", "고장", "상당수", "차지",
         "나타", "것", "기자"]

stopwords = ["가다", "늘어", "나타", "것", "기자"]

words2 = [w for w in words if w not in stopwords]
print(words2)


nltk.download('punkt')

########################tokenize##########################

from nltk.tokenize import word_tokenize

text = "Boeing’s troubles run deep. The 737 Max, its newest and most important jet, has been grounded since March after two deadly crashes killed 346 people."
print(word_tokenize(text))

from nltk.tokenize import sent_tokenize

print(sent_tokenize(text))

# tweet messenger 

from nltk.tokenize import TweetTokenizer
text = "@Jason, Let's finish #projectA quickly."
tknzr = TweetTokenizer()
print(tknzr.tokenize(text))

#정규 표현식을 사용하는 Tokenizer
from nltk.tokenize import RegexpTokenizer
text = """
ESPRESSO
caffeinated dreams espresso blend
ESPRESSO CON PANNA
double espresso + whipped cream
ESPRESSO MACCHIATO
double espresso + milk foam -traditional
"""
tokenizer = RegexpTokenizer(r'[A-Z]+')
print(tokenizer.tokenize(text))

text = """
AAA abc
BBB
DDD
fff
"""
tokenizer = RegexpTokenizer(r'[A-Z]+')
print(tokenizer.tokenize(text))


#############freqdist###################

from nltk import FreqDist

text = """
ESPRESSO
caffeinated dreams espresso blend
ESPRESSO CON PANNA
double espresso + whipped cream
ESPRESSO MACCHIATO
double espresso + milk foam -traditional
"""

fd = FreqDist(text.lower().split())
print(fd.most_common(5))
fd.plot(title="Word Frequency", cumulative=True)

fd.plot(title="Word Frequency")

words = set(text.lower().split())
for w in words:
    print(f"{w:12s} : {fd.freq(w):.4f}")
    
################ex#####################
import selenium
from selenium import webdriver

import time


driver = webdriver.Chrome('/home/pirl/Downloads/chromedriver')
driver.get('https://www.whitehouse.gov/briefings-statements/the-inaugural-address/')

text = ""
for i in range(4,81):
    selector = f"#main-content > div.page-content > div > div > p:nth-of-type({i})"
    ui = driver.find_element_by_css_selector(selector)
    print(ui.text)   
#    text += ui.text       

print(text)

fd = FreqDist(text.lower().split())
fd.most_common(5)

#stopwords delete
from nltk.corpus import stopwords
sw = stopwords.words('english')
result = text.lower().split()
text_swdel = [w for w in result if w not in sw ]

fd2 = FreqDist(text_swdel)
fd2.most_common(5)



#########################okt########################
from konlpy.tag import Okt

okt = Okt()
text = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
result = okt.morphs(text)
print(result)
print(okt.nouns(text))
print(okt.pos(text))
#####################kkma##########################
from konlpy.tag import Kkma
kkma=Kkma()
text = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
result = kkma.morphs(text)
print(result)
print(okt.nouns(text))
print(okt.pos(text))

###################stemming#####################

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

text = '''It is important to be immersed while you are pythoning with python. 
All pythoners have pythoned poorly at least once'''
text = text.lower()

# tokeninzer
words = word_tokenize(text)
print(words)

# stemming
porter_stemmer = PorterStemmer()
for w in words:
    print(w, porter_stemmer.stem(w))

#####korean stemming
okt = Okt()
text = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
result = okt.morphs(text, stem = True)
print(result)

########################ngram##########################
from nltk import ngrams

sentence = '''Chief Justice Roberts, President Cater, President Clinton,
President Obama, fellow Americans and people of the word, thank you.
We, the citizens of America are now joined in a great national effort
to rebuild our country and restore its promise for all of our people.'''

# bi-gram
grams = ngrams(sentence.lower().split(), 2)
for gram in grams:
    print(gram)

# tri-gram
grams = ngrams(sentence.lower().split(), 3)
for gram in grams:
    print(gram)



#####################pos_tag##########################
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
text = '''Boeing's troubles run deep. The 737 Max, its newest and most 
important jet, has been grounded since March after two deadly crashes killed 346 people.'''
tokens = word_tokenize(text)
nltk.download('averaged_perceptron_tagger')
tags = pos_tag(tokens)
print(tags)
result = [x[0] for x in tags if x[1][:2] == "NN"]
print(result)

from konlpy.tag import Okt
document = '봄과 함께 찾아온 따뜻한 신제품 소식'
okt = Okt()
words = okt.pos(document, stem=True)
clean_words = [x[0] for x in words if x[1] in ['Noun','Verb','Adjective']]
print(clean_words)


#####################pre-process###################
from konlpy.tag import Okt
from konlpy.tag import Komoran
import re
with open('/home/pirl/test/BigData/text_/code/day02/03_text_preprocessing/news.txt','r', encoding='utf8') as f:
    content = f.read()

p = re.compile("[\Wa-zA-Z0-9_]+")
content = re.sub(p, " ", content)

okt = Okt()
okt_morphs = okt.pos(content)
print(okt_morphs)

okt = Okt()
okt_nouns = okt.nouns(content)
print(okt_nouns)


from collections import Counter

c = Counter(okt_nouns)
mc = c.most_common(3)
print(mc)

################################wordcloud###########################3
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path

text = " ".join(okt_nouns)

FONT_PATH = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

wordcloud = WordCloud(max_font_size=70, max_words=30, background_color='white',
relative_scaling=.5, font_path=FONT_PATH).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


#########################embedding##############################
from konlpy.tag import Okt
phrase = "나는 자연어 처리를 배운다"
okt = Okt()
token = okt.morphs(phrase)
print(token)

word_set = {}
index = 0
for t in token:
    if t not in word_set:
        word_set[t] = index
        index += 1
print(word_set)


def one_hot_encoding(word, word_set):
    vector = [0] * len(word_set)
    index = word_set[word]
    vector[index] = 1
    return vector
print(one_hot_encoding("자연어", word_set))


#ex
import re

text1 = "정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다."
text1 = re.sub(r"\.", "", text1)

okt = Okt()
token = okt.morphs(text1)

bow = {}
index = 0
for t in token:
    if t not in bow:
        bow[t] = index
        index += 1
print(bow)

vec = []
for w, i in bow.items():
    count = token.count(w)
    vec.append(count)
print(vec)

########################scikit-learn##############################
from sklearn.feature_extraction.text import CountVectorizer
text_data = [
'나는 배가 고프다',
'내일 점심 뭐먹지',
'내일 공부 해야겠다.',
'점심 먹고 공부해야지'
]
# 단어 사전 구성
cv = CountVectorizer() # 객체 생성
cv.fit(text_data)
# 단어 목록 생성
print(cv.vocabulary_)
print(len(cv.vocabulary_))

result = cv.transform([text_data[0]])
print(result)

#####################TfidVectorizer###########################
from sklearn.feature_extraction.text import TfidfVectorizer
text_data = [
'나는 배가 고프다',
'내일 점심 뭐먹지',
'내일 공부 해야겠다.',
'점심 먹고 공부해야지'
]
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(text_data)
print(tfidf_vectorizer.vocabulary_)
sentence = [text_data[3]]
vector = tfidf_vectorizer.transform(sentence).toarray()
print(vector)



