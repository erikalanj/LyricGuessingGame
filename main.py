import tkinter as tk
import json
import random


def load_lyrics(file="lyrics.json"):
    with open(file, "r") as f:
        return json.load(f)


def get_random_lyrics(lyrics):
    return random.choice(lyrics)


def update_band_menu():
    # create list of random bands
    all_bands = [
        lyric["band"] for lyric in lyrics if lyric["band"] != current_lyric["band"]
    ]
    # assign 2 of those incorrect, random bands
    random_bands = random.sample(all_bands, 2)
    band_choices = random_bands + [current_lyric["band"]]
    random.shuffle(band_choices)
    band_var.set("Select band")
    band_menu["menu"].delete(0, "end")
    for band in band_choices:
        band_menu["menu"].add_command(
            label=band, command=lambda b=band: band_var.set(b)
        )


def submit_guess():
    # check user input
    user_guess = missing_word_entry.get()
    user_band = band_var.get()
    # correct answers from current lyric
    correct_lyric = current_lyric["missing_lyric"]
    correct_band = current_lyric["band"]

    if user_guess.lower() == correct_lyric.lower() and user_band == correct_band:
        result_label.config(text="nice freaking job you're not a poser", fg="green")
    else:
        result_label.config(text="POSER!!!!!", fg="red")


update_band_menu()

lyrics = load_lyrics()
current_lyric = get_random_lyrics(lyrics)

root = tk.Tk()
root.title("Lyric Guessing Game")

# display lyric
lyric_label = tk.Label(root, text=current_lyric["lyric"]).pack()

# input for missing word
missing_word_entry = tk.Entry(root)
missing_word_entry.pack()

# band selection
band_var = tk.StringVar(value="Select Band")
band_menu = tk.OptionMenu(root, band_var, "Queen", "Guns n Roses", "Nirvana").pack()

# submit button
tk.Button(root, text="Submit", command=submit_guess).pack()

# result display
result_label = tk.Label(root, text="", font=("Helvetica", 12)).pack()

print("game should start")
root.mainloop()
