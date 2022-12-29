# import tkinter

# tkinter._test()

# mainApp = tkinter.Tk()
# Add the codes for the widget here..
# mainApp.mainloop()

# aplikacja ma wyliczac konty w trojkacie na podstawie dlugosci bokow

x = int (input('Podaj dlugosc pierwszego boku: '))
y = int (input('Podaj dlugosc drugiego boku: '))
z = int (input('Podaj dlugosc trzeciego boku: '))

max = x
min1 = y
min2 = z
if (y > max):
    max = y
    min1 = x
if (z > max):
    max = z
    min1 = x
    min2 = y

k1 = arcsin (min1/max)
k2 = arcsin (min2/max)
k3 = 180 - k1 -k2