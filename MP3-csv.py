import csv
from mutagen.id3 import ID3, TRCK, TIT2, TALB, TPE1, TCOP, TYER, TCON # calls the necessary mutagen library ID3 tags

csvfile = open('test2.csv') # opens your CSV file, change to whatever yours is named

reader = csv.reader(csvfile)
    
next(reader) # skip header
    
for trackno, songFile, songTitle, album, artist, year, genre, rights in reader: # the columns in your csv
    audio = ID3(songFile, v2_version=3)
    audio.add(TRCK(encoding=3, text=trackno))
    audio.add(TIT2(encoding=3, text=songTitle))
    audio.add(TALB(encoding=3, text=album))
    audio.add(TPE1(encoding=3, text=artist))
    audio.add(TCOP(encoding=3, text=rights))
    audio.add(TYER(encoding=3, text=year))
    audio.add(TCON(encoding=3, text=genre))
    audio.save(v2_version=3)
