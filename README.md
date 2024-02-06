# POROČILO
>[!WARNING]
>Koda bo uploudana ko bom vse spravil v en program. Trenutno ima vsaka funckija en program

>[!NOTE]
>Projekt je izdelan za projektno nalogo pri projektu Informatika v 1. letniku na Gimnaziji Vič
## Opis Naloge
Izdelujemo poenostavljeno verzijo windows task manager-ja v proramskem jeziku python
## Načrt Programa
Program deluje tako da z uporabo knjižnice **psutil** pridobi podate o uporabi CPU-ja in RAM-a ter jih sharni v spremenljike. Z uporabo knjižnice **wmi** program pridobi podatke o vseh procesi, ki se izvajajo na računalniku ter jih shrani v list. Nato ustvarimo GUI s pomočjo **tkinter** knjižnice. Podatke o programih nato pirkažemo v tkinter oknu. V tkinter GUI lahko nato vnesemo PID(process id), ki ga nato s pomočjo **os**
knjižnice lahko prisilno ustavimo(enako kot windows task manager).
# To Do List
- [x] GUI
- [x] PID list
- [x] Process kill
- [x] Performance graph
- [ ] združitev seh funkcij v en program
- [ ] Hitrejši startup time
- [ ] Lepši GUI
- [ ] iskalnik procesov
- [ ] izboljšava Poročila
## Progress
Program zanekrat deluje precejo okorno ter počasi vendar osnovne funkcije delujejo, v prihodnosti bo izboljšan.

