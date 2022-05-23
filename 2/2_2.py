x = 5
x == 5 and 3                 # 3  '5 and 3' nie znaduje się w nawiasie. Python najpierw sprawdził, że 'x == 5' jest prawdą,
                             # więc przeszedł do kolejnej części i zwrócił 3.
                             
                             
x == 4 and 3                 # False  'x' nie jest równe 4, więc Python nie sprawdza dalej.
3 and x == 5                 # True    Podobnie jak w pierwszym przypadku. Python zwrócił wynik ostatniego działania, czyli 'x == 5'.
3 and x == 4                 # False   'x' nie jest równe 4, więc wyświetla się wynik "False"

isinstance(True, int)         # True
isinstance(True, bool)        # True 
# 'True' należy do klasy 'bool', która jest podklasą 'int'.

