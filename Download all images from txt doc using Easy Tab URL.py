import urllib.request
import time
def gettheurls():
    with open('urls.txt') as file_of_urls:
        for line in file_of_urls:
            url = line.split()
            print (url)
            urllib.request.urlretrieve(url[-1], 'C:/Users/Peter/Documents/python testing/Download All Tabs/Downloads/' + str(url[0]))
if __name__ == "__main__":
    gettheurls()
    print('DONE!')
