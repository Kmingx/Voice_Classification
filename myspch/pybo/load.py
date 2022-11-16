from tensorflow import keras
from django.apps import AppConfig
import os

from tensorflow import keras
import librosa
import scipy.io.wavfile
import numpy as np
import subprocess


class LoadConfig(AppConfig):
    model = keras.models.load_model("C:/src/model/model.h5")

    def new_file():
        files_Path = "C:/Users/user/Downloads/"  # 파일들이 들어있는 폴더
        file_name_and_time_lst = []
        # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌.
        for f_name in os.listdir(f"{files_Path}"):
            written_time = os.path.getctime(f"{files_Path}{f_name}")
            file_name_and_time_lst.append((f_name, written_time))
        # 생성시간 역순으로 정렬하고,
        sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
        # 가장 앞에 이는 놈을 넣어준다.
        recent_file = sorted_file_lst[0]
        recent_file_name = recent_file[0]
        # 지정경로와 최신파일 명을 Path로 재정의한다.
        files_Path = files_Path + recent_file_name
        return files_Path, recent_file_name

    def ffmpeg(files_Path, recent_file_name):
        cmd = "ffmpeg -i {} -f wav -ab 192000 -vn C:/Users/user/Downloads/+{}".format(files_Path, recent_file_name)
        subprocess.run(cmd, shell=True)

    def audioFileLoad():
        files_Path, recent_file = LoadConfig.new_file()  # 최근 생성된 files_Path 수집
        print("최신파일 : ", files_Path)
        LoadConfig.ffmpeg(files_Path, recent_file)  # ffmpeg로 재인코딩
        files_Path, recent_file = LoadConfig.new_file()  # 인코딩된 files_Path 수집
        print("최신파일2 : ", files_Path)
        data, sr = librosa.load(files_Path, sr=16000)  # 파일 로드
        # mini = 81900
        # 해당 오디오를 처음부터 4초까지 사용
        audiofile = data[:34155]
        # mfcc알고리즘으로 해당 오디오 파일에 특징점을 추출
        mfcc_file = librosa.feature.mfcc(y=audiofile, sr=16000, n_mfcc=20)
        # 넘파이 배열로 형변환
        mfcc_np = np.array(mfcc_file, np.float32)
        # 모델에 input할수있는 데이터 형태로 reshape
        print(mfcc_np.shape)
        mfcc_file2 = mfcc_np.reshape((1, 20, 67, 1))
        return mfcc_file2

    def classification(value):
        value = np.argmax(value)
        if value == 0:
            peopleType = "아동"
        
        elif value == 1:
            peopleType = "일반남성"
        elif value == 2:
            peopleType = "일반여성"
        elif value == 3:
            peopleType = "노인남성"
        elif value == 4:
            peopleType = "노인여성"

        return value,peopleType

    def ready(self):
        pass