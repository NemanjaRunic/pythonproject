from classes_and_functions import *
import sqlite3
from sqlite3 import Error

try:
      conn=sqlite3.connect('database2.db')
      print('\nxx Uspješno ste se konektovali na bazu xx\n')
except Error as e:
      print('GREŠKA U KONEKCIJI: "' + str(e) + '"')




print('DOBRO DOŠLI NA APLIKACIJU GYM - BEAM!\n'
      '================================================================\n'
      'U okviru aplikacije možete upravljati spiskom korisnika GYM-a,\n'
      'spiskom trenera u GYM-u, kao i spiskom opreme za treniranje i\n'
      'određenim proizvodima za dodatke u ishrani koji pomažu u procesu\n'
      'treniranja.\n\n'
      'Za prolazak kroz aplikaciju koristite numeričke tipke, kako je\n'
      'navedeno u uputstvu koje slijedi!\n'
      '================================================================')

while True:
      print('BROJ 1 - upravljanje listom TRENERA!\n'
            'BROJ 2 - upravljanje listom KORISNIKA!\n'
            'BROJ 3 - upravljanje listom OPREME!\n'
            'BROJ 4 - upravljanje listom SUPLEMENATA!\n'
            'BROJ 0 - IZLAZAK IZ APLIKACIJE!\n'
            '__________________________________________________________')
      izbor=input('Birate opciju broj: ')
      print('__________________________________________________________')
      if izbor=='0':
            print('Hvala što ste koristili GYM - BEAM aplikaciju!')
            break
      elif izbor=='1':
            while True:
                  print('U sekciji TRENERI možete birati sledeće opcije:\n'
                        'C - dodaj novog trenera\n'
                        'R - prikaži listu postojećih trenera\n'
                        'U - ažuriraj podatke vezane za postojeće trenere\n'
                        'D - obriši trenera iz liste\n'
                        'X - izlaz iz sekcije TRENERI.\n'
                        '__________________________________________________________')
                  opcija_in=input('Za izbor akcije upiši znak sa liste: ')
                  print('__________________________________________________________')
                  opcija=opcija_in.upper()
                  if opcija=='X':
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        break
                  elif opcija=='C':
                        TrainerCreate()
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija=='R':
                        trainer_read(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija=='U':
                        trainer_update(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija=='D':
                        trainer_delete(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  else:
                        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                              'UKUCALI STE NEPOSTOJEĆU KOMANDU!\n'
                              'Upišite komandu sa liste ispod!\n'
                              '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                        pass
      elif izbor=='2':
            while True:
                  print('U sekciji KORISNICI možete birati sledeće opcije:\n'
                        'C - dodaj novog korisnika\n'
                        'R - prikaži listu postojećih korisnika\n'
                        'U - ažuriraj podatke vezane za postojeće korisnike\n'
                        'D - obriši korisnike iz liste\n'
                        'X - izlaz iz sekcije KORISNICI.\n'
                        '__________________________________________________________')
                  opcija_in = input('Za izbor akcije upiši znak sa liste: ')
                  print('__________________________________________________________')
                  opcija = opcija_in.upper()
                  if opcija == 'X':
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        break
                  elif opcija == 'C':
                        CustomerCreate()
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'R':
                        customer_read(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'U':
                        customer_update(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'D':
                        customer_delete(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  else:
                        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                              'UKUCALI STE NEPOSTOJEĆU KOMANDU!\n'
                              'Upišite komandu sa liste ispod!\n'
                              '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                        pass
      elif izbor=='3':
            while True:
                  print('U sekciji OPREMA možete birati sledeće opcije:\n'
                        'C - dodaj novu opremu\n'
                        'R - prikaži listu postojeće opreme\n'
                        'U - ažuriraj podatke vezane za postojeću opremu\n'
                        'D - obriši opremu iz liste,\n'
                        'X - izlaz iz sekcije OPREMA.\n'
                        '__________________________________________________________')
                  opcija_in = input('Za izbor akcije upiši znak sa liste: ')
                  print('__________________________________________________________')
                  opcija = opcija_in.upper()
                  if opcija == 'X':
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        break
                  elif opcija == 'C':
                        EquipmentCreate()
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'R':
                        equipment_read(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'U':
                        equipment_update(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'D':
                        equipment_delete(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  else:
                        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                              'UKUCALI STE NEPOSTOJEĆU KOMANDU!\n'
                              'Upišite komandu sa liste ispod!\n'
                              '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                        pass

      elif izbor=='4':
            while True:
                  print('U sekciji SUPLEMENTI možete birati sledeće opcije:\n'
                        'C - dodaj novi proizvod\n'
                        'R - prikaži listu postojećih proizvoda\n'
                        'U - ažuriraj podatke vezane za postojeće proizvode\n'
                        'D - obriši proizvode iz liste,\n'
                        'X - izlaz iz sekcije SUPLEMENTI.\n'
                        '__________________________________________________________')
                  opcija_in = input('Za izbor akcije upiši znak sa liste: ')
                  print('__________________________________________________________')
                  opcija = opcija_in.upper()
                  if opcija == 'X':
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        break
                  elif opcija == 'C':
                        SuplementationCreate()
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'R':
                        supplement_read(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'U':
                        supplement_update(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  elif opcija == 'D':
                        supplement_delete(conn)
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  else:
                        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                              'UKUCALI STE NEPOSTOJEĆU KOMANDU!\n'
                              'Upišite komandu sa liste ispod!\n'
                              '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                        pass

      else:
            print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
                  'UKUCALI STE NEPOSTOJEĆU KOMANDU!\n'
                  'Upišite komandu sa liste ispod!\n'
                  '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
            pass

conn.close()

