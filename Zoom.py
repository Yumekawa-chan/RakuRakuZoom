import pyautogui as pg
import time
import datetime as dt
import pause
import webbrowser as wb
import os
import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import ttk
from timetable import *

#時間とか
dt_now = dt.datetime.now()
now = str(dt_now.hour)+ ":" + str(dt_now.minute) #00:00
hour = dt_now.hour #時
minute = dt_now.minute #分
year = dt_now.year #年
month = dt_now.month #月
day = dt_now.day #日
date = dt.date(year, month, day).strftime('%a')

#曜日時限とアドレスの紐づけ
def adress_linking(n):
    if n == "月1":
        return mon[0]
    elif n == "月2":
        return mon[1]
    elif n == "月3":
        return mon[2]
    elif n == "月4":
        return mon[3]
    elif n == "火1":
        return tue[0]
    elif n == "火2":
        return tue[1]
    elif n == "火3":
        return tue[2]
    elif n == "火4":
        return tue[3]
    elif n == "水1":
        return wed[0]
    elif n == "水2":
        return wed[1]
    elif n == "水3":
        return wed[2]
    elif n == "水4":
        return wed[3]
    elif n == "木1":
        return thu[0]
    elif n == "木2":
        return thu[1]
    elif n == "木3":
        return thu[2]
    elif n == "木4":
        return thu[3]
    elif n == "金1":
        return fri[0]
    elif n == "金2":
        return fri[1]
    elif n == "金3":
        return fri[2]
    elif n == "金4":
        return fri[3] 
    else:
        tkm.showerror('エラー', '正しく入力して下さい。')

#画面録画
def start_capture():
    pg.hotkey("win","alt","r")

def end_capture():
    pg.hotkey("win","alt","r")

# 自動入室予約
def auto_inout(start_time,end_time,subject):
    if start_time[0] == start_time[2] == "0":
        pause.until(dt.datetime(year,month, day,int(start_time[1]),int(start_time[3])))
    elif start_time[0] == "0":
        pause.until(dt.datetime(year,month, day,int(start_time[1]),int(start_time[2:])))
    elif start_time[2] == "0":
        pause.until(dt.datetime(year,month, day,int(start_time[0:2]),int(start_time[3])))
    else:
        pause.until(dt.datetime(year,month, day,int(start_time[0:2]),int(start_time[2:])))
    
    wb.open(adress_linking(subject))
    time.sleep(5)
    
    
    pg.hotkey("alt","f") 
    
    if var.get() == 1:
        time.sleep(5)
        start_capture()

    if end_time[0] == end_time[2] == "0":
        pause.until(dt.datetime(year,month, day,int(end_time[1]),int(end_time[3])))
    elif end_time[0] == "0":
        pause.until(dt.datetime(year,month, day,int(end_time[1]),int(end_time[2:])))
    elif end_time[2] == "0":
        pause.until(dt.datetime(year,month, day,int(end_time[0:2]),int(end_time[3])))
    else:
        pause.until(dt.datetime(year,month, day,int(end_time[0:2]),int(end_time[2:])))
    
    if var.get() == 1:
        end_capture()

    exit_zoom()

# 自動予約
def appointment():
    subject = txt2.get()
    start_time = txt3.get()
    end_time = txt4.get()

    if subject == "" or start_time == "" or end_time == "":
        tkm.showerror('エラー', '正しく入力して下さい。')
    else:
        tkm.showinfo('予約完了', '時間までお待ちください')
        txt2.delete(0, tk.END)
        txt3.delete(0, tk.END)
        txt4.delete(0, tk.END)
        auto_inout(start_time,end_time,subject)

#zoomから退出
def exit_zoom(): #zoomから退出
    time.sleep(2)
    pg.hotkey('alt', 'q')
    time.sleep(4)
    pg.press('enter')

### 以下はレイアウト ###
root = tk.Tk()
root.title('楽々Zoom')
iconfile = 'raku.ico'
root.iconbitmap(default=iconfile)
root.geometry("600x300")

#ラベル
label1 = tk.Label(
    root, 
    font = ("MSゴシック", 16), 
    text = "手動で入室（月曜1限:月1と入力）" ,
    relief="ridge"
)
label1.place(
    x = 10, 
    y = 10, 
)
label2 = tk.Label(
    root, 
    font = ("MSゴシック", 16), 
    text = "自動入室（16時5分:1605と入力）" ,
    relief="ridge"
)
label2.place(
    x = 10, 
    y = 95, 
)

label3 = tk.Label(
    root, 
    font = ("System", 16), 
    text = "曜日・時限" 
)
label3.place(
    x = 10, 
    y = 130, 
)
label4 = tk.Label(
    root, 
    font = ("System", 16), 
    text = "入室時間" 
)
label4.place(
    x = 10, 
    y = 160, 
)
label5 = tk.Label(
    root, 
    font = ("System", 16), 
    text = "退出時間" 
)
label5.place(
    x = 10, 
    y = 190, 
)

# テキストボックス
txt1 = tk.Entry(width=20)
txt1.place(x=20, y=50)

txt2 = tk.Entry(width=20)
txt2.place(x=130, y=135)

txt3 = tk.Entry(width=20)
txt3.place(x=130, y=165)

txt4 = tk.Entry(width=20)
txt4.place(x=130, y=195)


#テキストボックスの処理
def btn_click():
    n = txt1.get()
    wb.open(adress_linking(n))

    if var.get() == 1:
        time.sleep(5)
        start_capture()

    txt1.delete(0, tk.END)

btn1 = tk.Button(root,
                text='入室する',
                command = btn_click
)
btn1.place(x=160, y=48)

btn2 = tk.Button(root,
                text='入室予約する',
                command = appointment
)
btn2.place(x=280, y=165)

#Webclass
def webclass():
    wb.open("https://els.sa.dendai.ac.jp/webclass/login.php")

btn3 = tk.Button(root,
                text='WebClass',
                command = webclass
)
btn3.place(x=10, y=250)

#Unipa
def unipa():
    wb.open("https://portal.sa.dendai.ac.jp/uprx/")

btn4 = tk.Button(root,
                text='Unipa',
                command = unipa
)
btn4.place(x=90, y=250)

var = tk.IntVar()
chk = tk.Checkbutton(root, text='授業画面を録画する', 
                    variable=var,
                    relief="ridge"
                    ) #チェックボックスでonなら1 offは0
chk.place(x=450, y=80)

### ここまでレイアウト ###


# ウィンドウの表示開始
root.mainloop()
