
class WordsGenerator:
    MAX_WORDS = 10_000
    file_path = 'words.txt'

    @classmethod
    def generate(cls, count: int):
        result = set()
        if count > cls.MAX_WORDS:
            raise Exception("Too many words requested.")
        for line in cls._read_file():
            if len(result) > count:
                break
            words = line.strip().split(' ')
            for word in words:
                if word:
                    result.add(word.strip('.').strip(','))
        return result

    @classmethod
    def _read_file(cls):
        with open(cls.file_path, 'r') as file:
            for line in file:
                yield line


words = WordsGenerator.generate(10_000)
print(words)
