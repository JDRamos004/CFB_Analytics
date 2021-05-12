import requests
from lxml import html


def scrape_cont(page_xpath, page_url):
    response = requests.get(url)
    byte_data = response.content
    tree = html.fromstring(byte_data)
    return tree.xpath(page_xpath)


url = 'https://www.ncaa.com/standings/football/fbs'
xpath = '//td/text()'

stats = scrape_cont(xpath, url)

print(stats)
