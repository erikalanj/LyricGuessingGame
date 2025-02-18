import tkinter as tk
import json
import random


# Load lyrics from a JSON file
def load_lyrics(file="lyrics.json"):
    with open(file, "r") as f:
        return json.load(f)


# Select a random lyric from the list
def select_random_lyric(lyrics):
    return random.choice(lyrics)


# Update the band dropdown with the correct band and two random incorrect bands
def update_band_menu(lyric):
    correct_band = lyric["band"]
    all_bands = {
        lyric_data["band"] for lyric_data in lyrics
    }  # Use a set for unique bands
    all_bands.remove(correct_band)
    all_bands = list(all_bands)  # Convert set to list for random sampling
    random_bands = random.sample(all_bands, 2)  # Get 2 random incorrect bands
    band_choices = random_bands + [correct_band]
    random.shuffle(band_choices)

    band_var.set("Select Band")
    band_menu["menu"].delete(0, "end")

    for band in band_choices:
        band_menu["menu"].add_command(
            label=band, command=lambda b=band: band_var.set(b)
        )


# Handle the submission of the guess
def submit_guess():
    user_guess = missing_word_entry.get().strip().lower()
    selected_band = band_var.get()
    correct_missing_word = current_lyric["missing_word"].lower()
    correct_band = current_lyric["band"]

    if user_guess == correct_missing_word and selected_band == correct_band:
        result_label.config(text="Nice! You got it right.", fg="green")
    else:
        result_label.config(
            text=f"Wrong! The correct word was '{correct_missing_word}' and the band was '{correct_band}'.",
            fg="red",
        )


# Initialize game
lyrics = load_lyrics()
current_lyric = select_random_lyric(lyrics)

# Initialize GUI
root = tk.Tk()
root.title("Lyric Guessing Game")

# Display lyric
lyric_label = tk.Label(root, text=current_lyric["lyric"])
lyric_label.pack()

# Input for missing word
missing_word_entry = tk.Entry(root)
missing_word_entry.pack()

# Band selection dropdown
band_var = tk.StringVar(value="Select Band")
band_menu = tk.OptionMenu(root, band_var, "Placeholder")  # Placeholder, will be updated
band_menu.pack()

# Update the band menu with random bands and the correct one
update_band_menu(current_lyric)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_guess)
submit_button.pack()

# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Start the game
root.mainloop()
