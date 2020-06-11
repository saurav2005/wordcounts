from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request ,'home.html')
def counts(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
            #.items is converting dict into list
    sorteddict=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)



    return render(request , 'counts.html',{'fulltext':fulltext,'networds':len(wordlist),'sorteddict':sorteddict})
