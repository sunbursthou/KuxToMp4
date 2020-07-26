import os
import subprocess

cur_path = input('请输入文件源路径')
target_path = input('请输入目标路径')
youku_path = input('请输入优酷ffmpeg.exe路径')
youku_path += "\\" + "ffmpeg.exe"
file_list = os.listdir(cur_path)

for i in file_list:
    split_file_name = i.split('.')
    command1 = "\"" + youku_path + "\"" + " -y -i " + "\"" + cur_path + "\\" + split_file_name[
        0] + ".kux" + "\"" + " -c:v copy -c:a copy -threads 2 " + "\"" + target_path + "\\" + split_file_name[
            0] + ".mp4" + "\""
    print('读取文件……')
    subprocess.Popen(command1, shell=True)
print('读取完成，开始转换……')
