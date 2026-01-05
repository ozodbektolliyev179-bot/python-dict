def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    age_group = {}
    for person in people:
        age = person['age']
        if age not in age_group:
            age_group[age] = []
        age_group[age].append(person['name'])
    return age_group
people = [
    {'name': 'Ali', 'age': 25},
    {'name': 'Vali', 'age': 30},                    
    {'name': 'Sami', 'age': 25},
    {'name': 'Gani', 'age': 30},
    {'name': 'Jon', 'age': 35},
]
result = group_by_age(people)
print(result)