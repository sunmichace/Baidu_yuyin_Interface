# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from aip import  AipSpeech
import os
from test1 import getLength
import shutil
import time

class Single():
    def __init__(self, path, filename_profix, format):
        self.filename_profix = filename_profix
        self.path = path
        self.format = format
        self.absolute_filename = str(self.path) + "\\" + str(self.filename_profix) + '.' + self.format
        self.new_audio_name = "New"
        self.new_folder = str(self.path) + "\\" + str(self.new_audio_name)
        # self.absolute_newfilename = str(self.path) + "\\" + str(self.new_audio_name) + "\\" + self.new_audio_name
        self.file_path =  r"C:\Users\Administrator\Desktop\command_line.txt"
        self.txt = self.new_folder + "\\cotent.txt"

        self.sound_process()
        self.detect(self.new_folder)

    def _get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    def get_token(self, file):
        APP_ID = '10838184'
        API_KEY = 'SNAhbhzgigmHoPAHWGTOOMSa'
        SECRET_KEY = 'a921e0f35a332c16a63b2b529c2389d6'
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = aipSpeech.asr(self._get_file_content(file), 'pcm', 16000, {'lan': 'zh', })  # 这里填8000不行就改为16000
        print(result)
        return (result["result"][0])

    def sound_process(self):
        os.chdir(self.path)
        os.mkdir(self.new_audio_name)
        os.chdir(self.new_folder)
        Copy = "Copy." + str(self.format)
        shutil.copy(self.absolute_filename, Copy)
        message = getLength(Copy)
        self.times = int(message[-2])
        last_seconds = float(message[-1])
        start_time = 0
        during_time = 59
        i = 1
        self.absolute_newfilename = self.new_folder + "\\" + Copy
        while i <= (self.times + 1):
            filenum = self.path + '\\' + self.new_audio_name + '\\' + 'sounds-' + str(i) + '.' + self.format
            if i > self.times:
                during_time = last_seconds
            i += 1
            command_line_split = 'ffmpeg -i ' + self.absolute_newfilename + ' -ss ' + str(start_time) + ' -t ' + str(
                during_time) + ' ' + filenum + '\n'
            start_time += 60

            print(command_line_split)
            with open(self.file_path, 'a') as f:
                f.write(command_line_split)
        a = 1
        while a <= (self.times + 1):
            split_path = self.new_folder + '\\' + 'sounds-' + str(a) + '.' + self.format
            new_split_path = self.new_folder + '\\' + 'sounds-' + str(a) + '.pcm'
            command_line_encoding = 'ffmpeg -y  -i ' + split_path + '  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ' + new_split_path + '\n'
            print(command_line_encoding)
            a +=1
            with open(self.file_path, 'a') as f:
                f.write(command_line_encoding)
    def detect(self, path, times=16):
        os.chdir(path)
        i = 1
        while i <= (times+1):
            for file in os.listdir('.'):
                name,extension = os.path.splitext(file)
                if extension == ".pcm":
                    i += 1
                    text = self.get_token(file)
                    with open(self.txt, 'a') as f:
                        f.write(text)
        print('OKOKOKOk')


    # def ecoding(self):
    #     os.chdir(self.new_folder)
    #     for file in os.listdir('.'):
    #         name,extension = os.path.splitext(file)
    #         if 'sounds' in name:
    #             self.split_path = self.new_folder + '\\' + file
    #             self.new_split_path = self.new_folder + '\\' + name + '.pcm'
    #             command_line_encoding = 'ffmpeg -y  -i ' + self.split_path + '  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ' + self.new_split_path + '\n'
    #             with open(self.file_path2, 'a') as f:
    #                 f.write(command_line_encoding)
       #查找音频的长度命令，结合ffmpg，需要有返回值
        #for 循环裁剪
        print('encoding is over')

        # new_path = path + '\\' + str(ttiimmee)
        # new_path_format = new_path + '\n'
        # path_txt  = r"C:\Users\Administrator\Desktop\path.txt"
        # with open(path_txt, 'a') as f:
        #     f.write(new_path_format)


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

if __name__ == "__main__":
    test = Single(r'D:\003_Data\Baidu_Yunpan\shuaiqidelige\lige', 'abc', 'mp4')
