# -*- coding:utf-8 -*-
from aip import  AipSpeech
# 你的 APPID AK SK

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from test1 import getLength
import shutil

class VedioSound_to_words():
    def __init__(self, path, format ):
        self.path = path
        self.format = format
        temp_list = self.cdfile(self.path, self.format)  #
        for absolute_filename, path2, file, fileprofix, ttiimmee in temp_list:
            self.sound_process(path2, absolute_filename, file, fileprofix, "flv", ttiimmee)
            print(absolute_filename)
    def _vedio_to_sound(self, vedio):
        # vedio_to_soundcommand = 'ffmpeg -i opencv.flv -vn -ar 44100 -ac 2 -ab 192 -f mp3 audio.mp3'
        pass
        # 未验证：音频裁剪命令 command_line = "ffmpeg -i  " + cut_name + "  -vn -acodec copy -ss " + start_time + " -t 00:00:30 " + section_name
    def sound_process(self, path, absolute_filename, file, fileprofix, format, ttiimmee):
        new_audio_name = "New"+ str(fileprofix) + ".pcm"
        absolute_newfilename = path + "\\" +new_audio_name
        command_line_encoding = 'ffmpeg -y  -i ' + absolute_filename + '  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ' + absolute_newfilename + '\n'
        file_path =  r"C:\Users\Administrator\Desktop\command_line.txt"

        print(command_line_encoding)
        with open(file_path, 'a') as f:
            f.write(command_line_encoding)
       #查找音频的长度命令，结合ffmpg，需要有返回值
        #for 循环裁剪
        print('encoding is over')
        os.chdir(path)
        os.mkdir(str(ttiimmee))
        new_path = path + '\\' + str(ttiimmee)
        new_path_format = new_path + '\n'
        path_txt  = r"C:\Users\Administrator\Desktop\path.txt"
        with open(path_txt, 'a') as f:
            f.write(new_path_format)
        Copy = "Copy."+ str(format)
        shutil.copy(file, Copy)
        message = getLength(Copy)
        times = int(message[-2])
        os.remove(Copy)
        last_seconds = float(message[-1])
        start_time = 0
        end_time = 60
        i = 1
        while i <= (times+1):
            filenum = new_path + '\\' + 'sounds-'+ str(i) + '.pcm'
            if i > times:
                end_time = last_seconds + start_time
            i += 1
            command_line_split = 'ffmpeg -i ' + absolute_newfilename +' -ss ' + str(start_time) + ' -t ' + str(end_time) + ' ' + filenum + '\n'
            start_time += 60
            end_time += 60
            print(command_line_split)
            with open(file_path, 'a') as f:
                f.write(command_line_split)
    # def getLength(self, filename):
    #     result = subprocess.Popen(["ffprobe", path2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     return [x for x in result.stdout.readlines() if "Duration" in x]
    #读取文件夹里，含有视屏，音频的文件
    def cdfile(self, path, format):
        temp = []
        temp_list = []
        ttiimmee = 1
        for (root, dirs, files) in os.walk(path):
            for d in dirs:
                path_all = os.path.join(root, d)
                temp.append(path_all)
            # if dirs == []:
            #     for file in os.listdir(path):
            #         absolute_filename = path +"\\" +str(file)
            #         path2 = path
            #         file = file
            #         fileprofix, extension = os.path.splitext(file)
            #         temp_list.append((absolute_filename, path2, file, fileprofix))
        for path2 in temp:
            path2 = path2.decode("gbk") #需要解码
            for file in os.listdir(path2):
                absolute_filename = str(path2) + "\\" +str(file)
                fileprofix,extension = os.path.splitext(file)
                if extension == "."+ str(format):
                    temp_list.append((absolute_filename, path2, file, fileprofix, ttiimmee)) #文件绝对路径，文件夹，文件名(含后缀), 前缀名
                    ttiimmee += 1
        return temp_list
    def get_file_content(self):
        f = open(r'C:\Users\Administrator\Desktop\path.txt')
        line = f.readlines()
        for each in line:
            os.chdir(each)
            for eachabc in os.listdir(each):
                with open(eachabc, 'rb') as fp:
                    temp =  fp.read()
                    words = self.get_token(temp)
                path = os.chdir('..')
                with open(each, 'a') as f:
                    f.write(words)
    def get_token(self, data):
        APP_ID = '10838184'
        API_KEY = 'SNAhbhzgigmHoPAHWGTOOMSa'
        SECRET_KEY = 'a921e0f35a332c16a63b2b529c2389d6'
        # 初始化AipSpeech对象
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        # 读取文件
        result = aipSpeech.asr(self.get_file_content('16k.pcm'), 'pcm', 16000, {'lan': 'zh', })  # 这里填8000不行就改为16000
        print (result["result"][0])

if __name__ == '__main__':
    test = VedioSound_to_words(r'D:\003 Data\Baidu_Yunpan\shuaiqidelige',"flv")
    #输入的必须是印文的路径，并且，是层级结构


    #输入信息：
    #文件夹

