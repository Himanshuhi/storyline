import random

# Define lists of possible story elements
characters = ["Himanshu", "Alice", "Bob", "Charlie", "Dave"]
actions = ["discovered a programming book in the library", "attended a coding workshop", "watched a tutorial online"]
outcomes = ["and found his passion for programming", "but initially struggled to understand it", "and decided to pursue it as a career"]

# Generate a random story
character = random.choice(characters)
action = random.choice(actions)
outcome = random.choice(outcomes)

story = f"{character} {action} {outcome}."

# Print the story
print(story)
