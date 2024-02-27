from playsound import playsound
import PyPDF2
import requests
from s_keys import API_KEY
from tkinter import *
from tkinter import filedialog

TTS_ENDPOINT = "http://api.voicerss.org/"


root = Tk()
root.config(padx=60, pady=60, background="gray24")
root.title("PDF to Audio Converter")


def select_pdf():
    global text
    global status_label
    global convert_button

    filename = filedialog.askopenfilename(initialdir="/mnt/c/Users/asimi/Desktop", title="Select PDF", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))

    reader = PyPDF2.PdfReader(filename)
    text = reader.pages[0].extract_text()

    status_label.config(text="PDF successfully selected.", fg="green2")
    convert_button.config(background="dodger blue", foreground="white smoke")


def convert_pdf():
    global status_label

    response = requests.get(f"{TTS_ENDPOINT}?key={API_KEY}&hl=en-us&v=Amy&c=MP3&src={text}")
    response.raise_for_status()

    with open("audio_file.mp3", "wb") as file:
        file.write(response.content)

    status_label.config(text="PDF successfully converted to audio.", fg="green2")


header_label = Label(root, text="Welcome to PDF to Audio Converter", font="Helvetica, 24", background="gray24", foreground="white smoke")
header_label.grid(column=0, row=0, columnspan=3, pady=(0, 20))

status_label = Label(root, text="Choose PDF to convert to audio", font="Helvetica, 12", background="gray24", foreground="white smoke")
status_label.grid(column=0, row=1, columnspan=3, pady=20)

select_button = Button(root, text="Select PDF", command=select_pdf, font="Helvetica, 12", background="dodger blue", foreground="white smoke")
select_button["border"] = "1"
select_button.grid(column=1, row=2, padx=10, pady=10, ipadx=5, ipady=5)

convert_button = Button(root, text="Convert", command=convert_pdf, font="Helvetica, 12")
convert_button.grid(column=1, row=3, padx=10, pady=10, ipadx=15, ipady=5)


root.mainloop()
