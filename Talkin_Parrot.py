#(Taliking parrot simple 5 lines Python Code)

# import pyttsx3

# engine = pyttsx3.init()

# text = input("What should the parrot say? 🦜: ")
# engine.say(text)
# engine.runAndWait()

#(2nd Practice Slow Speed Methods) 
# import pyttsx3

# # Initialize the engine
# engine = pyttsx3.init()

# # Adjust speaking rate (speed)
# rate = engine.getProperty('rate')  # Get the current speed
# engine.setProperty('rate', rate - 50)  # Reduce speed (default ~200)

# # Adjust volume (optional)
# volume = engine.getProperty('volume')  # Get current volume
# # engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)
# engine.setProperty('volume', 0.8)


# # Text input
# text = input("What should the parrot say? 🦜: ")
# engine.say(text)

# # Run and wait for the speech to complete
# engine.runAndWait()

#(3rd Method Is Generate Female voice)

# import pyttsx3

# # Initialize the engine
# engine = pyttsx3.init()

# # Adjust speaking rate (speed)
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate - 50)

# # Adjust volume (optional)
# engine.setProperty('volume', 0.9)

# # Set voice to female
# voices = engine.getProperty('voices')  # Get all available voices
# engine.setProperty('voice', voices[1].id)  # Select female voice (index 1)

# # Text input
# text = input("What should the parrot say? 🦜: ")
# engine.say(text)

# # Run and wait for the speech to complete
# engine.runAndWait()
