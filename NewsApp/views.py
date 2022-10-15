from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='078af8df3ea343409a37075af5cbc533')
    top = newsapi.get_top_headlines(sources='techcrunch')

    l = top['articles']
    news = []
    desc = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(news,desc,img)
    context = {'mylist':mylist}

    return render(request,'index.html', context)

