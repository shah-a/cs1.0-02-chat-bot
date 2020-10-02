# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Sept. 27, 2020
# CS1.0 Assignment 2: Chat Bot

"""
Avatar: The Last Airbender quote bot

This is a chat bot that returns quotes to the user based on
their string inputs. Quotes are randomly chosen from lists containing
three quotes per character.

Program loops indefinitely, returning quotes based on user input until
user inputs keyword 'done'.
"""

from random import choice


def get_bot_response(response):
    """Returns a randomly selected quote from a character based on user input."""

    # Response set 1 for Aang
    aang = [
        "\"Harsh words won't solve problems, action will!\"",  # S1E11
        "\"The past can be a great teacher.\"",  # S3E13
        "\"It's easy to do nothing, but it's hard to forgive.\"",  # S3E16
    ]

    # Response set 2 for Katara
    katara = [
        "\"It is the strength of your hearts that make you who you are.\"",  # S1E6
        "\"Everybody, hold hands. We can do this. We have to.\"",  # S2E11
        "\"I will never, ever turn my back on people who need me!\"",  # S3E3
    ]

    # Response set 3 for Sokka
    sokka = [
        "\"I'm just a guy with a boomerang. I didn't ask for all this flying and magic!\"",  # S1E2
        "\"It's a giant mushroom! Maybe it's friendly!\"",  # S2E11
        "\"I'm just a guy who likes comedy.\"",  # S3E17
    ]

    # Response set 4 for Uncle Iroh
    iroh = [
        "\"Pride is not the opposite of shame, but its source.\n"
        "True humility is the only antidote to shame.\"",  # S2E9

        "\"It is usually best to admit mistakes when they occur,\n"
        "and seek to restore honor.\"",  # S2E15

        "\"You can't always see the light at the end of the tunnel,\n"
        "but if you just keep moving, you will come to a better place.\""  # S2E20
    ]

    # Response set 5 for Cabbage Merchant
    cabbage = [
        "\"No! My cabbages!\"",  # S1E5
        "\"My cabbages! This place is worse than Omashu!\"",  # S1E9
        "\"My cabb--!... Oh, forget it!\""  # S2E15
    ]

    # Pseudorandom response chosen from a response set selected based on keyword from user
    # "in" checks if keyword is present in user's inputted phrase
    if "Aang" in response or "aang" in response:
        return f"Aang says:\n{choice(aang)}"
    if "Katara" in response or "katara" in response:
        return f"Katara says:\n{choice(katara)}"
    if "Sokka" in response or "sokka" in response:
        return f"Sokka says:\n{choice(sokka)}"
    if "Iroh" in response or "iroh" in response:
        return f"Uncle Iroh says:\n{choice(iroh)}"
    if "Cabbage" in response or "cabbage" in response:
        return f"The Cabbage Merchant says:\n{choice(cabbage)}"

    # Return default statement when user input is unrecognized
    return f"Hmm... I don't have any quotes for {response}"

print('Hey :D! Welcome to the Avatar quote bot!\nEnter "done" to quit the program.\n')

while True:  # Infinite loop; only breaks when user inputs "done"

    user_response = input(
        "Tell me about a character you like from Avatar: The Last Airbender!\n"
        "Be as detailed (or not!) as you like.\n"
        "If I recognize the character, I'll share one of their quotes: "
    )

    if user_response == "done":
        print("\nBye! Thanks for coming!\n")
        break

    print(f"\n{get_bot_response(user_response)}\n")  # Display response message
