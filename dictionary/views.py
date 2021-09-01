from django.shortcuts import render
import requests
from PyDictionary import PyDictionary
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

# Create your views here.
def index(request):
    return render(request,'index.html')

def syn_find(search):
    synonyms=[]
    for syn in wordnet.synsets(search):
        for l in syn.lemmas():
            synonyms.append(l.name())

    return list(set(synonyms))

def anto_find(search):
    antonyms = []
    synonyms=[]
    for syn in wordnet.synsets(search):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return list(set(antonyms))

def word(request):
    search = request.GET.get('search')
    dictionary=PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms= syn_find(search)
    synonyms=list(synonyms)
    antonyms= anto_find(search)
    antonyms=list(antonyms)
    if len(antonyms)==0:
        antonyms = ["no antonyms available for this word"]
    else:
        antonyms=(antonyms[:5])
    if len(synonyms)==0:
        synonyms = ["no synonyms available for this word"]
    else:
        synonyms=(synonyms[:5])
    context = {
        'meaning': meaning['Noun'][0:2],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request,'word.html',context)
