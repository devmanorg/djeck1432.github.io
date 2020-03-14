from bs4 import BeautifulSoup
import requests

if __name__=='__main__':
    response = requests.post('https://itproger.com/news/76')
    soup = BeautifulSoup(response.content)


    print(soup.div['block'])