import random


def read_file_lazy(file_path):
    with open(file_path, 'r') as file:
        for word in file:
            yield word


def generate_words(count: int):
    result = set()
    if count > 10_000:
        raise Exception("Too many words requested.")
    for word in read_file_lazy('words.txt'):
        if len(result) >= count:
            break
        if random.randint(0, 10) < 2:
            result.add(word.strip())
    return result


words = generate_words(1000)
print(words)
