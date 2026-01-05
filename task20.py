permissions = {"read": True, "write": False, "delete": True}

for i in permissions:
    if permissions[i]:
        print(i)