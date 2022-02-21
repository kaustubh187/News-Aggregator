from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup 
from toll.models import Headline
# Create your views here.
titles=[]
images=[]
urls=[]
def scrape(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/breaking-news/news-in-brief"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    News=soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})

    for article in News:
        main=article.find_all('a',href=True)
        linkx=article.find('a', {"class":"sc-1out364-0 hMndXN js_link"} )
        link=linkx['href']
        imgx=main[0].find('img',src=True)
        image_src=imgx['data-srcset'].split(" ")[-4]
        titlex=article.find('h2',{"class":"sc-759qgu-0 iRbzKE cw4lnv-6 pdtMb"})
        title=titlex.text
        titles.append(title)
        images.append(image_src)
        urls.append(link)
        new_headline = Headline()
        #Headline.objects.all().delete()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
  
    return redirect("../")
def grape(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/latest"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    News=soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})

    for article in News:
        main=article.find_all('a',href=True)
        linkx=article.find('a', {"class":"sc-1out364-0 hMndXN js_link"} )
        link=linkx['href']
        imgx=main[0].find('img',src=True)
        image_src=imgx['data-srcset'].split(" ")[-4]
        titlex=article.find('h2',{"class":"sc-759qgu-0 iRbzKE cw4lnv-6 pdtMb"})
        title=titlex.text
        titles.append(title)
        images.append(image_src)
        urls.append(link)
        new_headline = Headline()
        #Headline.objects.all().delete()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
  
    return redirect("../")
def entertainment(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/entertainment/news-in-brief"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    News=soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})

    for article in News:
        main=article.find_all('a',href=True)
        linkx=article.find('a', {"class":"sc-1out364-0 hMndXN js_link"} )
        link=linkx['href']
        imgx=main[0].find('img',src=True)
        image_src=imgx['data-srcset'].split(" ")[-4]
        titlex=article.find('h2',{"class":"sc-759qgu-0 iRbzKE cw4lnv-6 pdtMb"})
        title=titlex.text
        titles.append(title)
        images.append(image_src)
        urls.append(link)
        new_headline = Headline()
        #Headline.objects.all().delete()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
  
    return redirect("../")

def sports(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/sports/football"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    News=soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})

    for article in News:
        main=article.find_all('a',href=True)
        linkx=article.find('a', {"class":"sc-1out364-0 hMndXN js_link"} )
        link=linkx['href']
        imgx=main[0].find('img',src=True)
        image_src=imgx['data-srcset'].split(" ")[-4]
        titlex=article.find('h2',{"class":"sc-759qgu-0 iRbzKE cw4lnv-6 pdtMb"})
        title=titlex.text
        titles.append(title)
        images.append(image_src)
        urls.append(link)
        new_headline = Headline()
        #Headline.objects.all().delete()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
  
    return redirect("../")

def gaming(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/ogn/news"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    News=soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})

    for article in News:
        main=article.find_all('a',href=True)
        linkx=article.find('a', {"class":"sc-1out364-0 hMndXN js_link"} )
        link=linkx['href']
        imgx=main[0].find('img',src=True)
        image_src=imgx['data-srcset'].split(" ")[-4]
        titlex=article.find('h2',{"class":"sc-759qgu-0 iRbzKE cw4lnv-6 pdtMb"})
        title=titlex.text
        titles.append(title)
        images.append(image_src)
        urls.append(link)
        new_headline = Headline()
        #Headline.objects.all().delete()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
  
    return redirect("../")

def politics(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/politics/news-in-brief"
    content = session.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    News=soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})

    for article in News:
        main=article.find_all('a',href=True)
        linkx=article.find('a', {"class":"sc-1out364-0 hMndXN js_link"} )
        link=linkx['href']
        imgx=main[0].find('img',src=True)
        image_src=imgx['data-srcset'].split(" ")[-4]
        titlex=article.find('h2',{"class":"sc-759qgu-0 iRbzKE cw4lnv-6 pdtMb"})
        title=titlex.text
        titles.append(title)
        images.append(image_src)
        urls.append(link)
        new_headline = Headline()
        #Headline.objects.all().delete()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
  
    return redirect("../")

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        "data" : headlines,
    }
    return render(request, "index.html", context)

# def index(request):
#     return render(request, 'index.html')
# def index(request):
#     return render(request, 'index.html', {'titles':titles, 'urls': urls, 'images':images})
