from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"hello_world.html")

def showEggs(request):
    return HttpResponse("<h1> eggs are here honey</h1>")

def countWords(request):
    words = request.GET['textarea']
    wordslist = words.split()
    uniqelist = set(wordslist)

    dictWords= {word:0 for word in uniqelist}

    for word in wordslist:
          dictWords[word]+=1

    print("dictionary is ", dictWords)
    return render(request ,"countWords.html",{'count':len(wordslist), 'fullText':words,'wordDictionary':dictWords})