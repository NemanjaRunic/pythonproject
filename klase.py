import sqlite3
from sqlite3 import Error
conn=sqlite3.connect('database2.db')


class Person:
    def __init__(self):
        self.id=input('Upiši ID osobe: ')
        self.first_name=input('Upiši ime: ')
        self.second_name=input('Upiši prezime: ')
        self.gender=input('Upiši pol (M/F): ')
        self.age=int(input('Upiši godine starosti: '))


class Customer_create(Person):
    def __init__(self):
        Person.__init__(self)
        self.fitness_level=input('Upiši nivo spremnosti (jun/med/sen): ')
        self.ntorka = (self.id, self.first_name, self.second_name, self.gender,self.age, self.fitness_level)
        save = input('-----------------------------------------\n'
                     'Da li želite sačuvati novog korisnika (Y/N): ')
        if save == 'Y':
            conn = sqlite3.connect('database2.db')
            crsr = conn.cursor()
            crsr.execute('INSERT INTO customers VALUES (?,?,?,?,?,?)', self.ntorka)
            conn.commit()
        else:
            pass

class Trainer_create(Person):
    def __init__(self):
        Person.__init__(self)
        self.seniority=input('Upiši nivo trenerskog senioriteta (jun/med/sen): ')
        self.ntorka = (self.id, self.first_name, self.second_name, self.gender, self.age, self.seniority)
        save = input('-----------------------------------------\n'
                     'Da li želite sačuvati novog trenera (Y/N): ')
        if save == 'Y':
            conn = sqlite3.connect('database2.db')
            crsr = conn.cursor()
            crsr.execute('INSERT INTO trainers VALUES (?,?,?,?,?,?)', self.ntorka)
            conn.commit()
        else:
            pass
class Equipment_create:
    def __init__(self):
        self.eq_id=int(input('Upiši ID opreme: '))
        self.name=input('Upiši naziv opreme: ')
        self.manufacturer=input('Upiši naziv proizvođača opreme: ')
        self.type=input('Upiši vrstu opreme: ')
        self.weight=input('Upiši težinu/masu opreme: ')
        self.color=input('Upiši boju opreme: ')
        self.ntorka=(self.eq_id, self.name, self.manufacturer, self.type, self.weight, self.color)
        save = input('-----------------------------------------\n'
                     'Da li želite sačuvati novu opremu (Y/N): ')
        if save == 'Y':
            conn = sqlite3.connect('database2.db')
            crsr = conn.cursor()
            crsr.execute('INSERT INTO equipment VALUES (?,?,?,?,?,?)', self.ntorka)
            conn.commit()
        else:
            pass

class Suplementation_create:
    def __init__(self):
        self.sup_id = int(input('Upiši ID proizvoda: '))
        self.name = input('Upiši naziv proizvoda: ')
        self.manufacturer = input('Upiši naziv proizvođača proizvoda: ')
        self.type = input('Upiši vrstu proizvoda: ')
        self.weight = input('Upiši težinu/masu proizvoda: ')
        self.cal = input('Upiši kalorijsku vrijednost na 100g: ')
        self.ntorka = (self.sup_id, self.name, self.manufacturer, self.type, self.weight, self.cal)
        save = input('-----------------------------------------\n'
                     'Da li želite sačuvati novi proizvod (Y/N): ')
        if save == 'Y':
            conn = sqlite3.connect('database2.db')
            crsr = conn.cursor()
            crsr.execute('INSERT INTO food_supplement VALUES (?,?,?,?,?,?)', self.ntorka)
            conn.commit()
        else:
            pass

def trainer_read(conn):
    crsr=conn.cursor()
    crsr.execute('SELECT * FROM trainers;')
    ans= crsr.fetchall()
    for i in ans:
        print(i)

def customer_read(conn):
    crsr=conn.cursor()
    crsr.execute('SELECT * FROM customers;')
    ans= crsr.fetchall()
    for i in ans:
        print(i)

def equipment_read(conn):
    crsr=conn.cursor()
    crsr.execute('SELECT * FROM equipment;')
    ans= crsr.fetchall()
    for i in ans:
        print(i)

def supplement_read(conn):
    crsr=conn.cursor()
    crsr.execute('SELECT * FROM food_supplement;')
    ans= crsr.fetchall()
    for i in ans:
        print(i)

def trainer_update(conn):
    trainer_read(conn)
    id=int(input('Unesite ID osobe koju želite ažurirati: '))
    ime=input('Upišite novo ime: ')
    prezime=input('Upišite novo prezime: ')
    try:
        crsr = conn.cursor()
        crsr.execute('UPDATE trainers SET first_name = ?, second_name = ? WHERE trainer_id = ?',(ime, prezime, id))
        conn.commit()
    except Error as e:
        print(e)


def customer_update(conn):
    customer_read(conn)
    id = int(input('Unesite ID osobe koju želite ažurirati: '))
    ime = input('Upišite novo ime: ')
    prezime = input('Upišite novo prezime: ')
    try:
        crsr = conn.cursor()
        crsr.execute('UPDATE customers SET first_name = ?, second_name = ? WHERE customer_id = ?', (ime, prezime, id))
        conn.commit()
    except Error as e:
        print(e)

def equipment_update(conn):
    equipment_read(conn)
    id = int(input('Unesite ID opreme koju želite ažurirati: '))
    ime = input('Upišite novi naziv opreme: ')
    proizvodjac = input('Upišite novog proizvođača: ')
    try:
        crsr = conn.cursor()
        crsr.execute('UPDATE equipment SET eq_name = ?, manufacturer = ? WHERE eq_id = ?', (ime, proizvodjac, id))
        conn.commit()
    except Error as e:
        print(e)

def supplement_update(conn):
    supplement_read(conn)
    id = int(input('Unesite ID proizvoda koji želite ažurirati: '))
    ime = input('Upišite novi naziv proizvoda: ')
    proizvodjac = input('Upišite novog proizvođača: ')
    try:
        crsr = conn.cursor()
        crsr.execute('UPDATE food_supplement SET sup_name = ?, manufacturer = ? WHERE sup_id = ?', (ime, proizvodjac, id))
        conn.commit()
    except Error as e:
        print(e)

def trainer_delete(conn):
    trainer_read(conn)
    id=int(input('Upiši ID osobe koju želiš izbrisati: '))
    try:
        crsr=conn.cursor()
        crsr.execute('DELETE FROM trainers WHERE trainer_id = ?',(id,))
        conn.commit()
    except Error as e:
        print(e)

def customer_delete(conn):
    customer_read(conn)
    id = int(input('Upiši ID osobe koju želiš izbrisati: '))
    try:
        crsr = conn.cursor()
        crsr.execute('DELETE FROM customers WHERE customer_id = ?', (id,))
        conn.commit()
    except Error as e:
        print(e)

def equipment_delete(conn):
    equipment_read(conn)
    id = int(input('Upiši ID opreme koju želiš izbrisati: '))
    try:
        crsr = conn.cursor()
        crsr.execute('DELETE FROM equipment WHERE eq_id = ?', (id,))
        conn.commit()
    except Error as e:
        print(e)

def supplement_delete(conn):
    supplement_read(conn)
    id = int(input('Upiši ID proizvoda koji želiš izbrisati: '))
    try:
        crsr = conn.cursor()
        crsr.execute('DELETE FROM food_supplement WHERE sup_id = ?', (id,))
        conn.commit()
    except Error as e:
        print(e)


conn.close()

