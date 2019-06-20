###############################################################
#                                                             #
#           Author: https://github.com/gr0wnedhog             #
#             Recommended python version: 3.7                 #
#                                                             #
#            Mein Versuch an einem Hangman-Spiel              #
#                                                             #
#            Nur die random Bibliothek benoetigt              #
#                                                             #
###############################################################

import random

Pfad = 'wordlist.txt'
difficulty = 1.5 #Schwierigkeit, je kleiner umso schwerer & je groeßer umso leichter

def LadeListe(Pfad):
    liste = open(Pfad,'r').read().splitlines() #Wortliste laden, lesen, und nach Zeilen aufspalten
    ausgewaehlt = random.choice(liste) #Zufälliges Wort auswaehlen und in der Variable "ausgewaehlt" speichern
    #print(ausgewaehlt) #neiiiin, nicht schummeln hier ;)
    return ausgewaehlt

def HAUPTSACHE(ausgewaehlt):
    print("Der Hangman-inator hat ein Wort ausgewählt und ist bereit, dich auf die Probe zu stellen!")
    for striche in range(0,len(ausgewaehlt)): #Die Anzahl der Buchstaben wird mit "_" dargestellt
        print("_ ", end="")
    print("") #Naechste print()-Befehle haben Zeilenumbruch danach

    for zuege in range(0,round(len(ausgewaehlt)*difficulty)): #Der Spieler hat gerundet auf ganze Zahlen: ( 1.5 * {Länge des ausgewaehlten Worts} ) Zuege
        print("Du hast noch ", (round(len(ausgewaehlt)*difficulty)-zuege), " Zuege frei.")
        char = input("Bitte gib einen Buchstaben ein, den du aufdecken möchtest, oder ein Wort, um zu sehen ob es richtig ist: ")
        if len(char) == 1: #Ueberpruefen, ob der eingegebe String nur 1 Buchstabe ist
            for zaehler in range(0,len(ausgewaehlt)):
                if char == ausgewaehlt[zaehler].lower(): #Ueberpruefen, ob der eingegebe String im Wort vorkommt
                    print("Der Buchstabe ", char, " kommt an Stelle", (zaehler+1))

        elif len(char) > 1 and char.lower() != ausgewaehlt.lower(): #Ueberpruefen, ob der eingegebe String laenger als 1 ist, und nicht das gesuchte Wort ist
            print("Das Wort, das du eingegeben hast, stimmt nicht ueberein :(")

        elif char.lower() == ausgewaehlt.lower(): #Ueberpruefen, ob der eingegebe String das gesuchte Wort ist
            print("Herzlichen Glückwunsch, du hast das richtige Wort erraten!")
            break #der break-Befehl, weil das Ergebnis bereits vorhanden ist.
    print("Leider kein Versuch mehr!")
    print("Das Wort war: ", ausgewaehlt)
    input("Druecke ENTER um zu beenden.")

HAUPTSACHE(LadeListe(Pfad))
