import re
from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import *
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


# Create your views here.
def home(request):
    return render(request,'home.html',{})
def summarize(request):
    return render(request,'home.html',{})
def action(request):
    if request.method=='POST': 
        text =request.POST["message"]
   
# Tokenizing the text
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
# Creating a frequency table to keep the 
# score of each word
        count1=0
        freqTable = dict()
        for word in words:
            word = word.lower()
            count1+=1
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        if count1<=50:
            return render(request,'home.html',{'summary':"",})
# Creating a dictionary to keep the score
# of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()
   
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
   
# Average value of a sentence from the original text
   
        average = int(sumValues / len(sentenceValue))
   
# Storing sentences into our summary.
        summary = ''
        res=0
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        words1= word_tokenize(summary)
        for word in words1:
            res+=1
        res1="Number of words in Summary: "+str(res)+"."
        count2="Number of words in Passage: "+str(count1)+"."
        return render (request,'home.html',context={'text':text,'summary':summary,'count1':count2,'res':res1})
    else:
        return render(request,'home.html',{'summary':""})
def sample(request):
    return render(request,'sample.html',{})