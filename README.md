# luckysocial

This is a small utility that will lookup a name at Google to find its homepage
and then look for social media accounts on the page (twitter, facebook,
instagram, youtube, and rss). This is rolling the dice a little bit because the
top ranked result is assumed to be the homepage for the name. It was really just
a proof of concept for looking up organization names, which you can read more
about [here](https://inkdroid.org/2020/09/05/organizations-on-twitter/).

You can run luckysocial on one name, or you can give it CSV file and it will add
relevant columns to it. As examples you can look at the included
[data.csv](https://github.com/edsu/luckysocial/blob/master/example/data.csv) and
[data-new.csv](https://github.com/edsu/luckysocial/blob/master/example/data-new.csv)
to see what the input and output can look like.

## Install

First you need to install some things like [Python3](https://python.org), and
then install luckysocial:

    pip install luckysocial

## Run

If you want to look up information about a single name you can:

    % luckysocial "uc santa barbara"

    name: uc santa barbara homepage: https://www.ucsb.edu/ twitter:
    https://twitter.com/ucsantabarbara facebook:
    https://www.facebook.com/ucsantabarbara instagram:
    https://www.instagram.com/ucsantabarbara

Or you can annotate a CSV file by giving it the path to your CSV file (it will
look for a `name` column).

    luckysocial data.csv

After it finishes you should see a data-new.csv file with the new columns.

If you have a differently named name column you can use the --name-col option:

    luckysocial --name-col "Org Name" data.csv

If you happen to know the homepage of the organization already and want to skip
the Google lookup you can use the `--url-col` parameter:

    ./luckysocial.py --url-col "Web Locationn" data.csv

## Develop

I'm sure that the logic for finding the accounts on a page could be improved.
If you'd like to test it out you can run the test suite:

    python setup.py test
