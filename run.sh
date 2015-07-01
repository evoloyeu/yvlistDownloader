# !/bin/bash

cd ./sptube/

scrapy crawl playlist -a playlistURL=$1
# echo $0
# echo $1
# echo $2
# pwd

cd ..

python downloader.py $2
# pwd

