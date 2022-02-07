# 楽々Zoom
東京電機大学の学生用に作ったZoom講義への入室・退室を手助けするソフトウェアです。

## 必要な環境
・WindowsのPC

・Python3が導入されている

・以下のpipが導入されている（pipの導入方法はググってください）

pause,pyautogui

## 事前準備
timetable.pyを開いてコメントアウトの説明に沿ってZoomアドレスを挿入してください。

## 実行方法
Pythonが実行できるターミナル（cmd,Anaconda Prompt）で指定のフォルダーに移動して以下のように実行。

`python Zoom.py`

下の画像のようなGUIが開けばOK

![image](https://user-images.githubusercontent.com/82374688/137908166-596d211e-f8b3-47ee-ae3d-40bb8d71fabf.png)

## 機能紹介
・特に時間を指定せずに今すぐ入室したい場合は手動で入室に例に沿って入力してください。

・入室、退室を自動で行う場合はそれぞれの時間を入力して入室予約してください。

※予約してから退出するまではプログラム自体が停止しますが仕様です。
