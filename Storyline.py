import random

characters = ["Himanshu", "Anil", "ram", "himzo", "ravi"]
actions = ["discovered a programming book in the library", "attended a coding workshop", "watched a tutorial online"]
outcomes = ["and found his passion for programming", "but initially struggled to understand it", "and decided to pursue it as a career"]

character = random.choice(characters)
action = random.choice(actions)
outcome = random.choice(outcomes)

story = f"{character} {action} {outcome}."

print(story)
