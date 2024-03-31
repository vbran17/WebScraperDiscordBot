import requests
from bs4 import BeautifulSoup

class RunWeb:
  def __init__(self):
    self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}
    self.url = 'https://letterboxd.com/search/films/'

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '-'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words

  def search(self, keywords):
    response = requests.get(self.url+keywords, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_links = soup.findAll('a')
    return result_links

  def send_link(self, result_links, search_words): 
    baseurl = 'https://letterboxd.com'
    send_link = set()
    count = 0
    for link in result_links:
        text = link.text.lower()
        if search_words in text:  
          send_link.add(baseurl + link.get('href'))
          count += 1
        if count == 5:
          break
    return send_link
