from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
word_learn = {}
data = {}
# ---------------------------- WORDS / TRANSLATIONS ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    data_dict = pd.DataFrame.to_dict(data, orient="records")


def next_word():
    global word_learn, flip_timer, data_dict
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=card_front)
    word_learn = random.choice(data_dict)
    word_learn_fr = word_learn["French"]
    canvas.itemconfig(language, text= "French", fill="black")
    canvas.itemconfig(word, text=f"{word_learn_fr}", fill="black")
    flip_timer = window.after(3000, show_translation)







def show_translation():
    global word_learn
    canvas.itemconfig(card, image=card_back)
    word_learn_en = word_learn["English"]
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{word_learn_en}", fill="white")




# ---------------------------- ERASE CORRECT WORDS ------------------------------- #

def correct_word():
    global data, word_learn, data_dict
    data_dict.remove(word_learn)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # bg is background

flip_timer = window.after(3000, show_translation)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)  # highlightthickness deletes the border
card_front = PhotoImage(file="images/card_front.png")  # To read my file in tkinter package
card = canvas.create_image(400, 265, image=card_front)
language = canvas.create_text(400, 165, text="", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 265, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

card_back = PhotoImage(file="images/card_back.png")

#Buttons

cross_img = PhotoImage(file="images/wrong.png")
cross = Button(image=cross_img, command=next_word, highlightthickness=0)
cross.grid(row=2, column=1)

tick_img = PhotoImage(file="images/right.png")
tick = Button(image=tick_img, command=correct_word, highlightthickness=0)
tick.grid(row=2, column=2)

next_word()



window.mainloop()
