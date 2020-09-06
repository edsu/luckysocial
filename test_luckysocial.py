import requests_html
from luckysocial import get_meta

http = requests_html.HTMLSession()

def test_meta():
    url = "https://alaskabehavioralhealth.org/"
    doc = http.get(url)
    assert get_meta(doc, 'twitter:creator') == "@AnchCMHS"
