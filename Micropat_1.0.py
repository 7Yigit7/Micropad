#Yazan Yiğit Çıtak
version = "1.0"

""""
Sürüm 1.0:
    İlk sürümdür

"""

import tkinter as tk
from tkinter import filedialog

renk = "black"

class buton_class:
    def __init__(self,
                y=0,
                x=0,
                text="",
                font_color="white",
                color="black"):
        self.x = x
        self.y = y
        self.text = text
        self.font_color = font_color
        self.color = color

buton1 = buton_class(
    x=1,
    y=1,
    text="Kaydet",
    font_color="white",
    color="black"
    )
buton2 = buton_class(
    x=1,
    y=50,
    text="Şifreli kaydet",
    font_color="cyan",
    color="black"
    )
buton3 = buton_class(
    x=1,
    y=200,
    text="Aç",
    font_color="white",
    color="black"
    )
buton4 = buton_class(
    x=1,
    y=250,
    text="Şifreli aç",
    font_color="cyan",
    color="black"
    )


def main():
    def but1():
        dosya_sec = tk.Tk()
        dosya_sec.withdraw()
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        try:
            with open(dosya_yolu, "w") as dosya:
                dosya.write(girdi.get("1.0","end-1c"))
        except:
            pass

    def but2():
        dosya_sec = tk.Tk()
        dosya_sec.withdraw()
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        try:
            sifreleniyor1 = girdi.get("1.0","end-1c").replace("q","y0032h210")
            sifreleniyor2 = sifreleniyor1.replace("w","y0031h210")
            sifreleniyor3 = sifreleniyor2.replace("e","y0030h210")
            sifreleniyor4 = sifreleniyor3.replace("r","y0029h210")
            sifreleniyor5 = sifreleniyor4.replace("t","y0028h210")
            sifreleniyor6 = sifreleniyor5.replace("y","y0027h210")
            sifreleniyor7 = sifreleniyor6.replace("u","y0026h210")
            sifreleniyor8 = sifreleniyor7.replace("ı","y0025h210")
            sifreleniyor9 = sifreleniyor8.replace("o","y0024h210")
            sifreleniyor10 = sifreleniyor9.replace("p","y0023h210")
            sifreleniyor11 = sifreleniyor10.replace("ğ","y0022h210")
            sifreleniyor12 = sifreleniyor11.replace("ü","y0021h210")
            sifreleniyor13 = sifreleniyor12.replace("a","y0020h210")
            sifreleniyor14 = sifreleniyor13.replace("s","y0019h210")
            sifreleniyor15 = sifreleniyor14.replace("d","y0018h210")
            sifreleniyor16 = sifreleniyor15.replace("f","y0017h210")
            sifreleniyor17 = sifreleniyor16.replace("g","y0016h210")
            sifreleniyor18 = sifreleniyor17.replace("h","y0015h210")
            sifreleniyor19 = sifreleniyor18.replace("j","y0014h210")
            sifreleniyor20 = sifreleniyor19.replace("k","y0013h210")
            sifreleniyor21 = sifreleniyor20.replace("l","y0012h210")
            sifreleniyor22 = sifreleniyor21.replace("ş","y0011h210")
            sifreleniyor23 = sifreleniyor22.replace("i","y0010h210")
            sifreleniyor24 = sifreleniyor23.replace("z","y0009h210")
            sifreleniyor25 = sifreleniyor24.replace("x","y0008h210")
            sifreleniyor26 = sifreleniyor25.replace("c","y0007h210")
            sifreleniyor27 = sifreleniyor26.replace("v","y0006h210")
            sifreleniyor28 = sifreleniyor27.replace("b","y0005h210")
            sifreleniyor29 = sifreleniyor28.replace("n","y0004h210")
            sifreleniyor30 = sifreleniyor29.replace("m","y0003h210")
            sifreleniyor31 = sifreleniyor30.replace("ö","y0002h210")
            sifrelendi = sifreleniyor31.replace("ç","y0001h210")

            with open(dosya_yolu, "w") as dosya:
                dosya.write(sifrelendi)
        except:
            pass


    def but3():
        dosya_sec = tk.Tk()
        dosya_sec.withdraw()

        dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])

        if dosya_yolu:

            with open(dosya_yolu, "r") as dosya:
                icerik = dosya.read()

            girdi.delete("1.0", tk.END)
            girdi.insert(tk.END, icerik)

    def but4():
            dosya_sec = tk.Tk()
            dosya_sec.withdraw()

            dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])

            if dosya_yolu:

                with open(dosya_yolu, "r") as dosya:
                    coz = dosya.read()
                cozuluyor1 = coz.replace("y0027y0015h2102100032y0015h210210","q")
                cozuluyor2 = cozuluyor1.replace("y0027y0015h2102100031y0015h210210","w")
                cozuluyor3 = cozuluyor2.replace("y0027y0015h2102100030y0015h210210","e")
                cozuluyor4 = cozuluyor3.replace("y0027y0015h2102100029y0015h210210","r")
                cozuluyor5 = cozuluyor4.replace("y0027y0015h2102100028y0015h210210","t")
                cozuluyor6 = cozuluyor5.replace("y0027y0015h210210","y")
                cozuluyor7 = cozuluyor6.replace("y0026y0015h210210","u")
                cozuluyor8 = cozuluyor7.replace("y0025y0015h210210","ı")
                cozuluyor9 = cozuluyor8.replace("y0024y0015h210210","o")
                cozuluyor10 = cozuluyor9.replace("y0023y0015h210210","p")
                cozuluyor11 = cozuluyor10.replace("y0022y0015h210210","ğ")
                cozuluyor12 = cozuluyor11.replace("y0021y0015h210210","ü")
                cozuluyor13 = cozuluyor12.replace("y0020y0015h210210","a")
                cozuluyor14 = cozuluyor13.replace("y0019y0015h210210","s")
                cozuluyor15 = cozuluyor14.replace("y0018y0015h210210","d")
                cozuluyor16 = cozuluyor15.replace("y0017y0015h210210","f")
                cozuluyor17 = cozuluyor16.replace("y0016y0015h210210","g")
                cozuluyor18 = cozuluyor17.replace("y0015h210","h")
                cozuluyor19 = cozuluyor18.replace("y0014h210","j")
                cozuluyor20 = cozuluyor19.replace("y0013h210","k")
                cozuluyor21 = cozuluyor20.replace("y0012h210","l")
                cozuluyor22 = cozuluyor21.replace("y0011h210","ş")
                cozuluyor23 = cozuluyor22.replace("y0010h210","i")
                cozuluyor24 = cozuluyor23.replace("y0009h210","z")
                cozuluyor25 = cozuluyor24.replace("y0008h210","x")
                cozuluyor26 = cozuluyor25.replace("y0007h210","c")
                cozuluyor27 = cozuluyor26.replace("y0006h210","v")
                cozuluyor28 = cozuluyor27.replace("y0005h210","b")
                cozuluyor29 = cozuluyor28.replace("y0004h210","n")
                cozuluyor30 = cozuluyor29.replace("y0003h210","m")
                cozuluyor31 = cozuluyor30.replace("y0002h210","ö")
                cozuldu = cozuluyor31.replace("y0001h210","ç")

                girdi.delete("1.0", tk.END)
                girdi.insert(tk.END, cozuldu)

    root = tk.Tk()
    root.minsize(1550,700)
    root.title("DefterYar")

    girdi=tk.Text(root,height=40,width=120,fg=renk)
    girdi.pack()

    save = tk.Button(root,#buton1
                     text=buton1.text,
                     command=but1,
                     fg=buton1.font_color,
                     bg=buton1.color
                     ).place(x=buton1.x,y=buton1.y)

    sifreli_kayit = tk.Button(root,#buton2
                              text=buton2.text,
                              command=but2,
                              fg=buton2.font_color,
                              bg=buton2.color
                              ).place(x=buton2.x,y=buton2.y)

    dosya_sec = tk.Button(root,#buton3
                     text=buton3.text,
                     command=but3,
                     fg=buton3.font_color,
                     bg=buton3.color
                     ).place(x=buton3.x,y=buton3.y)

    sifreli_sec = tk.Button(root,#buton4
                     text=buton4.text,
                     command=but4,
                     fg=buton4.font_color,
                     bg=buton4.color
                     ).place(x=buton4.x,y=buton4.y)

    title_y = buton4.y + 170
    title = tk.Label(root,
                     text="DefterYar",
                     font="italic 20",
                     fg="blue",
                     ).place(x=1,y=title_y)

    ver = tk.Label(root,
                   text=f"sürüm: {version}",
                   font="italic 10",
                   fg="blue",
                   ).place(x=10,y=title_y + 50)

    root.mainloop()


if __name__ == "__main__":
    main()
