
import random

print("=" * 45)
print("       🧠 NUMBER MYSTERY GAME")
print("=" * 45)

print("\nWelcome to the Secret Code Challenge!")
print("Find the hidden 4-digit number.")
print("All digits are different.")
print("You have 10 attempts.")

print("\nCLUES:")
print("🟢 Correct digit and correct position")
print("🟡 Correct digit but wrong position")
print("🔴 Digit is not in the secret number")

# Generate secret number
digits = random.sample("0123456789", 4)

# First digit cannot be zero
while digits[0] == "0":
    digits = random.sample("0123456789", 4)

secret = "".join(digits)

attempts = 10
score = 100

# Game starts
while attempts > 0:

    print("\n" + "-" * 45)
    print("Attempts remaining:", attempts)
    print("Current score:", score)

    guess = input("\nEnter your 4-digit guess: ")

    # Validate input
    if len(guess) != 4 or not guess.isdigit():
        print("Please enter exactly 4 digits!")
        continue

    if len(set(guess)) != 4:
        print("Digits must not repeat!")
        continue

    if guess[0] == "0":
        print("The first digit cannot be zero!")
        continue

    # Check answer
    if guess == secret:
        print("\n🎉 CONGRATULATIONS!")
        print("You cracked the secret code!")
        print("Secret number:", secret)
        print("Final score:", score)
        break

    # Calculate clues
    correct_position = 0
    wrong_position = 0

    for i in range(4):
        if guess[i] == secret[i]:
            correct_position += 1
        elif guess[i] in secret:
            wrong_position += 1

    print("\nYour clues:")

    print("🟢 Correct position:", correct_position)
    print("🟡 Wrong position:", wrong_position)
    print("🔴 Not in code:", 4 - correct_position - wrong_position)

    attempts -= 1
    score -= 10

# Game over
if attempts == 0:
    print("\n😢 GAME OVER!")
    print("The secret code was:", secret)
    print("Better luck next time!")

print("\nThanks for playing NUMBER MYSTERY!")

import random

print("=" * 45)
print("       🧠 NUMBER MYSTERY GAME")
print("=" * 45)

print("\nWelcome to the Secret Code Challenge!")
print("Find the hidden 4-digit number.")
print("All digits are different.")
print("You have 10 attempts.")

print("\nCLUES:")
print("🟢 Correct digit and correct position")
print("🟡 Correct digit but wrong position")
print("🔴 Digit is not in the secret number")

# Generate secret number
digits = random.sample("0123456789", 4)

# First digit cannot be zero
while digits[0] == "0":
    digits = random.sample("0123456789", 4)

secret = "".join(digits)

attempts = 10
score = 100

# Game starts
while attempts > 0:

    print("\n" + "-" * 45)
    print("Attempts remaining:", attempts)
    print("Current score:", score)

    guess = input("\nEnter your 4-digit guess: ")

    # Validate input
    if len(guess) != 4 or not guess.isdigit():
        print("Please enter exactly 4 digits!")
        continue

    if len(set(guess)) != 4:
        print("Digits must not repeat!")
        continue

    if guess[0] == "0":
        print("The first digit cannot be zero!")
        continue

    # Check answer
    if guess == secret:
        print("\n🎉 CONGRATULATIONS!")
        print("You cracked the secret code!")
        print("Secret number:", secret)
        print("Final score:", score)
        break

    # Calculate clues
    correct_position = 0
    wrong_position = 0

    for i in range(4):
        if guess[i] == secret[i]:
            correct_position += 1
        elif guess[i] in secret:
            wrong_position += 1

    print("\nYour clues:")

    print("🟢 Correct position:", correct_position)
    print("🟡 Wrong position:", wrong_position)
    print("🔴 Not in code:", 4 - correct_position - wrong_position)

    attempts -= 1
    score -= 10

# Game over
if attempts == 0:
    print("\n😢 GAME OVER!")
    print("The secret code was:", secret)
    print("Better luck next time!")

print("\nThanks for playing NUMBER MYSTERY!")

