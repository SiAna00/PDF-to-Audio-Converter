from playsound import playsound
import PyPDF2
import requests
from s_keys import API_KEY

TTS_ENDPOINT = "http://api.voicerss.org/"

reader = PyPDF2.PdfReader("one_morning.pdf")
text = reader.pages[0].extract_text()

response = requests.get(f"{TTS_ENDPOINT}?key={API_KEY}&hl=en-us&v=Amy&c=MP3&src={text}")
response.raise_for_status()

with open("audio_file.mp3", "wb") as file:
    file.write(response.content)

playsound("audio_file.mp3")
