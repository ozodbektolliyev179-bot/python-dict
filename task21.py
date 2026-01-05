def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for name in names:
        result[name] = names.count(name)
    return result


names = ['ali','veli','veli','ali','veli','sami','sami','sami']
result = count_names(names)
print(result) 