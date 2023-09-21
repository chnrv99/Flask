from flask import Flask
import requests, json
from bs4 import BeautifulSoup


app = Flask(__name__)

# fetch news
# based on language on category
# take top 3 news for now, and do manual scraping for content alone
# 1hr once the job will run

# 2 categories - sports and 
# 2 languages - tamil and english
# 4 domains - sports()

# database
# source, title, link, date and time, category(positive/negative)

# API Key - 55a0cdab50f94dbaba53e0a8aa9a1c93
# Endpoint - https://api.bing.microsoft.com/
# Location - global

def scrap(url):
# def scrap():
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    # response = requests.get('https://www.hindustantimes.com/india-news/sonia-gandhi-came-to-pull-collar-nishikant-dubeys-reminder-in-lok-sabha-101695200191323.html', headers=agent)
    response = requests.get(url, headers = agent)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    # print("Hello")
    paras = soup.findAll('p')
    for para in paras:
        print(para.get_text())
    
    # print(title.get_text()) # Prints page title.
    
    # print(response.conten
    # t)

def fetchMSNews():
    newsAPI_KEY = '55a0cdab50f94dbaba53e0a8aa9a1c93'
    newsAPI_URL = 'https://api.bing.microsoft.com/'
    location = 'global'
  

    subscription_key = newsAPI_KEY
    search_term = "Microsoft"
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q" : "வணிக|பொழுதுபோக்கு|இந்தியா|வாழ்க்கை|அரசியல்|அறிவியல் மற்றும்|தொழில்நுட்பம்|விளையாட்டு|உலகம்","textDecorations": True,  "setLang" : "ta","cc" : "IN", "textFormat": "HTML","count" : "30"}
    response = requests.get(search_url, headers=headers, params=params)
    # response.raise_for_status()
    # search_results = json.dumps(response.json())
    # # print(search_results)
    # search_results = dict(search_results)
    # newses = search_results["sort"]
    # for news in newses:
    #     print(news["url"])
    data = response.json()
    print(data)
    print("\n\n")
    newses = data["value"]
    # print(newses)
    for news in newses:
        provider = news["provider"]
        
        print( provider[0]["name"] +" " + news["url"] + "\n\n")
        scrap(news["url"])
        print("\n\n\n\n")
        
    # same for english
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q" : "Business|Entertainment|India|Life|Politics|Science|Technology|Sports|World","textDecorations": True,  "setLang" : "ta","cc" : "IN", "textFormat": "HTML","count" : "30"}
    response = requests.get(search_url, headers=headers, params=params)
    # response.raise_for_status()
    # search_results = json.dumps(response.json())
    # # print(search_results)
    # search_results = dict(search_results)
    # newses = search_results["sort"]
    # for news in newses:
    #     print(news["url"])
    data = response.json()
    print(data)
    print("\n\n")
    newses = data["value"]
    # print(newses)
    for news in newses:
        provider = news["provider"]
        
        print( provider[0]["name"] +" " + news["url"] + "\n\n")
        scrap(news["url"])
        print("\n\n\n\n")
        
        
    
    
    
    
        
    
fetchMSNews()


def fetchGNews(lang, category):
    newsAPI_KEY = 'd73724588f06f6269a5dfbd8ec4fb267'
    newsAPI_URL = 'https://gnews.io/api/v4/top-headlines?'
    
    # add timings logic
    # 
    # 
    
    
    final_URL = newsAPI_URL + '?lang=' + lang + '&country=in&apikey=' + newsAPI_KEY
    
    
    r = requests.get(final_URL)
    data = r.json()
    # print(data)
    articles = data['articles']
    # print(articles)
    
    for article in articles:
        print(article['title'])
        print(article['description'])
        print(article['content'])
        print(article['url'])
        print(article['publishedAt'])
        print(article['source'])
        print("Scraping now: .... \n")
        scrap(str(article['url']))
        print("\n\n")
        
        
        
        
    

def fetchNews(lang):
    print("Fetching for language: " + lang)
    newsAPI_KEY = '0f25275ebe70404eb560a6c36065bee5'
    # newsAPI_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey='
    newsAPI_URL = 'https://newsapi.org/v2/top-headlines?country=in'
    
    
    # add timings logic
    # 
    # 
    
    
    final_URL = newsAPI_URL  + '&lang=' + lang  + '&apikey='+ newsAPI_KEY
    r = requests.get(final_URL)
    data = r.json()
    print(data)
    


@app.route('/')
def hello():
    # fetchNews('hi')
    # scrap()
    fetchMSNews()
    return "Hello"

if __name__ == "__main__":
    app.run()