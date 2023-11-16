import speech_recognition as aud
import pyttsx3
import pywhatkit
import datetime
import wikipedia


machine = pyttsx3.init()
listener = aud.Recognizer()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with aud.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech).lower()
            if "victor" in instruction:
                instruction = instruction.replace('victor', '')
            return instruction
    except aud.WaitTimeoutError:
        return "timeout"
    except aud.UnknownValueError:
        return "unknown"
    except Exception as e:
        return str(e)

def play_victor():
    while True:
        instruction = input_instruction()
        print(instruction)

        if "play" in instruction:
            song = instruction.replace('play', '')
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk("Current time is " + current_time)
        elif 'date' in instruction:
            current_date = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + current_date)
        elif 'hello' in instruction:
            print("Hi, Edwin! What's up?")
            talk("Hi, Edwin! What's up?")
        elif 'who are you' in instruction:
            print("Hi, i am victor! What can i do for you?")
            talk("Hi, i am victor! What can i do for you?")
        elif 'how are you' in instruction:
            print("I'm fine. How about you?")
            talk("I'm fine. How about you?")
        elif 'who is' in instruction:
import speech_recognition as aud
import pyttsx3
import pywhatkit
import datetime
import wikipedia


machine = pyttsx3.init()
listener = aud.Recognizer()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with aud.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech).lower()
            if "victor" in instruction:
                instruction = instruction.replace('victor', '')
            return instruction
    except aud.WaitTimeoutError:
        return "timeout"
    except aud.UnknownValueError:
        return "unknown"
    except Exception as e:
        return str(e)

def play_victor():
    while True:
        instruction = input_instruction()
        print(instruction)

        if "play" in instruction:
            song = instruction.replace('play', '')
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk("Current time is " + current_time)
        elif 'date' in instruction:
            current_date = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + current_date)
        elif 'hello' in instruction:
            print("Hi, Edwin! What's up?")
            talk("Hi, Edwin! What's up?")
        elif 'who are you' in instruction:
            print("Hi, i am victor! What can i do for you?")
            talk("Hi, i am victor! What can i do for you?")
        elif 'how are you' in instruction:
            print("I'm fine. How about you?")
            talk("I'm fine. How about you?")
        elif 'who is' in instruction:
            person = instruction.replace('who is', '')
            try:
                info = wikipedia.summary(person, 1)
                talk(info)
                print(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                talk("I couldn't find any information about that person.")
        elif 'exit' in instruction:
            print("bye catch you later")
            talk("Goodbye!")
            break
        elif 'stop' in instruction:
            talk("Goodbye! I'm going to sleep")
            break
        else:
            talk("Please repeat your command.")

if __name__ == "__main__":
    play_victor()

