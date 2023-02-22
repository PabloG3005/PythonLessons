
# uzycie petla while

print ('Tem program uzywa petli "while i <= y:" do wyliczenia sumy liczb')

x = int (input('Podaj pierwsza liczbe w ciagu od 1 do 100: '))
y = int (input('Podaj ostatnia liczbe w ciagu od 1 do 100: '))

print ('Kolejne sumy liczb w ciagu od ',x,' do ', y)
n = 0
i = x
while i <= y: 
    n = n + i
    print ('Suma #', i, ': ', n)
    i+=1 # i = i + 1
