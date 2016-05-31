import csv
from mutagen.flac import FLAC # calls the necessary mutagen library ID3 tags

csvfile = open('test3.csv') # opens your CSV file, change to whatever yours is named

reader = csv.reader(csvfile)
    
next(reader) # skip header
    
for trackno, songFile, songTitle, album, artist, year, genre, rights in reader: # the columns in your csv
    audio = FLAC(songFile)
    audio["title"] = songTitle
    audio["album"] = album
    audio["artist"] = artist
    audio["tracknumber"] = trackno
    audio["copyright"] = rights
    audio["date"] = year
    audio["genre"] = genre
    audio.save()
