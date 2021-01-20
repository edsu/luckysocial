import luckysocial
import requests_html

http = requests_html.HTMLSession()

def test_lookup():
    info = luckysocial.lookup('ALASKA PUBLIC TELECOMMUNICATIONS INC')
    assert info['homepage'] == 'https://www.alaskapublic.org'
    assert info['twitter'] == 'https://twitter.com/aprn'
    assert info['facebook'] == 'https://www.facebook.com/alaskapublic'
    assert info['instagram'] == 'https://www.instagram.com/alaskapublic'
    assert info['youtube'] == 'https://www.youtube.com/user/aptiadmin'
    assert info['rss'] == 'https://www.alaskapublic.org/feed/'

def test_get_social():
    info = luckysocial.get_social('https://www.alaskapublic.org')
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
    assert luckysocial.get_meta(doc, 'twitter:site') == "https://twitter.com/AnchCMHS"

def test_relative_feed_url():
    url = 'https://www.homewardva.org'
    doc = http.get(url)
    assert luckysocial.get_rss(doc, url) == 'https://www.homewardva.org/?format=feed&type=rss'

def test_get_homepage():
    hp = luckysocial.get_homepage('uc santa barbara')
    assert hp == 'https://www.ucsb.edu'

    hp = luckysocial.get_homepage('ALASKA PUBLIC TELECOMMUNICATIONS INC')
    assert hp == 'https://www.alaskapublic.org'
