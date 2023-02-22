# uzycie petli for i in range 

print ('Tem program uzywa petli "for n in range" do wyliczenia sumy liczb parzystych')

i = 0
x = int (input('Podaj pierwsza liczbe od 1 do 200: '))
y = int (input('Podaj ostatnia liczbe od 1 do 200: '))

print ('Kolejne sumy liczb parzystych w ciagu od ', x, ' do ', y)
for n in range (x, y+1):
    if (n % 2 == 0):
        i = i + n
        print ('Suma #', n, ': ', i)

