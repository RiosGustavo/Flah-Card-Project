from tkinter import *
import pandas
from tkinter import messagebox # importamos las cajitas de mensasjes

import random
import pyperclip
from pandas.core.interchange import dataframe

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = None

try:
   data =pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/English_words.csv")

finally:
    #print(data)
    data_list = data.to_dict(orient="records")
    #print(data_list)

current_card= random.choice(data_list)
#print(current_card["Ingles"])
#print(current_card["Español"])


def word():
    global timer
    global current_card
    if timer is not None:
        ventana.after_cancel(timer)
    current_card = random.choice(data_list)
    palabra = current_card["Ingles"]
    canvas.itemconfig(card_title, text="English", fill = "black")
    canvas.itemconfig(card_word, text=palabra, fill = "black")
    canvas.itemconfig(nueva_imagen, image=card_front)
    timer = ventana.after(3000, flip_cards)




def flip_cards():


    palabra = current_card["Español"]
    canvas.itemconfig(card_title, text="Español", fill = "white")
    canvas.itemconfig(card_word, text=palabra, fill = "white")
    canvas.itemconfig(nueva_imagen, image=card_back)


def es_conocida():

        global current_card
        data_list.remove(current_card)
        new_data = pandas.DataFrame(data_list)
        new_data.to_csv("data/words_to_learn.csv", index=False)

        word()


# ---------------------------- UI SETUP ------------------------------- #
ventana = Tk()
ventana.title("Card App Capstone")
ventana.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#lienzo


canvas = Canvas(ventana, width=800, height=526)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
nueva_imagen = canvas.create_image(400, 263, image=card_front)

#para cambiar la imagen
#canvas.itemconfig(nueva_imagen, image=card_back)

#canvas.create_image(400, 263, image = card_front )
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 2)


right_image = PhotoImage(file="images/right.png")
boton_right = Button(ventana, image=right_image, highlightthickness=0,bg=BACKGROUND_COLOR, bd=0, command=es_conocida)
boton_right.grid(row = 1, column = 1)



wrong_image = PhotoImage(file="images/wrong.png")
boton_wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=word)
boton_wrong.grid(row = 1, column = 0)



word()


ventana.mainloop()