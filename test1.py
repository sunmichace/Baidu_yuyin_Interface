# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
from moviepy.editor import VideoFileClip


# def get_file_times(filename):
#     u"""
#     获取视频时长（s:秒）
#     """
#     clip = VideoFileClip(filename)
#     print(clip.duration)
#     file_time = timeConvert(clip.duration)
#     return file_time
#
# def timeConvert(size):  # 单位换算
#     M, H = 60, 60 ** 2
#     if size < M:
#         return str(size) + u'秒'
#     if size < H:
#         return u'%s分钟%s秒' % (int(size / M), int(size % M))
#     else:
#         hour = int(size / H)
#         mine = int(size % H / M)
#         second = int(size % H % M)
#         tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
#         return tim_srt
#
# a= get_file_times(r'output.wav')
#
# clip = VideoFileClip("test.mp3")
# print( clip.duration )

import subprocess
from aip import AipSpeech
def getLength(filename ):
  result = subprocess.Popen(["ffprobe", filename], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x][0].split(',')[0].split(':')


def _get_file_content(filePath):
  with open(filePath, 'rb') as fp:
    return fp.read()


def get_token(file):
  APP_ID = '4'
  API_KEY = 'Sa'
  SECRET_KEY = '89d6'
  aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
  result = aipSpeech.asr(_get_file_content(file), 'pcm', 16000, {'lan': 'zh', })  # 这里填8000不行就改为16000
  print(result)
  return (result["result"][0])
#返回秒