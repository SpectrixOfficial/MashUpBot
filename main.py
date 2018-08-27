import pydub
from pydub import AudioSegment

print("Starting 1")
pydub.AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg"

song1 = AudioSegment.from_mp3("songs\hotline_bling.mp3")
song2 = AudioSegment.from_mp3("songs\hotline_bling.mp3")

print("Starting 2")

final = song1 + song2

print("Starting 3")

final.export("mashup.mp3", format="mp3", tags={'artist': 'Spectrix', 'album': 'MashUpBot', 'comments': 'https://github.com/SpectrixOfficial/MashUpBot'})
print("Done!")