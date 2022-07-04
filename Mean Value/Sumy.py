

x = int (input('Podaj pierwsza liczbe w ciagu od 1 do 100: '))
y = int (input('Podaj ostatnia liczbe w ciagu od 1 do 100: '))


i = 0
print ('Kolejne sumy liczb w ciagu ', x, y)
for n in range (x, y+1):
    i = i + n
    print (i)


n = 0
i = x
while i <= y: 
    n = n + i
    print (n)
    i+=1
