#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import tensorflow as tf
import os
import random
import main

# 学習結果(ckpt_path)のpath
CKPT_PATH = './model/kaomodel.ckpt'

# OpenCVのデフォルトの顔の分類器のpath
cascade_path = './settings/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascade_path)

# 識別ラベルと各ラベル番号に対応する名前
HUMAN_NAMES = {
  0: "kim",
  1: "phone"
}

#指定した画像(img_path)を学習結果(ckpt_path)(上記参照)を用いて判定する
def evaluation(img_path):
  ckpt_path = CKPT_PATH
  # GraphのReset(らしいが、何をしているのかよくわかっていない…)
  tf.reset_default_graph()
  # データを入れる配列
  image = []
  img = cv2.imread(img_path)
  img = cv2.resize(img, (28, 28))

  # 画像情報を一列にした後、0-1のfloat値にする
  image.append(img.flatten().astype(np.float32)/255.0)
  # numpy形式に変換し、TensorFlowで処理できるようにする
  image = np.asarray(image)
  # 入力画像に対して、各ラベルの確率を出力して返す(main.pyより呼び出し)
  logits = main.inference(image, 1.0)
  # We can just use 'c.eval()' without passing 'sess'
  sess = tf.InteractiveSession()
  # restore(パラメーター読み込み)の準備
  saver = tf.train.Saver()
  # 変数の初期化
  sess.run(tf.initialize_all_variables())
  if ckpt_path:
    # 学習後のパラメーターの読み込み
    saver.restore(sess, ckpt_path)
  # sess.run(logits)と同じ
  softmax = logits.eval()
  # 判定結果
  result = softmax[0]

  # 判定結果を%にして四捨五入
  rates = [round(n * 100.0, 1) for n in result]
  humans = []
  # ラベル番号、名前、パーセンテージのHashを作成
  for index, rate in enumerate(rates):
    name = HUMAN_NAMES[index]
    humans.append({
      'label': index,
      'name': name,
      'rate': rate
    })
  # パーセンテージの高い順にソート
  # 追記：コマンドラインを利用した、ハイパーパラメータ確認の際は、x['rate']をx['label']に変更する
  rank = sorted(humans, key=lambda x: x['rabel'], reverse=True)

  # 判定結果を返す
  return rank


# コマンドラインからのテスト用
if __name__ == '__main__':
    # それぞれハイパーパラメータテスト画像のフォルダパス。確認したい画像のパスを、file_path=の後に置く
    kim_path="./hyper-test-pics/kim/kim"
    tel_path="./hyper-test-pics/tel/tel"
    other_path="./hyper-test-pics/other/other"
    image_count = 100
    for i in range(image_count):
        # このfile_pathはローカルのパス
        file_path = (other_path + str(i) + '.jpg')
        result = evaluation(file_path)
        print(result)
