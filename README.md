# luckysocial

This is a small utility that will read a given CSV that has a name in it (there
can be others as well) and will write out a new CSV that includes all the old
columns and new ones for twitter, facebook, instagram, youtube, and rss.

The program looks up the name on Google and uses the top ranked result as the
homepage for the name, and then looks for social media accounts on the homepage.
It was really just a proof of concept for looking up organization names, which
you can read more about [here](https://inkdroid.org/2020/09/05/organizations-on-twitter/).

As examples you can look at the included [data.csv](https://github.com/edsu/luckysocial/blob/master/example/data.csv) and [data-new.csv](https://github.com/edsu/luckysocial/blob/master/example/data-new.csv) to see what the input and output can look like.

## Run

First you need to install some things like [Python3](https://python.org), and
the the requirements:

    pip install -r requirements.txt 

Then you can generate a file by giving it an input file (remember it must have a
'name' column:

    ./luckysocial.py data.csv

After it finishes you should see a data-new.csv file with the new columns.

If you have a differently named name column you can use the --name-col option:

    ./luckysocial.py --name-col "Org Name" data.csv

If you happen to know the homepage of the organization already and want to skip
the Google lookup you can use the `--url` parameter:

    ./luckysocial.py --url-col "Web Locationn" data.csv
