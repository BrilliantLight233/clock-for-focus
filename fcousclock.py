import time

def focus_timer(minutes):
  seconds = minutes * 60
  while seconds:
    minutes, secs = divmod(seconds,60)
    timer = '{:02d}:{:02d}'.format(minutes, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1
  print("Time's up!")
