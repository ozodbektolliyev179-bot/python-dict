def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    result = []
    for _, user in users.items():
        if user['active']:
            result.append(user)

    return result

users = {
    '1': {'name': 'Ali', 'active': True},
    '2': {'name': 'Vali', 'active': False},
    '3': {'name': 'Gani', 'active': True},
    '4': {'name': 'Sami', 'active': False},

}

reselt = get_active_users(users=users)
print(reselt)
