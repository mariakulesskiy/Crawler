import datetime
import lxml.html
import requests
import pytz
from dateutil.parser import parse

anon_array = ['Untitled', 'Guest', 'Unknown', 'Anonymous']


def get_site_data():
    posts = []
    html = requests.get('https://pastebin.com')
    doc = lxml.html.fromstring(html.content)
    new_posts = doc.xpath('//ul[@class="sidebar__menu"]')[0]
    for post in new_posts:
        link = post.xpath('a/@href')[0]
        html_details = requests.get('https://pastebin.com' + link)
        doc_details = lxml.html.fromstring(html_details.content)
        username = doc_details.xpath('//div[@class="username"]')
        if len(username) > 0:
            author = doc_details.xpath('//div[@class="username"]')[0]
            author_name = author.xpath('a')[0].text_content()
        else:
            author_name = ''
        title = doc_details.xpath('//h1')[0].text_content()
        content = doc_details.xpath('//textarea[@class="textarea"]')[0].text_content()
        date = parse(doc_details.xpath('//div[@class="date"]/span/@title')[0], tzinfos={"CDT": -5 * 3600})
        post_data = {
            'Author': author_name,
            'Title': title,
            'Content': content,
            'Date': date,
            '_id': link
        }
        for key in post_data:
            post_data[key] = normalize_data(post_data[key])
        posts.append(post_data)
    return posts


def normalize_data(value):
    if value in anon_array:
        return ''
    elif type(value) is datetime.datetime:
        return value.astimezone(pytz.UTC)
    else:
        return value.strip()
