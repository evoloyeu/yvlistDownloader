import sys
from pytube import YouTube

# not necessary, just for demo purposes
from pprint import pprint
# from __future__ import print_function

filename = './sptube/playlist.txt'
def  readURL(filename):
	fs = open(filename)
	urls = []

	for f in fs:
		if len(f) > 0:
			urls.append(f)
			print f

	return urls

def downloader(savePath, url):
	yt = YouTube()

	# Set the video URL.
	yt.url = url

	# Once set, you can see all the codec and quality options YouTube has made
	# available for the perticular video by printing videos.

	# pprint(yt.videos)

	#[<Video: MPEG-4 Visual (.3gp) - 144p>,
	# <Video: MPEG-4 Visual (.3gp) - 240p>,
	# <Video: Sorenson H.263 (.flv) - 240p>,
	# <Video: H.264 (.flv) - 360p>,
	# <Video: H.264 (.flv) - 480p>,
	# <Video: H.264 (.mp4) - 360p>,
	# <Video: H.264 (.mp4) - 720p>,
	# <Video: VP8 (.webm) - 360p>,
	# <Video: VP8 (.webm) - 480p>]

	# The filename is automatically generated based on the video title.
	# You can override this by manually setting the filename.

	# view the auto generated filename:
	# from __future__ import print_function
	print(yt.filename)
	print(yt.url)

	#Pulp Fiction - Dancing Scene [HD]

	# set the filename:
	# yt.filename = 'Dancing Scene from Pulp Fiction'

	# You can also filter the criteria by filetype.

	# pprint(yt.filter('flv'))

	#[<Video: Sorenson H.263 (.flv) - 240p>,
	# <Video: H.264 (.flv) - 360p>,
	# <Video: H.264 (.flv) - 480p>]

	# notice that the list is ordered by lowest resolution to highest. If you
	# wanted the highest resolution available for a specific file type, you
	# can simply do:
	mp4s = yt.filter('mp4')

	# print(yt.filter('mp4')[-1])
	#<Video: H.264 (.mp4) - 720p>

	# you can also get all videos for a given resolution
	# pprint(yt.filter(resolution='480p'))

	#[<Video: H.264 (.flv) - 480p>,
	#<Video: VP8 (.webm) - 480p>]

	# to select a video by a specific resolution and filetype you can use the get
	# method.

	# video = yt.get('mp4', '720p')

	# NOTE: get() can only be used if and only if one object matches your criteria.
	# for example:

	pprint(yt.videos)

	#[<Video: MPEG-4 Visual (.3gp) - 144p>,
	# <Video: MPEG-4 Visual (.3gp) - 240p>,
	# <Video: Sorenson H.263 (.flv) - 240p>,
	# <Video: H.264 (.flv) - 360p>,
	# <Video: H.264 (.flv) - 480p>,
	# <Video: H.264 (.mp4) - 360p>,
	# <Video: H.264 (.mp4) - 720p>,
	# <Video: VP8 (.webm) - 360p>,
	# <Video: VP8 (.webm) - 480p>]

	# Notice we have two H.264 (.mp4) available to us.. now if we try to call get()
	# on mp4..
	if len(mp4s) > 0:
		video = mp4s[-1]
		video.download(savePath)
	else:
		video = yt.videos[-1]
		video.download(savePath)
	# MultipleObjectsReturned: get() returned more than one object -- it returned 2!

	# In this case, we'll need to specify both the codec (mp4) and resolution
	# (either 360p or 720p).

	# Okay, let's download it!
	# video.download()

	# Downloading: Pulp Fiction - Dancing Scene.mp4 Bytes: 37561829
	# 37561829  [100.00%]

	# Note: If you wanted to choose the output directory, simply pass it as an
	# argument to the download method.
	# video.download(savePath)

urls = readURL(filename)
for url in urls:
	downloader( sys.argv[1], url)


