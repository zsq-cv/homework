import random
def generate():
    sentence = ' '
    noun_phrase=' '
    verb_phrase=' '
    Article = ['一个', '这个']
    noun = ['篮球', '女人', '桌子', '小猫']
    verb = ['看着', '听着', '看见']
    Adj = ['蓝色的', '好看的', '小小的', '年轻的']
    a=random.randint(0,len(Article)-1)
    b=random.randint(0,len(noun)-1)
    c=random.randint(0,len(verb)-1)
    d=random.randint(0,len(Adj)-1)
    noun_phrase = Article[a]+Adj[d]+noun[b]
    verb_phrase=verb[c]+noun_phrase
    sentence=noun_phrase+verb_phrase
    return sentence
print(generate())
