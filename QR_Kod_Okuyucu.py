import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode


def qr_kod_olustur():
    url = url_girdi.get() 

    if url:
        qr_url = pyqrcode.create(url) 
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG DOSYALARI","*.svg")]) 

        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8)
            durum_etiketi.config(text="QR Kodu oluşturuldu ve kaydedildi")



#tkinder tasarım 

uygulama_penceresi = tk.Tk()
uygulama_penceresi.title("QR Kodu Oluşturucu")

etiket = tk.Label(uygulama_penceresi,text="URL'yi girin")
url_girdi = tk.Entry(uygulama_penceresi,width=40)
qr_kod_olustur_butonu = tk.Button(uygulama_penceresi,text="QR Kodu Oluştur",command=qr_kod_olustur)
durum_etiketi = tk.Label(uygulama_penceresi,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10) 

qr_kod_olustur_butonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

uygulama_penceresi.mainloop()