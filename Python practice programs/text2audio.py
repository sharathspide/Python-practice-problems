from gtts import gTTS
mytext = "Po da eruma saani kiruku payale.... en friend oru pombalaporuki"
language = "ta"
myobj = gTTS(text = mytext,lang=language,slow=True)
myobj.save("tease.mp3")
'''filename = "C:/Users/rasha/Desktop/youtube/anime review video scripts/death note.txt"
try:
    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()
        print ("read")
        language = 'en'
        myobj = gTTS(text=content, lang=language, slow=False)
        myobj.save("deathNoteReview.mp3")
        print("done")
        #print(content)
except FileNotFoundError:
    print("File not found or path is incorrect.")
except UnicodeDecodeError:
    print("Error: Unable to decode the file using the specified encoding.")
except IOError:
    print("An error occurred while reading the file.")'''
