import json

from praca_domowa2.Manager import Manager
from FileHandler import save_saldo_and_magazyn_to_file, save_history
manager = Manager(history_file="history.txt", magazyn_and_saldo_file="saldo_i_magazyn.txt")

@manager.assign("Saldo")
def change_saldo(manager: Manager):
    changes = input("Chcesz dodać czy odjąć z konta? (-/+)")
    try:
        if changes == "+":
            amount = float(input("Podaj kwotę, którą chcesz dodać"))
            manager.saldo += amount
            manager.history.append(f"Wykonano instrukcję saldo zasilono {amount} \n")
            return int(manager.saldo), manager.history
        elif changes == "-":
            amount = float(input("Podaj kwotę, którą chcesz odjąć"))
            manager.saldo -= amount
            manager.history.append(f"Wykonano instrukcje saldo zmniejszono {amount} \n")
            return int(manager.saldo), manager.history
    except:
        print("Wystąpił błąd, musisz wpisać kwotę!")


@manager.assign("Sprzedaz")
def sell_item(manager: Manager):
    try:
        print(manager.magazyn)
        product = input("Podaj nazwę produktu: ")
        amount = int(input("Podaj ilość, którą chcesz sprzedać: "))
        if amount <= manager.magazyn[product]["ilosc"]:
            manager.magazyn[product]["ilosc"] -= amount
            manager.saldo += (manager.magazyn[product]["cena"] * amount)
            manager.history.append(f"Sprzedano {product} w ilości {amount} \n")
            if manager.magazyn[product]["ilosc"] == 0:
                del manager.magazyn[product]
                print(f"Usunięto {product} z magazynu")
                manager.history.append(f"Usunięto {product} z magazynu, \n")
        else:
            print("Zbyt mała ilość w magazynie!")
            manager.history.append(f"Nie udało się sprzedać towaru {product}, mamy go za mało na magazynie \n")
            pass
    except ValueError:
        print("Wystąpił błąd")

@manager.assign("Zakup")
def buy_item(manager: Manager):
    print(manager.magazyn)
    product = input("Podaj nazwe produktu: ")
    amount = int(input("Podaj ilość: "))
    if not product in manager.magazyn.keys():
        value = int(input("Podaj cene produktu: "))
        manager.magazyn[product] = {"ilosc": amount,
                            "cena": value}
        saldo2 = (manager.magazyn[product]["cena"]) * amount
        manager.saldo -= int(saldo2)
        manager.history.append(f"Dodano {product} w ilości {amount} do magazynu, \n")
        print(manager.magazyn)
        pass
    elif product in manager.magazyn.keys():
        manager.magazyn[product]["ilosc"] += amount
        saldo2 = (manager.magazyn[product]["cena"]) * amount
        manager.saldo -= int(saldo2)
        manager.history.append(f"Zakupiono {product} w ilości {amount}, \n")
@manager.assign("Konto")
def check_saldo(manager: Manager):
    print(manager.saldo)

@manager.assign("Lista")
def check_list(manager: Manager):
    print(manager.magazyn)
@manager.assign("Magazyn")
def check_magazine(manager: Manager):
    print(list(manager.magazyn.keys()))
@manager.assign("Historia")
def lookup_for_data(manager: Manager):
    value_from = input("Podaj początkowy zakres")
    value_to = input("Podaj końcowy zakres")
    history2 = open("history.txt", mode="r+")
    if history2.readable():
        try:
            if value_from and not value_to:
                value_from = int(value_from)
                value_to = int()
                print(history2.readlines()[value_from:value_to])
            elif not value_from and value_to:
                value_from = int(0)
                value_to = int(value_to)
                print(history2.readlines()[value_from:value_to + 1])
            elif value_from and value_to:
                od = int(value_from)
                do = int(value_to)
                print(history2.readlines()[od:do + 1])
            else:
                print(history2.readlines())
        except ValueError:
            print("Podana wartość jest błędna")

@manager.assign("Koniec")
def end_program(manager: Manager):
    save_saldo_and_magazyn_to_file(file="saldo_i_magazyn.txt", saldo=manager.saldo, magazyn=manager.magazyn)
    with open("history.txt", mode="w") as save_history:
        historytxt = "".join(manager.history)
        save_history.write(historytxt)
        end_program = True