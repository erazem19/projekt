# POROČILO
## Opis Naloge
Program je napisan v pythonu s pomočjo knjižnice **Flask**. Program je zasnovan kot spletna aplikacija katere cillj je prikazovanje prihajajočih testov. Uporabnik lahko pod pogojem da ima uporabniško ime in geslo dodaja ali odstranjuje teste. 
## Načrt Programa
Program deluje s pomočjo python knjižnice **Flask** ter **SQLAlchemy**  in pa database **SQLite**. Flask poskrbi za vse funkcije dodajanja in brisanja podatkov iz baze ter pa tudi prikaz na sami spletni strani.
- Flask rendera spletno stran
- S pomočjo funckije **for test in testi** naredimo nov element na ne urejenem listu __(unordered list)__ ter vsakemu testu dodamo tudi gumb za izbris.
- Funkcija v Flasku teste razporedi po padajočem datumu.
- Preverimo tudi če je datum testa že pretekel v temu preimeru test izbrišemo
- Imamo **Bootstrap** drop down meni v katerem imamo gumbe ki nas odplejejo na različne dele spletnega mesta npr. Login, Dodaj test ipd.
- **Flask Session** nam omogoča da ko se uporabnik prijavi lahko s pomočjo piškotkov shranimo njegov _session_ tako vemo ali je uporabnik prijavljen ali ne.
- Imamo tudi seznam za ustno spraševanje kjer lahko dodajamo ljudi van vendar žal deluje le napol

## +
Če bi se spletna stran dejansko deployala bi bilo potrebno uporabnike vezati na podatkovno bazo trenutno sta nastavljena dva uporabnika kot user1 in user2 z gesloma password1 in password2 fino bi bilo tudi dodati sistem kjer shranimo hashano geslo ter primerjamo hashana gesla. Ker pa ta projekt ni namenjen temu lahko uporabljamo kar tak sistem. 

# To Do List
- [x] dodajanje testov
- [x] brisanje testov
- [x] dodatne funkcije
- [ ] več seznamov ❌
- [ ] dnevi pri testih ❌
- [x] razdelitev testov ~~po predmetu~~ in datumu

# Dokazi o naučenem
### Koncept zaporednosti izvajanja ukazov
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot0(inf).png)  
Najprej preverimo če je uporabnik prijavljen šele na to ga pošljemo na stran za dodajanje testov.


### Koncept vejitve (if stavek) 
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot1(inf).png)  
Preverimo če je uporabnik prijavljen, če ni ga vrnem nazaj na _index.html_.

### Koncept zanke 
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot2(inf).png)  
Za vsak test v podatkovni bazi naredimo nov element na _unordered listu_.

### Dogodkovno programiranje 
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot3(inf).png)  
Ko uporabnik pritisne gumb _add_ pošljemo _**POST**_ ukaz ki ga _main.py_ sprejme. Ta nato vzame podatke, ki smo jih vnesli v _html form_, ter jih shrani v bazo podatkov.

### Branje in izpisovanje (IO ukazi) 
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot%204.1(inf).png)  
V _form_ za dodajanje testov napišemo podatke o testu  
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot4(inf).png)  
Te na to program izpiše na _index.html_  

### Koncept spremenljivke 
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot5(inf).png)  
Ustvarimo sprmenčjivko _danminus1_ katero nastavimo na včerajšnji datum. Nato za vsak test v bazi preverimo če je njegov datum enak spremenljivki _danminus1_.  
_strftime("%Y-%m-%d") obrne vrstni red datuma v leto-mesec-dan._

### Tabelarična spremenljivka (list) 
![image](https://github.com/erazem19/projekt/blob/main/slike/Screenshot6(inf).png)  
V mojem projektu dejanskih **_python listov_** nisem uporabil saj za to ni bilo potrebe. Sem pa uporabil **SQLite** podatkovno bazo v katero shranjujemo vse podatke. Vsak test dobi svoj id, predmet, ter datum.  
_return f"Test(subject='{self.subject}', date='{self.date}', details='{self.details}')"_ s pomočjo tega ukaza nato vse podatke spravimo v lepo obliko berljivo za program.  

# ZAKLJUČEK
Projekt je še kar uredu usepel vendar mi na žalost ni useplo narediti funkcije ki bi nam omgočala dodajanje več seznamov za ustna spraševanja. Zaradi tega je ta funckcija precej neuporabna. To je seveda zaradi mojih zelo omejenih izkušenj z podatkovnimi bazami in se mi je pojvaila težava ko sem dodal tretjo tabelo vanjo je začelo vse skupaj delati malo posvoje.  
Prav tako dizajn ni ravno najlepši, ker čeprav css še kar uredu poznam ga nimam prav preveč rad in tudi naloga je o pythonu ne pa css in html za to sem več časa posvetil Pythonu(stvari kot so naprimer ozadje ne delajo najbolje).  
Nekaterih funkcij ki bi si jih želel mi tudi ni useplo vključiti ker bi za vse te stvari potreboval dejansko znati SQLite vnedar sem še kar zadovoljen kako mi je usepelo glede na to da ga prvič uporabljam.

#### Erazem Perko 1.b GIMVIC 2024©
