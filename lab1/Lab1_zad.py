### Zad 1 ###
x = int(input("Podaj liczbę x\n"))
y = int(input("Podaj liczbę y\n"))
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)
print("x / y + x - x * x = ", x / y + x - x * x)

### Zad 2 ###

name = input("podaj imię\n")
print("Witaj ", name)

### Zad 3 ###

print(float(int(input("Podaj liczbę pierwszą\n")) + int(input("Podaj liczbę drugą\n"))))

### Zad 4 ###

print(sum(range(8, 81)))

### Zad 5 ###
from datetime import datetime

y = int(input("Podaj rok: "))
m = int(input("Podaj miesiąc: "))
d = int(input("Podaj dzień: "))

print(datetime.today() - datetime(y, m, d))

### Zad 6 ###

bool = True
print("Wybierz: 1 - dodawanie, 2 - odejmowanie, 3 - dzielenie, 4 - mnożenie, każdy inny kończy pracę kalkulatora.")
while bool:
    choosen = int(input("wprowadź numer operacji jaką chcesz wykonać: "))
    if choosen == 1:
        print(int(input("Podaj pierwszy składnik")) + int(input("Podaj drugi składnik")))
    elif choosen == 2:
        print(int(input("Podaj pierwszy składnik")) - int(input("Podaj drugi składnik")))
    elif choosen == 3:
        print(int(input("Podaj pierwszy składnik")) / int(input("Podaj drugi składnik")))
    elif choosen == 4:
        print(int(input("Podaj pierwszy składnik")) * int(input("Podaj drugi składnik")))
    else: bool = False