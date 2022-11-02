# pip install speech_recognition
import speech_recognition

from tkinter import *

# IN CASE OF "PYAUDIO" ERROR, USE BELOW COMMANDS
# pip install pipwin 
# pipwin install pyaudio

# speech_recognition setup
bot = speech_recognition.Recognizer()

# for opening a window
window = Tk()
window.title("Your Text here")
window.resizable(False, False) 

isListening = True

# funtion to add text to .txt file
def addTextToFile(text):
    file_object = open('text_file.txt', 'a')
        file_object.write(text)
    file_object.close()

# funtion to listen and write text in terminal
def listenToUser():
    global isListening
    while isListening:
        with speech_recognition.Microphone() as source:
            print("Listening...")
            audioCapture = bot.listen(source)

            try:
                print("Recognizing...")
                recognizedText = bot.recognize_google(audioCapture)

                addTextToFile(recognizedText + "\n")
                print(recognizedText)

            except:
                print("Say that again!")

            if 'close' in recognizedText:
                print("bye")            
                sys.exit()     
# Tkinter main page
mainFrame = Frame(window, bg='#D4D4D3')
mainFrame.grid(columnspan=5, ipadx=270, ipady=110, padx=10, pady=10)

# Welcome text
welcomeText = Label(mainFrame, text="Speech To Text!", font=('Courier', 20), bg='#D4D4D3')
welcomeText.place(relx=0.5, rely=0.35, anchor='center')

# Listen button
listenButton = Button(mainFrame, text='Listen', bg='#D4D4D3', height=2, width=10, command=lambda: listenToUser())
listenButton.place(relx=0.5, rely=0.65, anchor='center')

# To open the window
window.mainloop()
