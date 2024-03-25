# POROČILO
## Opis Naloge
Program je napisan v pythonu s pomočjo knjižnice **Flask**. Program je zasnovan kot spletna aplikacija katere cillj je prikazovanje prihajajočih testov. Uporabnik lahko pod pogojem da ima uporabniško ime in geslo dodaja ali odstranjuje teste. 
## Načrt Programa
Program deluje s pomočjo python knjižnice **Flask** ter **SQLAlchemy** podatkovne baze. Flask poskrbi za vse funkcije dodajanja in brisanja podatkov iz baze ter pa tudi prikaz na sami spletni strani.
- Flask rendera spletno stran
- S pomočjo funckije **for test in testi** naredimo nov element na ne urejenem listu __(unordered list)__ ter vsakemu testu dodamo tudi gumb za izbris.
- Funkcija v Flasku teste razporedi po padajočem datumu.
- Preverimo tudi če je datum testa že pretekel v temu preimeru test izbrišemo
- Imamo **Bootstrap** drop down meni v katerem imamo gumbe ki nas odplejejo na različne dele spletnega mesta npr. Login, Dodaj test ipd.
- **Flask Session** nam omogoča da ko se uporabnik prijavi lahko s pomočjo piškotkov shranimo njegov _session_ tako vemo ali je uporabnik prijavljen ali ne.
- Imamo tudi seznam za ustno spraševanje kjer lahko dodajamo ljudi van vendar žal deluje le napol


# To Do List
- [x] dodajanje testov
- [x] brisanje testov
- [x] dodatne funkcije
- [ ] več seznamov ❌
- [ ] dnevi pri testih ❌
- [x] razdelitev testov ~~po predmetu~~ in datumu
## Progress
Programu manjkajo funckije ter lpeša grafika.

# Dokazi o naučenem
### Koncept vejitve (if stavek) 


