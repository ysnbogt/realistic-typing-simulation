import random
import string
import time

filename = "your_file.txt"

keyboard_layouts = {
    "QWERTY": 0.05,
    "AZERTY": 0.1,
    "QWERTZ": 0.075,
}

difficult_chars = ["q", "z", "x", "c", "p"]
special_chars = string.punctuation
keyboard_layout = "QWERTY"


def simulate_typing_speed(base_speed: float) -> float:
    random_speed = random.uniform(0.8, 1.2)
    return base_speed * random_speed


with open(filename, "r") as file:
    for line in file:
        for char in line:
            print(char, end="", flush=True)
            wait_time = keyboard_layouts.get(keyboard_layout, 0.1)

            wait_time = simulate_typing_speed(wait_time)

            if char in [" ", "\n"]:
                wait_time += random.uniform(0.05, 0.15)

            if char == "." or char == ",":
                wait_time += random.uniform(0.2, 0.4)

            if char.lower() in difficult_chars:
                wait_time += random.uniform(0.05, 0.15)

            if char in string.ascii_uppercase or char in special_chars:
                wait_time += random.uniform(0.05, 0.15)

            time.sleep(wait_time)

            if random.uniform(0, 1) < 0.05:
                print("\b \b", end="", flush=True)
                time.sleep(random.uniform(0.1, 0.2))
                print(char, end="", flush=True)
