# QUESTION:

# 1. The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
# 2. When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
# 3. For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.



# SOLUTION:

# Importing important librares
import random
import re

# Define categories
categories = {
  "Fruits": ["kiwi", "peach", "pear", "fig", "plum", "papaya", "apricot"],
  "Animals": ["dog", "cat", "lion", "kangaroo", "zebra", "giraffe", "elephant", "panda", "cheetah"],
  "Colors": ["red", "green", "black", "cyan", "maroon", "turquoise", "indigo", "lavender", "coral", "gold"],
  "Countries": ["usa", "france", "japan", "italy", "spain", "brazil", "canada", "india", "australia", "germany"],
  "Vegetables": ["carrot", "broccoli", "lettuce", "onion", "radish", "celery", "cabbage", "zucchini", "asparagus", "eggplant"],
  "Tools": ["hammer", "wrench", "drill", "saw", "level", "chisel", "screwdriver", "pliers", "trowel"],
  "Transportation": ["car", "bus", "bicycle", "train", "airplane", "boat", "subway", "truck", "motorbike", "helicopter"],
  "Professions": ["doctor", "teacher", "engineer", "artist", "chef", "lawyer", "nurse", "plumber", "scientist", "architect"],
  "Technology": ["computer", "phone", "tablet", "internet", "software", "robot", "camera", "microphone", "headphones", "printer", "keyboard", "mouse", "smartwatch"],
  "Weather": ["sun", "snow", "wind", "hail", "rainbow", "thunder", "lightning", "cloudy", "sunny", "stormy"],
  "Hobbies": ["fishing", "painting", "gardening", "cycling", "singing", "writing", "dancing", "cooking", "photography", "reading"],
  "Music": ["piano", "bass", "singer", "violin", "trumpet", "guitar", "drums", "accordion", "ukulele", "harmonica"],
  "Shapes": ["circle", "pentagon", "hexagon", "sphere", "cylinder", "diamond", "octahedron", "pyramid", "rectangle", "oval"],
  "Emotions": ["happy", "sad", "calm", "loved", "bored", "excited", "content", "anxious", "curious", "surprised"],
  "Clothing": ["shirt", "shoes", "hat", "socks", "scarf", "skirt", "jumper", "trousers", "gloves", "sweater"],
  "Sports": ["soccer", "tennis", "swimming", "cycling", "running", "volleyball", "baseball", "skiing", "surfing", "golf"],
  "Science": ["physics", "biology", "geology", "mathematics", "botany", "zoology", "ecology", "genetics", "chemistry", "astronomy", "psychology"],
  "Desserts": ["cake", "pie", "pudding", "muffin", "brownie", "cookie", "cupcake", "ice cream", "macarons", "cheesecake"],
  "Movies": ["comedy", "horror", "romance", "adventure", "fantasy", "animation", "thriller", "mystery", "western", "documentary"],
  "Instruments": ["flute", "xylophone", "sitar", "trombone", "accordion", "harmonica", "clarinet", "bagpipes", "didgeridoo", "viola"]
}

# Select a random category.
categoryAndWords = random.choice(list(categories.items()))

# Define category.
category = categoryAndWords[0]

# Detect word which contains a character at least twice.
rgx = re.compile(r'.*(.).*\1.*') 

# Function for selecting (non repeating characters) word.
def filter_words(words):
    for word in words:
        if rgx.match(word) is None:
            yield word

# Select and define a random word from category.
WORD = random.choice(list(filter_words(categoryAndWords[1])))

# # If you want to cheating so, uncommint it.
# print(WORD)

# Playing turns.
chances = len(WORD) + 2

# Get user name.
user_name = input("Your name: ")

# Dashes for characters.
dashes = ""
for i in range(1, len(WORD) + 1):
    dashes = dashes + "_"

# Greeting user.
print(f"\n{user_name} you have {chances} chances Good luck!")
print(f"Guess the word {dashes} HINT: word is from {category}!\n")


# While loop for running & combining all things in game.
while chances > 0:
    # Get user guess.
    user_guess = input("Guess a character: ")

    # If user guess is correct.
    if user_guess in WORD and user_guess != "":
        # Define word index.
        word_index = WORD.index(user_guess)
        # Convert dashes & characters to a list.
        charList = list(dashes)
        # Filled a dash with alphabet at correct index.
        charList[word_index] = user_guess
        # Rejoin all dashes & alphabets
        dashes = "".join(charList)

    # If user guess is wrong.
    elif user_guess not in WORD:
        # 1 turn is subtracted.
        chances -= 1
        # Tell number of turns to user
        print("Wrong, You have", chances, "more guesses\n")

        # If all turns are used.
        if chances == 0:
            # Print loose & end the game with break.
            print("You Loose!")
            break

    # Printing dashes
    print(dashes,"\n")
    
    # If all dashes are filled.
    if "_" not in dashes:
        # Celebrate winning & end the game with break.
        print(f"Congratulations {user_name} you win!")
        break