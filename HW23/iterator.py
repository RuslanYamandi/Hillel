class CustomIterator:
    def __init__(self, data, key_func, value_func):
        self.data = data
        self.keys = list(self.data.keys())
        self.index = 0
        self.key_func = key_func
        self.value_func = value_func

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        new_key = self.key_func(key)
        new_value = self.value_func(self.data[key])
        self.index += 1
        return new_key, new_value

    def __call__(self):
        transformed_dict = {}
        for new_key, new_value in iter(self):
            transformed_dict[new_key] = new_value
        return transformed_dict


sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

result = CustomIterator(sample_dict, lambda x: x.upper(), lambda x: x * 2)()
print(result)
