#this program must return the name of the person
#when a fax number is entered

fax_numbers = {
    '0866318603': 'Hesthea',
    '0866318738': 'Fransina',
    '0866207753': 'Bulelni',
    '0864522341': 'Celiwe',
    '0862480979': 'Girley',
    '0866435215': 'Helen',
    '0866220131': 'Khanyi',
    '0864805079': 'Ludene',
    '0866211239': 'Stephen',
    '0862040019': 'Vashna',
    '0864522340': 'Shannon'
    }

def fax_get():
    fax= (str(input("Enter fax number: ")))
    for i in fax_numbers:
        if i == fax:
            name = fax_numbers.get(fax)
            print(name)
            break
    print ('If not found, sorry number does not exist!' )

while True:
    fax_get()
