from pytube import YouTube
import glob
import os
videos = []
for v in videos:
	YouTube(v).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
	print(v+" Ok!")
for f in glob.glob('*.mp4'):
	print(f)
	os.system(f'ffmpeg -i \"{f}\" -vcodec libx265 -filter:v fps=1 \"compressed-videos\{f}\"')
