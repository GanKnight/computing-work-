While true:
  print("Scallywag the Pirate")
  print("")
  print("")
  name = input("What is your name?")
  print("Hello " + name + "!")
  print("My name is Scallywag the pirate!")
  counter = 0
  while counter == 0:
    description = input("How do you feel right now, matey?")
    list_of_words = description.split()
    for each_word in list_of_words:
      if each_word == "sad" and counter == 0:
        print("Back in my day, if an 'ol seadog was sad, we'll drink to the gods!")
        print("Tomorrow will be a better day, we would say.")
        print("You wanna' have some?")
        print("...")
        print("No?")
        print("Well, your loss. But remember, there's always a fresh supply here!")
        print("*wink*")
        counter = 1
      if each_word == "happy" and counter == 0:
        print("Well," + name + ", look's like it's time for some rum!")
        print("Yes, the good stuff.....")
        print("Huh? Oh yah, you're not like us.")
        print("Uh..... here's a cookie to chew on then.")
        print("Uh..... take another one.....")
        counter = 1
      if each_word == "tired" and counter == 0:
        print("Working your butt off the whole day? Hardworking, I'se say.")
        print("You should remember to hole up once in a while, lad")
        print("Otherwise..... * lowers voice *")
        print("Your' bones will melt and all the meat falls out in clumps....")
        print("...")
        print("Now don't look so sad, lad. It's just a story.")
        print("But it just might happen to you.....")
        counter = 1
      if each_word == "bored" and counter == 0:
        print("Well," + name + ", what are you waiti'n for?Do something for the crew!")
        print("Yes, the good stuff.....")
        print("Huh? Oh yah, you're not like us.")
        print("Uh..... fix the sails.")
        print("Uh..... Man the rigging.....")
        counter = 1
      
      if counter == 0:
        print("What? I don't know what you are saying!")
        print("Oh nevermind. Your feelings can stay to yourself.")
        print("You can tell me them later.")
        counter = 1
          
    while counter == 1:
    description = input("You look troubled, is that nasty shark biting your leg again?")
    list_of_words = description.split()
    for each_word in list_of_words:
      if each_word == "no" or "No" and counter == 1:
        print("Oh?")
