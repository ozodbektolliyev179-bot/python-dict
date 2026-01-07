phonebook: dict[str, str] = dict()
def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print1:('1: Kontakt qo\'shish (ism -> telefon)\n'
        '2: Barcha kontaktlarni chiqarish\n' 
        '3: Ism bo\'yicha telefon qidirish')


        choice = input('> ')
        if choice == '1':
            name = input('name: ')
            phone = input('phone: ')

            phonebook[name] = phone
            print('kontakt muvaffaqiyatli qo\'shildi.')
        elif choice == '2':
            for name, phone in phonebook.items():
                print(name, phone)
        elif choice == '3':
            search = input('Search (name): ')

            for name, phone in phonebook.items():
                if search.lower() in name.lower():
                    print(name, phone)
                else:
                    print('Bunday ism mavjud emas.')

phonebook_menu(phonebook)

print(phonebook)
    
   

    
    