
person = {"name": "Ali", "age": 25, "city": "Tashkent"}


key = input("Qaysi kalitni o'chirmoqchisiz? ")


if key in person:
    del person[key]  
    print("O'chirildi")
else:
    print("Bunday kalit yo'q")

print(person)
