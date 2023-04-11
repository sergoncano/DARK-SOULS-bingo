import requests
from bs4 import BeautifulSoup
from sections import sections, not_items
from urllib import parse
import random
def get_items(section):
    r = requests.get(f'https://darksouls.wiki.fextralife.com/{section}')
    soup = BeautifulSoup(r.text, 'lxml')
    As = soup.findAll('a')
    srcs = []
    for a in As:
        imgs = a.find_all('img', {'src':True})
        for img in imgs:
            if img.parent.text:
                srcs.append(img.parent.text)
            elif section == 'Unique+Armor':
                srcs.append(img['alt'][:-4].replace('_', ' '))
    srcs.pop(0)
    return [item for item in srcs if item != '']

def get_pic(item):
    item_url = parse.quote_plus(item)
    r = requests.get(f'https://darksouls.wiki.fextralife.com/{item_url}')
    soup = BeautifulSoup(r.text, 'lxml')
    srcs = soup.find_all('img', {'src':True})
    src = srcs[1]['src'].replace(' ', '+')
    if src.startswith('https'):
        if requests.get(src).status_code != 404:
            return src
        else:
            return src.replace('+', '%20')
    else:
        if requests.get(f'https://darksouls.wiki.fextralife.com{src}').status_code != 404:
            return f'https://darksouls.wiki.fextralife.com{src}'
        else:
            return f'https://darksouls.wiki.fextralife.com{src}'.replace('+', '%20')

def get_wiki_url(item):
    item_url = parse.quote_plus(item)
    return f'https://darksouls.wiki.fextralife.com/{item_url}'

def bingo(sd):
    if sd != "":
        random.seed(sd)
    all_items = []
    for section in sections:
        items = get_items(section)
        for i in items:
            all_items.append(i)
    for item in not_items:
        if item in all_items:
            all_items.remove(item)
    bingolist = []
    for _ in range(25):
        bingolist.append(all_items[random.randint(0, len(all_items)-1)])
    return bingolist


if __name__ == '___main___':
    random.seed(input('Input seed: '))

    bing = bingo()

    bingo_url = []
    for b in bing:
        bingo_url.append(get_wiki_url(b))

    bingo_pic = []
    for b in bing:
        bingo_pic.append(get_pic(b))

    print(bing)