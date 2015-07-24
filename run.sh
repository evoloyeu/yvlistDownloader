# !/bin/bash

cd ./sptube/

scrapy crawl playlist -a playlistURL=$1

cd ..

python downloader.py $2
# pwd

