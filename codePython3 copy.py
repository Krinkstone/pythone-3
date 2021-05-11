import os
os.system("cls")

productenlijst = {"appel": 155, "peer": 120, "appelsap": 299, "bier": 4250, "lolly": 99999}

def productlijst(productenlijst):
    for key, value in productenlijst.items():
        print(key, value)

def overzicht(productenlijst):
    productlijst(productenlijst)

def toevoegen(productenlijst):
    product = input("Welk product wilt u tovoegen? ")
    prijs = input("Hoe duur is het product? ")
    productenlijst[product] = int(prijs)
    productlijst(productenlijst)

def aanpassen(productenlijst):
    productlijst(productenlijst)
    producta = input("Welk product wilt u aanpassen? ")
    prijsa = input("Hoe duur word het product? ")
    productenlijst[producta] = prijsa
    productlijst(productenlijst)

def verwijderen(productenlijst):
    productlijst(productenlijst)
    productape = input("Welk product wilt u verwijderen? ")
    del productenlijst[productape]
    productlijst(productenlijst)

def boodschappen(productenlijst):
    prijstotaal = 0
    vraag = input("Wilt u iets gaan kopen? ")
    question = vraag.lower()
    while question != "nee":
        if question == "ja":
            productlijst(productenlijst)
            productain = str(input("welk product wilt u kopen? "))
            prijstotaal += int(productenlijst[productain])
            print(prijstotaal)
        elif question == "nee":
            boodschappenprijs = str(boodschappenprijs)
            print("De prijs van uw boodschappen is: €" + boodschappenprijs + ".")
            return prijstotaal
        else:
            print("Fout, probeer iets anders! ")
        vraag = input("Wil je iets gaan kopen? ")
        question = vraag.lower()

def main():
    print("")
    print("Wat wilt u doen?")
    print("O = onze producten")
    print("T = toevoegen")
    print("A = aanpassen")
    print("V = verwijderen")
    print("B = boodschappen doen")
    print("S = stoppen")
    input_ = input("")
    letter = input_.lower()
    while letter != "s":
        if letter == "o":
            overzicht(productenlijst)
        elif letter == "t":
            toevoegen(productenlijst)
        elif letter == "a":
            aanpassen(productenlijst)
        elif letter == "v":
            verwijderen(productenlijst)
        elif letter == "b":
            boodschappen(productenlijst)
        else:
            print("")
            print("Fout, probeer iets anders. ")
        print("")
        print("wat wilt u doen?")
        print("O = onze producten")
        print("T = toevoegen")
        print("A = aanpassen")
        print("V = verwijderen")
        print("B = boodschappen doen")
        print("S = stoppen")
        input_ = input("")
        letter = input_.lower()

main()