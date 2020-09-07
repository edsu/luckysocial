#!/usr/bin/env python3

import os
import re
import csv
import sys
import time
import random
import argparse
import collections
import requests_html

def main():
    parser = argparse.ArgumentParser(description="look up social media accounts")
    parser.add_argument('input', help='Either a name to lookup or a CSV file')
    parser.add_argument('--name-col', default='name', help='The column containing the name')
    parser.add_argument('--url-col', default=None, help='A column containing the URL to lookup')
    args = parser.parse_args()

    # if a name was passed in as input print what we know about it and exit

    if not os.path.isfile(args.input):
        info = {"name": args.input}
        info.update(lookup(args.input))
        if info:
            print_info(info)
        print()
        sys.exit()

    # otherwise we are processing a CSV

    in_csv = csv.DictReader(open(args.input))
    if not args.url_col and args.name_col not in in_csv.fieldnames:
        parser.error('{} column not found in {}'.format(args.name_col, args.input))
    if args.url_col and args.url_col not in in_csv.fieldnames:
        parser.error('{} column not found in {}'.format(args.url_col, args.input))

    fieldnames = in_csv.fieldnames + new_fields
    new_csv_file = args.input.replace('.csv', '-new.csv')
    out_csv = csv.DictWriter(open(new_csv_file, "w"), fieldnames=fieldnames)
    out_csv.writeheader()

    for row in in_csv:
        if not args.url_col:
            info = lookup(row[args.name_col])
            # TODO: make the sleep optional?
            # it is hear to prevent getting blocked by Google for scraping
            time.sleep(random.randint(0, 3))
        else:
            info = get_social(row[args.url_col])
        row.update(info)
        out_csv.writerow(row)
        print_info(row)

def lookup(name):
    result = {"homepage": get_homepage(name)}
    result.update(get_social(result["homepage"]))
    return result

def get_homepage(org_name):
    url = "https://google.com/search"
    resp = http.get(url, params={"q": org_name}, headers={"User-Agent": ua})
    resp.html.render()
    links = resp.html.find("div.r a")
    if len(links) > 0:
        return links[0].attrs["href"]
    else:
        return None

def get_social(url):
    no_result = {k: None for k in new_fields}
    if not url:
        return no_result

    if not url.startswith('http'):
        url = 'http://' + url

    try:
        doc = http.get(url)
    except Exception as e:
        return no_result

    return {
        "twitter": get_meta(doc, 'twitter:creator') or find_url(doc, r".*twitter.com/(?:#!/)?([a-z0-9_]+)/?$", "https://twitter.com/", ["intent"]),
        "facebook": find_url(doc, r".*facebook.com/([a-z0-9_]+)/?$", "https://www.facebook.com/"),
        "instagram": find_url(doc, r".*instagram.com/([a-z0-9_]+)/?$", "https://www.instagram.com/"),
        "youtube": find_url(doc, r".*youtube.com/user/([a-z0-9_]+)/?$", "https://www.youtube.com/user/"),
        "rss": get_rss(doc)
    }

def get_meta(doc, name):
    meta = doc.html.find('meta[name="{}"]'.format(name), first=True)
    if meta and meta.attrs['content']:
        # TODO: make not twitter specific
        return meta.attrs['content'].replace('@', 'https://twitter.com/')
    else:
        return None
 
def find_url(doc, pattern, prefix, ignore=[]):
    accounts = collections.Counter()
    for a in doc.html.find("a[href]"):
        m = re.match(pattern, a.attrs["href"], re.IGNORECASE)
        if m and m.group(1) not in ignore:
            accounts[m.group(1)] += 1
    if len(accounts) > 0:
        return prefix + accounts.most_common()[0][0] 
    else:
        return None

def get_rss(doc):
    links = doc.html.find('head link[rel="alternate"]')
    for link in links:
        if 'href' in link.attrs and 'comments' not in link.attrs['href']:
            return link.attrs['href']
    return None

def print_info(info):
    print()
    for k, v in info.items():
        if v:
            print('{}: {}'.format(k, v))

ua = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

http = requests_html.HTMLSession()
new_fields = ["homepage", "twitter", "facebook", "instagram", "youtube", "rss"]

if __name__ == "__main__":
    main()
