import tkinter as tk

def hesapla():
    try:
        km=float(km_entry.get())
        litre=float(litre_entry.get())
        fiyat=float(fiyat_entry.get())
        tuketim=(litre/km)*100
        maliyet=litre*fiyat
        sonuc.config(text=f"Tüketim: {tuketim:.2f} L/100km\nYakıt Maliyeti: {maliyet:.2f} TL")
    except:
        sonuc.config(text="Lütfen geçerli değerler gir.")

p=tk.Tk()
p.title("Yakıt Hesaplayıcı")
p.geometry("360x260")

tk.Label(p,text="Gidilen Km").pack()
km_entry=tk.Entry(p)
km_entry.pack()

tk.Label(p,text="Harcanan Litre").pack()
litre_entry=tk.Entry(p)
litre_entry.pack()

tk.Label(p,text="Litre Fiyatı (TL)").pack()
fiyat_entry=tk.Entry(p)
fiyat_entry.pack()

tk.Button(p,text="Hesapla",command=hesapla).pack(pady=10)
sonuc=tk.Label(p,font=("Arial",12))
sonuc.pack()

p.mainloop()
