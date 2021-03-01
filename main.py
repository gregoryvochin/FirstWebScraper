from urllib.request import urlopen
from bs4 import BeautifulSoup

# define scraper class to take in a URL and scrape for links


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        html = urlopen(self.url)
        parser = "html.parser"
        soup_object = BeautifulSoup(html, parser)
        for tag in soup_object.find_all("a"):
            url = str(tag.get("href"))
            print("\n" + url)


inputLink = input("Enter the URL you would like to scrape for links: ")

pageScrape = Scraper(inputLink)
pageScrape.scrape()
