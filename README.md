# pythonproject
Python course final exam 

Cilj zadatka je bio razvoj aplikacije koja ce imati osnovne CRUD funkcionalnosti nad najmanje cetiri tabele u bazi podataka.
Tabele ne trebaju biti u relacijama, jer u toku kursa nije radeno modelovanje baze.

Aplikacija je osmišljena da korisnicima sportske ustanove (teretana, fitnes) omoguci osnovne CRUD operacije nad cetiri kategorije, 
odnosno tabele:
1. treneri
2. korisnici
3. oprema
4. proizvdi za suplementaciju ishrane

Projekat sadrži tri python fajla i jednu sqlite bazu podataka.
- Dokument baze2create.py sadži kod kojim se kreira sama baza i cetiri tabele unutar baze.
- Dokument klase.py sadrži definisane klase i funkcije za sve CRUD operacije nad cetiri tabele
- Dokument Konzola.py simulira UI gdjekorisnik može da se krece kroz menije i izvršava operacije

Pored navedena tri python fajla, repozitorijum sadrži i kreiranu sqlite bazu sa odredenim brojem vec unesenih slucajeva u svim tabelama.
