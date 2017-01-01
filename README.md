### Site Fetch

TODO

### Getting Data

The current data source is a txt file of the top 1,000,000 sites, fetched from
https://statvoo.com/dl/top-1million-sites.csv.zip

This needs to be trimmed into a more reasonable number. Use the following command line script to trim it to a more reasonable number, as well as remove line prefixes:

    head -50000 data.txt | cut -d, -f2 | cut -d/ -f1 > topsites.txt
