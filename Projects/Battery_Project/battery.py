import time
import psutil
from playsound import playsound

def main():
    # Set the flag to False initially
    plugged_in_sound_played = False
    unplugged_sound_played = False

    # Continuously check the battery status
    while True:
        # Get the current battery status
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent

        # If the battery is being plugged in and is not already 100% charged
        if plugged and percent < 100 and not plugged_in_sound_played:
            # Play the "plugged in" sound
            playsound("Battery_Project\Mu1.mp3")
            # Set the flag to True
            plugged_in_sound_played = True
            unplugged_sound_played = False

        # If the battery is being unplugged and is not already 0% charged
        if not plugged and percent > 0 and not unplugged_sound_played:
            # Play the "unplugged" sound
            playsound("Battery_Project\Mu2.mp3")
            # Set the flag to True
            unplugged_sound_played = True
            plugged_in_sound_played = False

        # If the battery is not being plugged in or unplugged
        if not plugged and not plugged_in_sound_played:
            # Reset the flags to False
            plugged_in_sound_played = False
            unplugged_sound_played = True

        # Wait for a short period of time before checking again
        time.sleep(1)

if __name__ == "__main__":
    main()
