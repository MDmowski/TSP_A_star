# PSZT Projekt 1.
## Zadanie MM.P1
Zaimplementować i przetestować algorytm A\* dla problemu komiwojażera. Porównać działanie algorytmu A\* z algorytmem zachłannym i przeszukiwaniem brute force (dla bf przerwać obliczenia w pewnym momencie). WE: plik ze współrzędnymi punktów. WY: najkrótszy cykl łączący punkty.
### Zespół
- Adam Szałowski
- Maciej Dmowski

## Przyjęte założenia

### Format pliku wejściowego
Każdy punkt zapisany w osobnej linijce w postaci wartości współrzednych (liczba zmiennoprzecinkowa) oddzielonych spacją. Pierwszy punkt jest punktem startowym.
```
0 0
1 0.5
10.15 14.1
...
```

### Format pliku wyjściowego
Taki sam jak format pliku wejściowego. Punkty posortowane w kolejności ułożenia ich na ścieżce.

### Wybrany język
Python

### Doprecyzowanie treści
Każdy punkt w pliku wejściowym to jeden wierzchołek grafu. Każdy wierzchołek łączy się ze wszystkimi pozostałymi (graf pełny), a waga danej krawędzi to odległość między
łączonymi punktami w układzie współrzędnych.


### TODO
- export state to file - A
- implement greedy alg. - M
- implement brute force - M
- implement timing - A
- measure time for different algs. - A
- visualize - A
- conclusions - A,M

