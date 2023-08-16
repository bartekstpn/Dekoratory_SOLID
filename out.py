from enums import WyborKomendy
from zadanie_domowe import manager

initial_message = "Witaj w Twoim magazynie. Lista dostępnych komend to:\n" \
                  " 1. Saldo\n 2. Sprzedaż\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przegląd\n 8. Koniec"

end_program = False
print(manager.history)
while not end_program:
    print(initial_message)
    print(manager.saldo)
    print(manager.magazyn)
    operation = input("Wybierz: ")
    if operation == WyborKomendy.ZMIEN_SALDO.value:
        manager.execute("Saldo")
        continue

    if operation == WyborKomendy.SPRZEDAZ.value:
        manager.execute("Sprzedaz")
        continue

    if operation == WyborKomendy.ZAKUP.value:
        manager.execute("Zakup")
        continue

    if operation == WyborKomendy.KONTO.value:
        manager.execute("Konto")
        continue

    if operation == WyborKomendy.LISTA.value:
        manager.execute("Lista")
        continue

    if operation == WyborKomendy.MAGAZYN.value:
        manager.execute("Magazyn")
        continue

    if operation == WyborKomendy.PRZEGLAD.value:
        manager.execute("Historia")
        continue

    if operation == WyborKomendy.KONIEC.value:
        manager.execute("Koniec")
        break


