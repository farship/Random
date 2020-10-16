from bs4 import BeautifulSoup as bs
import requests
url = 'https://feeds.feedburner.com/sciencealert-latestnews'
req = requests.get(url)
soup = (bs(req.content, 'html.parser'))
titleList =[]
counter = 0
for title in soup.findAll('title'):
    if counter < 11:
        noTitle = str(title).replace("<title>", "")
        noEndTitle = noTitle.replace("</title>", "")
        titleList.append(noEndTitle)
        print(noEndTitle)
        counter += 1
    else:
        break
