import tkinter as tk
import RPi.GPIO as GPIO
import time

# Define the GPIO pin where your LED is connected
led_pin = 17

# Define the Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' '
}

# Function to blink Morse code
def blink_morse_code(word):
    for letter in word:
        if letter == ' ':
            time.sleep(3)  # 3 units of time for word spacing
        else:
            morse = morse_code.get(letter.upper(), '')
            for symbol in morse:
                if symbol == '.':
                    GPIO.output(led_pin, GPIO.HIGH)
                    time.sleep(1)  # 1 unit of time for dot
                    GPIO.output(led_pin, GPIO.LOW)
                    time.sleep(1)  # 1 unit of time for space between dots and dashes
                elif symbol == '-':
                    GPIO.output(led_pin, GPIO.HIGH)
                    time.sleep(3)  # 3 units of time for dash
                    GPIO.output(led_pin, GPIO.LOW)
                    time.sleep(1)  # 1 unit of time for space between dots and dashes

# Function to handle button click event
def on_button_click():
    input_text = entry.get()[:12]  # Get the text from the entry field (max 12 characters)
    blink_morse_code(input_text)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Create the GUI window
window = tk.Tk()
window.title("Morse Code LED Blinker")

# Create an entry field for text input
entry = tk.Entry(window, width=20)
entry.pack(padx=10, pady=10)

# Create a button to trigger Morse code blinking
button = tk.Button(window, text="Blink Morse Code", command=on_button_click)
button.pack(pady=10)

# Start the GUI main loop
window.mainloop()

# Cleanup GPIO on program exit
GPIO.cleanup()
