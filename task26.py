def merge_dicts(a: dict, b: dict) -> dict:
    a.update(b)

    return a


d1 = {
    'name': 'ali',
    'age': 23
}
d2 = {
    'email':'ali@gmail.com',
    'gender': 'male'
}

user = merge_dicts(d1, d2)
print(user)