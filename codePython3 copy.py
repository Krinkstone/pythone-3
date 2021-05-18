import os
os.system("cls")

def contactlijst(contacten):
    for key, value in contacten.items():
        print(key, value)

def overzicht(contacten):
    contactlijst(contacten)

def toevoegen(contacten):
    nieuw_contact = input("Hoe heet het contact dat u wil toevoegen? ")
    telefoonnummer = input("Wat is het telefoonnummer van dit contact? ")
    contacten[nieuw_contact] = int(telefoonnummer)
    contactlijst(contacten)
    return contacten

def aanpassen(contacten):
    contactlijst(contacten)
    contact_aanpassen = input("Welk Contact wilt u aanpassen? ")
    nieuw_telefoonnummer = input("Wat wordt het nieuwe telefoonnummer van dit contact? ")
    contacten[contact_aanpassen] = nieuw_telefoonnummer
    contactlijst(contacten)
    return contacten

def verwijderen(contacten):
    contactlijst(contacten)
    verwijder_contact = input("Welk contact wilt u verwijderen? ")
    del contacten[verwijder_contact]
    contactlijst(contacten)
    return contacten

def aantal_contacten(contacten):
    print(contacten)

def menu():
    print("")
    print("Wat wilt u doen?")
    print("O = Overzicht Contacten")
    print("T = Contact Toevoegen")
    print("A = Contact Aanpassen")
    print("V = Contact Verwijderen")
    print("S = stoppen")
    print("")

def main():
    contacten = {"Jan Jannes": 878971387 ,"Henk Hark": 489573948, "Piet Pientje": 324684888, "Barend Binck": 234987427, "Anne Annelotte": 324864823}
    menu()
    input_ = input("")
    letter = input_.lower()
    while letter != "s":
        if letter == "o":
            overzicht(contacten)
        elif letter == "t":
            contacten = toevoegen(contacten)
        elif letter == "a":
            contacten = aanpassen(contacten)
        elif letter == "v":
            contacten = verwijderen(contacten)
        else:
            print("")
            print("Fout, probeer iets anders. ")
        menu()
        input_ = input("")
        letter = input_.lower()

main()
