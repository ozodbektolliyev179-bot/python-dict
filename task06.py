car = {
    'brand': "Chevrolet",
    'model': "Malibu",
    'color': "white",
}

key = input('key:')

if key in car.keys():
    value = car[key]
else:
    value = 'topilmadi'

print(value)