import random


def generate_words(count: int):
    if count > 10_000:
        raise Exception("Too many words requested.")
    i = 0
    with open('words.txt', 'r') as file:
        for word in file:
            if i >= count:
                break
            if random.randint(0, 10) < 2:
                yield word.strip()
                i += 1


print(list(generate_words(1000)))
