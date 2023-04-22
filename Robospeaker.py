import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Abhi: ")

    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak : ")

        if x == "q":
            engine.say("Bye Bye Friends:")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
