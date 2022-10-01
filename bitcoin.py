from string import whitespace
from tempfile import tempdir
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import width
import requests
import json
import pandas as pd

#colors
col1="white"
col2="#333333"
col3="#000000"

window = Tk()
window.title(' ')
window.geometry('320x350')
window.configure(bg=col1)

#data = pd.DataFrame((r.json())[['time_stamp','value']])

def info():
    api_link='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,INR,CAD'
    r=requests.get(api_link)
    dic=r.json()

    

    #USD
    usd_value=float(dic["USD"])
    #print(usd_value)
    usd_formatted_value="{:,.3f}".format(usd_value)
    usd["text"]="USA : $ "+usd_formatted_value

    #Euros
    euro_value=float(dic["EUR"])
    euro_formatted_value="{:,.3f}".format(euro_value)
    euros["text"]="Europe : € "+euro_formatted_value

    #CAD
    cad_value=float(dic["CAD"])
    cad_formatted_value="{:,.3f}".format(cad_value)
    cad["text"]="Canada : CAD "+cad_formatted_value

    #INR
    inr_value=float(dic["INR"])
    inr_formatted_value="{:,.3f}".format(inr_value)
    inr["text"]="India : INR "+inr_formatted_value

    #result=usd_formatted_value

    #tempDf = pd.DataFrame(result[['time_stamp','value']])
    #data.append(tempDf, ignore_index=False)
    #tempDf.head()
    time=0
    print(++time,"s :",usd_value)
    time=time+1
    frame_body.after(1000,info)



frame_head = Frame(window, width=320, height=100, bg=col1)
frame_head.grid(row=1, column=0)

frame_body = Frame(window, width=320, height=300, bg=col2)
frame_body.grid(row=2, column=0)

name=Label(frame_head, padx=0, text="Bitcoin Price Tracker",bg=col1, fg= col3, width=16, height=1, anchor="center", font=('Poppins 18'))
name.place(x=50,y=11)

usd=Label(frame_body, text="$0000", width=14, height=1, font=('Arial 10 bold'), bg=col2, fg=col1)
usd.place(x=10,y=30)

euros=Label(frame_body, text="$0000", width=14, height=1, font=('Arial 10 bold'), bg=col2, fg=col1)
euros.place(x=20,y=60)

cad=Label(frame_body, text="$0000", width=14, height=1, font=('Arial 10 bold'), bg=col2, fg=col1)
cad.place(x=20,y=90)

inr=Label(frame_body, text="$0000", width=14, height=1, font=('Arial 10 bold'), bg=col2, fg=col1)
inr.place(x=20,y=120)

info()

window.mainloop()