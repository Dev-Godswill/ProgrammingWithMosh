# Car Game (Building the Engine for the game)
user_input = "" #This is an emptry string, so user can input whatever they need to 
started = False

# I need to write the loop for this game
while True:
  user_input = input(">> ").lower() # If user types ALL CAPS this would convert to lowercase
  if user_input == "start": # always put a semi-colon after the end
    if started:
      print ("Car has already started!")
    else:
      started = True
      print ("Thank You, Car Started.... Ready to Go")
  elif user_input == "stop":
    if not started:
      print ("Car has already stopped")
    else:
      started = False
      print ("Car stopped")
  elif user_input == "help":
    print (" start - to start the car\n stop - to stop the car\n quit - to exit")
  else:
    print ("Sorry, I don't understand this")

