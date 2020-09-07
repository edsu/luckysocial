import luckysocial
import requests_html

http = requests_html.HTMLSession()

def test_lookup():
    info = luckysocial.lookup('ALASKA PUBLIC TELECOMMUNICATIONS INC')
    assert info['homepage'] == 'https://www.alaskapublic.org/about/'
    assert info['twitter'] == 'https://twitter.com/aprn'
    assert info['facebook'] == 'https://www.facebook.com/alaskapublic'
    assert info['instagram'] == 'https://www.instagram.com/alaskapublic'
    assert info['youtube'] == 'https://www.youtube.com/user/aptiadmin'
    assert info['rss'] == 'https://www.alaskapublic.org/feed/'

def test_get_social():
    info = luckysocial.get_social('https://www.alaskapublic.org/about/')
    assert info['twitter'] == 'https://twitter.com/aprn'
    assert info['facebook'] == 'https://www.facebook.com/alaskapublic'
    assert info['instagram'] == 'https://www.instagram.com/alaskapublic'
    assert info['youtube'] == 'https://www.youtube.com/user/aptiadmin'
    assert info['rss'] == 'https://www.alaskapublic.org/feed/'

def test_get_social_none():
    info = luckysocial.get_social(None)
    assert info['twitter'] == None
    assert info['facebook'] == None
    assert info['instagram'] == None
    assert info['youtube'] == None
    assert info['rss'] == None

def test_meta():
    url = "https://alaskabehavioralhealth.org/"
    doc = http.get(url)
    assert luckysocial.get_meta(doc, 'twitter:creator') == "https://twitter.com/AnchCMHS"
