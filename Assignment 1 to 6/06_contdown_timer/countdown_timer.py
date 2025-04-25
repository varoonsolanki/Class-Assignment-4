import time

def countdown(minutes, seconds):
    total_seconds = minutes * 60 + seconds

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print("⏳ Time left:", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up!")

# User input
try:
    mins = int(input("Kitne minutes ka timer chahiye? "))
    secs = int(input("Kitne seconds? "))
    countdown(mins, secs)
except ValueError:
    print("⚠️ Sirf numbers daalo, please.")