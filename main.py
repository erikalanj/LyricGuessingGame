import tkinter as tk
import json
import random


def load_lyrics(file="lyrics.json"):
    with open(file, "r") as f:
        return json.load(f)


def get_random_lyrics(lyrics):
    return random.choice(lyrics)


def submit_guess():
    # check user input
    user_guess = missing_word_entry.get()
    print(f"User generated: {user_guess}")


root = tk.Tk()
root.title("Lyric Guessing Game")

# display lyric
tk.Label(root, text="Is this the real life? Is this just ____?").pack()

# input for missing word
missing_word_entry = tk.Entry(root)
missing_word_entry.pack()

# band selection
band_var = tk.StringVar(value="Select Band")
band_menu = tk.OptionMenu(root, band_var, "Queen", "Guns n Roses", "Nirvana")

# submit button
tk.Button(root, text="Submit", command=submit_guess).pack()

root.mainloop()
