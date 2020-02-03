from konlpy.tag import Okt

okt = Okt()
text = "한글 자연어 처리는 재밌다. 이제부터 열심히 해야지."
#text = "한글 자연어 처리는 재밌다. 이제부터 열심히 해야겠어."
#text = "한글 자연어 처리는 재밌다. 이제부터 열심히 하겠다."
#text = "한글 자연어 처리는 재밌다. 이제부터 열심히 할꺼야."

print(okt.morphs(text))
print(okt.morphs(text, stem=True))