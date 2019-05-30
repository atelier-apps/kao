# -*- coding:utf-8 -*-

import cv2
import numpy as np

# 先ほど集めてきた画像データのあるディレクトリ
input_data_path = './downloads/kim/kim'
# 切り抜いた画像の保存先ディレクトリ(予めディレクトリを作っておいてください)
save_path = './cutted_kim_images/'
# OpenCVのデフォルトの分類器のpath。(https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xmlのファイルを使う)
cascade_path = 'C:\\Users\\sawad\\Anaconda3\\envs\\tensorflow-cpu\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascade_path)

# 収集した画像の枚数(任意で変更)
image_count = 324
# 顔検知に成功した数(デフォルトで0を指定)
face_detect_count = 0

# 集めた画像データから顔が検知されたら、切り取り、保存する。
for i in range(image_count):
  img = cv2.imread(input_data_path + str(i) + '.jpg', cv2.IMREAD_COLOR)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  print(i)
  face = faceCascade.detectMultiScale(gray, 1.1, 3)
  if len(face) > 0:
    for rect in face:
      # 顔認識部分を赤線で囲み保存(今はこの部分は必要ない)
      # cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=1)
      # cv2.imwrite('detected.jpg', img)
      x = rect[0]-30;
      y = rect[1]-60;
      w = rect[2]+60;
      h = rect[3]+100;
      cv2.imwrite(save_path + 'cutted_kim' + str(face_detect_count) + '.jpg', img[y:y+h, x:x+w])
      face_detect_count = face_detect_count + 1
#  else:
#    print 'image'+str(i)+':NoFace'
