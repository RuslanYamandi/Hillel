

def new_format(num: str):
    if len(num) > 3:
        num = num[::-1]
        result = []
        for idx, char in enumerate(num):
            result.append(char)
            position = idx + 1
            if position < len(num) and position % 3 == 0:
                result.append('.')
        return ''.join(result)[::-1]
    return num


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
