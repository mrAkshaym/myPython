import winsound
import random 

def try_beep():
    try:
        winsound.Beep(440, 1000)
    except RuntimeError:
        print("Beep not available on this platform")


def try_play_recording():
    try:
        choice:int = random.randint(1, 3)
        print("choice is", choice)
        if choice == 1:
            winsound.PlaySound('sound_files\mixkit-dog-barking-twice-1.wav', winsound.SND_FILENAME)
        elif choice == 2:
            winsound.PlaySound('sound_files\mixkit-little-birds-singing-in-the-trees-17.wav', winsound.SND_FILENAME)
        elif choice == 3:
            winsound.PlaySound('sound_files\mixkit-trumpet-fanfare-2293.wav', winsound.SND_FILENAME)
        print("Played sound")
    except RuntimeError:
        print("PlaySound not available on this platform")


if __name__ == "__main__":
    try_play_recording()