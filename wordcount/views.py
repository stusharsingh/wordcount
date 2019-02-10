from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    noofwords = len(wordlist)
    i=0
    for word in wordlist :
        for char in word :
            i+=1
            average = i/noofword
    return render(render,'count.html',{'fulltext':fulltext,'count' : len(wordlist) "avgword": avgword})
    
    def about(request);
    return render(request,'about.html')    

