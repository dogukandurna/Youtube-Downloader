from cProfile import label
from cgitb import text
from msilib.schema import Font
from struct import pack
from textwrap import fill
import tkinter as tk
from turtle import bgcolor
from tkinter import ttk
from tkinter import PhotoImage
from pytube import YouTube 
import os

SAVE_PATH = "C:/Users/Doğukan Durna/Downloads"

def download():
    try:
        url=urlentryarea.get()
        selectedform=combolist.get()
        yt=YouTube(url)
        if combolist.current()==0:
            form.title("Downloading...")
            audio_stream = yt.streams.filter(only_audio=True).first()
            out_file = audio_stream.download(output_path=SAVE_PATH)
            base,ext=os.path.splitext(out_file)
            to_mp3=base + ".mp3"
            os.rename(out_file,to_mp3)
            form.title("Youtube Downloader by Dogukan Durna")
        else:
            form.title("Downloading...")
            mp4file = yt.streams.get_highest_resolution().download(SAVE_PATH)
            form.title("Youtube Downloader by Dogukan Durna")
    except:
        label2=tk.Label(form,text="Bağlantı Kurulamadı",font="Arial 22 bold",bg='#1b1e5a', fg="white")
        label2.place(x=165,y=275)

form=tk.Tk()
form.title("Youtube Downloader by Dogukan Durna")
form.iconbitmap('C:\\Users\\Doğukan Durna\\Desktop\\YAZILIM\\PYTHON\\Youtube Downloader\\Youtube.ico')
form.geometry('600x400')
form.configure(bg='#1b1e5a')
form.minsize(600,400)
form.maxsize(600,400)

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "white", background= "white")

label1=tk.Label(form,text="Youtube Downloader",font="Arial 22 bold",bg='#1b1e5a', fg="white")
label1.place(x=165,y=75)

urlentryarea=tk.Entry(form,text="Paste Url", font="Arial 14 bold", bg="White", fg="Black", width=27)
urlentryarea.place(x=165,y=130)

combolist=ttk.Combobox(form, width = 5, values = [' MP3', ' MP4'], font="Arial 14 bold", state="readonly")
combolist.place(x=270,y=180)
combolist.current(0)

downbutton=tk.Button(form,text="Download",bg="White",font=('Arial', 14), command=download)
downbutton.place(x=260,y=230)

form.mainloop()