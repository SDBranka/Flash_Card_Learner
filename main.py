import pandas
import tkinter
from tkinter import messagebox, simpledialog
import random


FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"
file_to_learn = None
current_card = {}


# ---------------------------- CSV INFORMATION ------------------------------- #
def build_lang_dict(file_to_learn):
    language_data = pandas.read_csv(f"data/{file_to_learn}.csv")
    language_dict = language_data.to_dict(orient="records")
    # print(f"language_dict: {language_dict}")
    return language_dict


# ---------------------------- CARD DISPLAY AND FLIP ------------------------------- #
def next_card():
    global current_card, flip_timer
    # cancel previously active timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(language_dict)
    except:
        card_canvas.itemconfig(language_text, text="No Further Cards Available",
                                fill="black"
        )
        card_canvas.itemconfig(word_text, text="",
                                fill="black"
        )
    else:
        # print(f"current_card: {current_card['Polish']}")
        topic = list(current_card.keys())[0]
        # print(topic)
        card_canvas.itemconfig(language_text, text=topic,
                                fill="black"
        )
        card_canvas.itemconfig(word_text, text=current_card[topic],
                                fill="black"
        )
        card_canvas.itemconfig(card_background, image=card_front_img)
        # start new timer
        flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    try:
        topic = list(current_card.keys())[1]
    except:
        pass
    else:
        card_canvas.itemconfig(language_text, text=topic, 
                                fill="white"
        )
        card_canvas.itemconfig(word_text, text=current_card[topic],
                                fill="white"
        )
        card_canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- CORRECT BUTTON PRESSED ------------------------------- #
def correct_button_clicked():
    try:
        language_dict.remove(current_card)
        # print(f"len(language_dictionary): {len(language_dict)}")
        # print(f"language_dictionary: {language_dict}")
        words_to_learn_data = pandas.DataFrame(language_dict)
        # index=False so that index numbers are not stored to csv
        words_to_learn_data.to_csv("data/still_to_learn.csv", index=False)
    except ValueError:
        messagebox.showerror('error', 'No more cards available.\nPlease load a new topic.')
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# build window
window = tkinter.Tk()
window.title("Flash Cards")
# add padding between window frame and elements and set bg color
window.config(padx=54, pady=54,
                bg=BACKGROUND_COLOR,
)
flip_timer = window.after(ms=3000, func=flip_card)

# card front
card_canvas = tkinter.Canvas(width=800,
                                    height=526,
                                    bg=BACKGROUND_COLOR,
                                    highlightthickness=0
)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_background = card_canvas.create_image(400, 263, 
                                image=card_front_img
)
language_text = card_canvas.create_text(400, 150, 
                                text="", 
                                fill="black", 
                                font=(FONT_NAME, 40, "italic")
)
word_text = card_canvas.create_text(400, 263, 
                                    text="", 
                                    fill="black", 
                                    font=(FONT_NAME, 60, "bold")
)
card_canvas.grid(row=0, column=0, columnspan=2)

# wrong button
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img,
                                highlightthickness=0,
                                command=next_card
)
wrong_button.grid(row=1, column=0)

# correct button
correct_img = tkinter.PhotoImage(file="images/right.png")
correct_button = tkinter.Button(image=correct_img,
                                highlightthickness=0,
                                command=correct_button_clicked
)
correct_button.grid(row=1, column=1)


# ---------------------------- Program Cycle ------------------------------- #
# ask the user to enter the name of the file to be opened
# continue to ask until the user enters a file
while file_to_learn == None:
    file_to_learn = simpledialog.askstring("input string", "please enter a vaild file name")
    # print(f"file_to_learn: {file_to_learn}")
    
    # backdoor for testing
    if file_to_learn == "a":
        break    
    
    try:
        language_dict = build_lang_dict(file_to_learn)
    except:
        file_to_learn = None

# once a valid file has been selected begin play
next_card()



window.mainloop()