from tkinter import *
from tkinter import Tk, messagebox
from tkinter import ttk
from PIL import ImageTk
import googletrans
import textblob

root = Tk()
root.title("PYtranslator")
root.geometry("900x400")
root.config(bg="black")
root.resizable(False, False)


def change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, change)


def trans():
    global language
    try:
        text_ = text1.get(1.0, END)
        c3 = combo1.get()
        c4 = combo2.get()
        if (text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i, j in language.items():
                if (j == c4):
                    lan_ = i
            words = words.translate(from_lang=lan, to=str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("PYtranslator", "Please try again later.")


image_icon = PhotoImage(file="data/logo.png")
root.iconphoto(False, image_icon)

arrow_image = ImageTk.PhotoImage(file="data/images1.png")
image_label = Label(root, image=arrow_image)
image_label.place(x=390, y=80)

title = Label(root, text="PYtranslator", font=("ALGERIAN", 40, "bold"), fg="green", bg="black").place(
    x=250, y=5)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="ALGERIAN", state="r")
combo1.place(x=110, y=70)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="Algerian", bg="white", width=25, bd=6, relief=GROOVE)
label1.place(x=80, y=110)

f1 = Frame(root, bg="green", bd=7, width=310, height=190)
f1.place(x=55, y=155)

text1 = Text(f1, bg="white", font="Constantia", width=32, height=9, relief=GROOVE, wrap=WORD)
text1.place(x=1, y=0)

combo2 = ttk.Combobox(root, values=languageV, font="ALGERIAN", state="r")
combo2.place(x=600, y=70)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="Algerian", bg="white", width=25, bd=6, relief=GROOVE)
label2.place(x=570, y=110)

f2 = Frame(root, bg="red", bd=7, width=310, height=190)
f2.place(x=542, y=155)

text2 = Text(f2, bg="white", font="Constantia", width=32, height=9, relief=GROOVE, wrap=WORD)
text2.place(x=1, y=0)

button = Button(root, command=trans, cursor="hand2", text="TRANSLATE",
                font=("Copperplate Gothic Light", 13, "bold"),
                fg="red",
                bg="green").place(
    x=380, y=300)

change()
root.mainloop()
