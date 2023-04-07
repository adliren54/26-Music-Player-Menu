from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen 
  time.sleep(1)
  os.system("clear")
  
  # Show the menu
  print("🎵 MyPOD Music Player")

  print("Press 1 to Play")
  print("Press 2 to Exit")
  
  print("Press anything else to see the menu again.")
  
  # take user's input
  user_input = str(input("> "))
  
  
  # check whether you should call the play() subroutine depending on user's input
  if user_input == "1":
    play()
    continue
  elif user_input == "2":
    break
  else:
    continue