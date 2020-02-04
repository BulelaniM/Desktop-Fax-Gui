from tkinter import *

root = Tk()

root.title('Fax Number locator')


mylabel1 = Label(root, text='Name:')
mylabel2 = Label(root, text='Enter Fax Numbers:')
myFax = Entry(root)

#function grabs number from dictionery and returns value pair
def fax_get():
	fax_numbers = {
	'0866318603': 'Dummy1',
	'0866318738': 'Dummy2',
	'0866207753': 'Dummy3',
	}

	a = myFax.get()
	name = fax_numbers.get(a)
	Label(root, text=name).grid(row=3,column=2)


SubmitButton = Button(root,text="Search", command = fax_get)

#Maps widgets to window
mylabel2.grid(row=1, column=1)
myFax.grid(row=1,column=2)
SubmitButton.grid(row=2, column=1)
mylabel1.grid(row=3, column=1)

#Initiates window
root.mainloop()