
A = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]


def get_max_deep(nums: list) -> int:
    length = len(nums)
    top = None
    bottom = None
    deep = 0

    for i in range(length):
        val = nums[i]
        if i == 0:
            top = val
            continue
        if i == length - 1:
            continue
        if val > top:
            top = val
            bottom = None
        elif val < top:
            if bottom is None:
                bottom = val
            elif val < bottom:
                bottom = val
        if top is not None and bottom is not None:
            diff = top - bottom
            if diff > deep:
                deep = diff
    return deep


max_deep = get_max_deep(A)
print(max_deep)



