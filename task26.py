def merge_dicts(a: dict, b: dict) -> dict:
    result = a.copy()   

    for key in b:
        result[key] = b[key]  

    return result
a = {"x": 1, "y": 2}
b = {"y": 5, "z": 3}

print(merge_dicts(a, b))

