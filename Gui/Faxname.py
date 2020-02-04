from tkinter import *

root = Tk()

root.title('Fax Number locator')

# fax_numbers = {
#     '0866318603': 'Hesthea',
#     '0866318738': 'Fransina',
#     '0866207753': 'Bulelni',
#     '0864522341': 'Celiwe',
#     '0862480979': 'Girley',
#     '0866435215': 'Helen',
#     '0866220131': 'Khanyi',
#     '0864805079': 'Ludene',
#     '0866211239': 'Stephen',
#     '0862040019': 'Vashna',
#     '0864522340': 'Shannon'
#     }


mylabel1 = Label(root, text='Name:')
mylabel2 = Label(root, text='Enter Fax Numbers:')
myFax = Entry(root)


def fax_get():
	fax_numbers = {
	'0866318603': 'Hesthea',
	'0866318738': 'Fransina',
	'0866207753': 'Bulelani',
	'0864522341': 'Celiwe',
	'0862480979': 'Girley',
	'0866435215': 'Helen',
	'0866220131': 'Khanyi',
	'0864805079': 'Ludene',
	'0866211239': 'Stephen',
	'0862040019': 'Vashna',
	'0864522340': 'Shannon'
	}
	a = myFax.get()
	name = fax_numbers.get(a)
	Label(root, text=name).grid(row=3,column=2)


SubmitButton = Button(root,text="Search", command = fax_get)
# root.bind("SubmitButton", fax_get)


mylabel2.grid(row=1, column=1)
myFax.grid(row=1,column=2)
SubmitButton.grid(row=2, column=1)
mylabel1.grid(row=3, column=1)



root.mainloop()