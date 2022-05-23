t = (2, 4)
print(t[2]) # Błąd: tuple index out of range. W Pythonie liczenie zaczyna się od 0, a nie od 1.
t.append(6) # Błąd: 'tuple' object has not attribute 'append'. Funkcję append() można stosować w przypadku list, a nie krotek.
a, b = t ; print(a, b) # Wynik: 2, 4. Do a i b zostały przypisane kolejne elementy krotki t.