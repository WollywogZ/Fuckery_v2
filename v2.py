from __future__ import unicode_literals
import os
import ffmpeg

path_mp4 = './mp4'
path_raw = './raw'
# video = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
# # print(video.streams.filter(only_audio=True).all())
# video.streams.filter(res="1080p").first().download(path_mp4)

print(os.listdir(path_raw))
trackName = '【CTGP WR】 Volcanic Valley - 223937 - Daseia'

input_video = ffmpeg.input('./raw/%s.mp4' % trackName)
# print(input_video)
input_audio = ffmpeg.input('./raw/%s.webm' % trackName)
# print(input_audio)
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./mp4/%s.mp4' % trackName).run()

