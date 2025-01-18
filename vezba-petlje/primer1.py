import time
pocetna_pozicija = 0
cilj = 100
trenutna_pozicija = 0
<<<<<<< HEAD
brzina = 20
for x in range(10):
=======
brzina = 10
for x in range(20):
>>>>>>> 9be09a1781f187d72089732f465cb27cd41aa222
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("stigao do cilja")
        break
    elif trenutna_pozicija > cilj:
        print("Prosli ste") 
    elif trenutna_pozicija < cilj:
        print("niste jos stigli")
    trenutna_pozicija += brzina 
