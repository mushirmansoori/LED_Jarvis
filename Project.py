# importing libraries
import pyfirmata
import time
import pyttsx3
import speech_recognition

board = pyfirmata.Arduino('COM3')
# text to speech
engine = pyttsx3.init()
def speak(something_say):
    engine.say(something_say)
    engine.runAndWait()

# Speaking capability
recogniser = speech_recognition.Recognizer()
mic_voice = speech_recognition.Microphone()

mic_voice = speech_recognition.Microphone(device_index=1)
# welcome and ask for something
speak("Welcome to Mushir arduino project, What do I do?")

def Ass():
    try:
        with mic_voice as source:
            print("Listening...")
            audio = recogniser.listen(mic_voice, phrase_time_limit=8)
        print("Processing...")
        text_out_of_audio = recogniser.recognize_google(audio, language="en-IN")
        # print("You said", text_out_of_audio)
        if (("green" in text_out_of_audio and "on" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
            print("Turning on green LED")
            speak("Turning on green LED")
            board.digital[9].write(1)
            time.sleep(2)
        else:
            if (("board" in text_out_of_audio and "on" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                print("Turning on board LED")
                speak("Turning on board LED")
                board.digital[13].write(1)
                time.sleep(2)
            else:
                if (("green" in text_out_of_audio and "off" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                    print("Turning off green LED")
                    speak("Turning off green LED")
                    board.digital[9].write(0)
                    time.sleep(2)
                else:
                    if (("board" in text_out_of_audio and "off" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                        speak("Turning off board LED")
                        print("Turning off board LED")
                        board.digital[13].write(0)
                        time.sleep(2)
                    else:
                        if (("red" in text_out_of_audio and "on" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                            speak("Turning on red LED")
                            print("Turning on red LED")
                            board.digital[10].write(1)
                            time.sleep(2)
                        else:
                            if (("all" in text_out_of_audio and "on" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                                speak("Turning all lights on")
                                print("Turning all lights on")
                                board.digital[10].write(1)
                                board.digital[9].write(1)
                                board.digital[13].write(1)
                                time.sleep(2)
                            else:
                                if (("all" in text_out_of_audio and "off" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                                    speak("Turning all lights off")
                                    print("Turning all lights off")
                                    board.digital[10].write(0)
                                    board.digital[9].write(0)
                                    board.digital[13].write(0)
                                    time.sleep(2)
                                else:
                                    if (("red" in text_out_of_audio and "off" in text_out_of_audio) and ("LED" in text_out_of_audio or "lights" in text_out_of_audio or "light" in text_out_of_audio)):
                                        speak("Turning off red LED")
                                        print("Turning off red LED")
                                        board.digital[10].write(0)
                                        time.sleep(2)
                                    else:
                                        speak("I didn't get it, Please say again sir")
                                        print("I didn't get it, Please say again sir")



    except Exception as e:
        print("An error occurred")

if __name__ == "__main__":
    while True:
        Ass()
