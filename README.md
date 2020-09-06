# luckysocial

This is a small utility that will read a given CSV that has a column called
*name* in it (there can be others as well) and will write out a new CSV that
includes columns for twitter, facebook, instagram and youtube. The program looks
up the name on Google and uses the top ranked result as the homepage for the
name, and then looks for social media accounts on the homepage. It was really
just designed as a proof of concept for looking up organization names. You can
read more about that [here](https://inkdroid.org/2020/09/05/organizations-on-twitter/).

You can look at the included data.csv and data-new.csv to see what the input and
output can look like.
