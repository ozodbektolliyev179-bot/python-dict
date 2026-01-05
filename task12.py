
inventory = {"apple": 5, "banana": 3}

product = input("Mahsulot nomi: ")

if product not in inventory:
    inventory[product] = 0

print(inventory)
