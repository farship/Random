import feedparser
import time
def public_projects_RSS():
    url = feedparser.parse('https://miguelmarquezoutside.com/rss')
    d2 = url.entries[0].description
    s1 = '<br/><br/><p>'
    i1 = d2.split(s1,1)[0]
    s2 = '<br/> <br/><p>'
    i2 = i1.split(s2,1)[0]
    i3 = i2.replace('<br/>','')
    f = open("Public Projects.html", "w")
    f.write('<head> <meta http-equiv="refresh" content="43200"> \n<link rel="icon" href="https://ih1.redbubble.net/image.1036241740.1273/flat,128x128,075,t.jpg"></head> \n<title>Public Projects</title> \n' + i3)
    f.close()
    time.sleep(86000)
    public_projects_RSS()
public_projects_RSS()