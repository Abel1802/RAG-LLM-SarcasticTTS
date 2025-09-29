import os
import glob

# 指定目录
folder = 'vits_rag'

# 遍历所有 .wav 文件
for filepath in glob.glob(os.path.join(folder, '*.wav')):
    filename = os.path.basename(filepath)
    if '#' in filename:
        new_filename = filename.replace('#', '_')
        new_filepath = os.path.join(folder, new_filename)
        os.rename(filepath, new_filepath)
        print(f'Renamed: {filename} → {new_filename}')
