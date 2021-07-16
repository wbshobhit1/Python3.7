from pygame import mixer

import time


def get_date():
    """""
    return its date and time
    """
    import datetime
    return datetime.datetime.now()


date = str(get_date())


def isoffc_time(current_time):
    """"
    returns true aur false
    according to our current time
    """
    if '09:00:00' < current_time < '17:00:00':
        return True
    else:
        print("This is not office hour , Your program will terminate in a minute")
        return False


def water_music():
    """
    return water music function
    here music.mp3 is a music file
    """
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(2.0)
    mixer.music.play()


def eyes_music():
    """
    return eyes excercise music function
    here music.mp3 is a music file
    """
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.set_volume(2.0)
    mixer.music.play()


def physical_excercise_music():
    """
    return physical excercise music function
    here music.mp3 is a music file
    """
    mixer.init()
    mixer.music.load("excercise.mp3")
    mixer.music.set_volume(2.0)

current_time = time.strftime("%H:%M:%S")
Water_taken_at_time = time.time()
Eyes_excercise_done_at_time = time.time()
Physical_excercise_done_at_time = time.time()

while isoffc_time(current_time):
    if Number_of_glasses_of_water_remaining > 0:
        if time.time() - Water_taken_at_time > Water_after_every:
            print("Time to drink Water\n")
            while True:
                water_music()
                if input("Enter Drank if drank a glass of water :").lower() == "drank":
                    Water_taken_at_time = time.time()
                    with open("water.txt", "a") as w:
                        w.write(f"Drank water at {date}")
                    Number_of_glasses_of_water_remaining -= 1
                    mixer.music.stop()
                    break

        if time.time() - Eyes_excercise_done_at_time > Eye_excercise_every:
            print("Time to  do Eyes excercise\n")
            while True:
                eyes_music()
                if input("Enter Eydone if you had completed the eye excercise:").lower() == "eydone":
                    with open("eyes.txt", "a") as ey:
                        ey.write(f"Eye excercise done at {date}")
                    mixer.music.stop()
                    break

        if time.time() - Physical_excercise_done_at_time > Physical_excercise_every:
            print("Time to  do Physical excercise\n")
            while True:
                physical_excercise_music()
                if input("Enter Exdone if you had completed physical excercise :").lower() == "exdone":
                    with open("eyes.txt", "a") as ex:
                        ex.write(f"Physical excercise done at {date}")
                    mixer.music.stop()
                    break

time.sleep(Sleep_time)
current_time = time.strftime("%H:%M:%S")