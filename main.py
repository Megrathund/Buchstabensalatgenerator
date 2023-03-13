from random import *

validInput = False
gridWidth = "notSet"
gridHeight = "notSet"
wordTheme = "notSet"
numberOfWords = "notSet"
userDefinedGeneration = "notSet"
words = []


while (validInput != True):
    userDefinedGeneration = input("Moechten Sie Ihr Buchenstabensalat Benutzerdefiniert erstellen\noder mit den Standard-Einstellungen? [benutzerdefiniert/standard]\nIhre Antwort: ")
    if (userDefinedGeneration == "benutzerdefiniert"):
        userDefinedGeneration = "userDefined"
        validInput = True
    elif (userDefinedGeneration == "standard"):
        userDefinedGeneration = "standard"
        validInput = True
    else:
        print("Diese Angabe ist nicht gültig! Bitte waehlen Sie aus: [benutzerdefiniert/standard]\n")
        userDefinedGeneration = "notSet"

validInput = False
if (userDefinedGeneration == "userDefined"):
    while (validInput != True):
        if (gridWidth == "notSet"):
            gridWidth = input("Bitte geben Sie die Breite des Grid-Systems an: ")
            if (int(gridWidth) < 15):
                print("Die mindestbreite des Grid-System's ist unterschritten.\nBitte geben Sie eine hoehere Breite an.\n")
                gridWidth = "notSet"
            elif (int(gridWidth) > 50):
                print("Die maximalbreite des Grid-System's ist ueberschritten.\nBitte geben Sie eine geringere Breite an.\n")
                gridWidth = "notSet"

        elif (gridHeight == "notSet"):
            gridHeight = input("Bitte geben Sie die Hoehe des Grid-Systems an: ")
            if (int(gridHeight) < 15):
                print("Die mindesthoehe des Grid-System's ist unterschritten.\nBitte geben Sie eine hoehere Hoehe an.\n")
                gridHeight = "notSet"
            elif (int(gridHeight) > 50):
                print("Die maximalhoehe des Grid-System's ist ueberschritten.\nBitte geben Sie eine geringere Hoehe an.\n")
                gridHeight = "notSet"

        elif (wordTheme == "notSet"):
            wordTheme = input("Bitte geben Sie das zu verwendende Wort-Thema an: ")

            if (wordTheme == "fruit"):
                words = ["APFEL", "BIRNE", "BANANE", "KIRSCHE", "ORANGE", "KIWI", "PFLAUME", "MELONE", "PFIRSICH",
                         "TRAUBE",
                         "ANANAS", "ERDBEERE", "BROMBEERE", "HIMBEERE", "JOHANNISBEERE", "MIRABELLE", "NEKTARINE",
                         "MANDERINE",
                         "KAKI", "QUITTE"]  # The list with the words for use with theme 'fruit'.

            elif (wordTheme == "in-the-air"):
                words = ["FLUGZEUG", "VOGEL", "WOLKE", "HUBSCHRAUBER", "JET", "REGENBOGEN"]  # The list with the words for use with theme 'in-the-air'.

            elif (wordTheme == "animal"):
                words = ["KATZE", "HUND", "BIENE", "PINGUIN", "AMSEL", "LOEWE", "ELEFANT", "AFFE", "BÄR", "WOLF",
                         "TIGER", "FISCH", "PFERD", "NASHORN", "WILDSCHWEIN", "HUHN", "SCHWAN", "MÜCKE", "LIBELLE",
                         "SCHMETTERLING", "MAUS", "HIRSCH", "WURM", "MAULWURF", "STINKTIER", "RAUPE", "MEISE",
                         "ZEBRA", "WACHSMOTTE", "JAGUAR", "ANTILOPE", "KAKADU", "SCHLANGE"]  # The list with the words for use with theme 'animal'.

            elif (wordTheme == "job"):
                words = ["MALER", "SCHORNSTERINFEGER", "VERKAEUFER", "PROGRAMMIERER", "BAUARBEITER", "IMKER",
                         "HAUSMEISTER", "KAPITAEN", "FORSCHER", "JAEGER", "FOTOGRAF", "ARZT", "AUTOR", "BAHNFAHRER",
                         "SOLDAT", "WISSENSCHAFTLER", "BAUER"]


            if (wordTheme != "fruit" and wordTheme != "in-the-air" and wordTheme != "animal" and wordTheme != "job"):
                print("Dieses Wort-Thema gibt es nicht! Füge es hinzu\noder waehle aus den schon vorhandenen Wort-Themen:\n'fruit', 'in-the-air', 'animal', 'job'\n")
                wordTheme = "notSet"

        elif (numberOfWords == "notSet"):
            numberOfWords = input("Bitte geben Sie an wie viele Woerter verwendet werden sollen.\nSie koennen bis zu " + str(len(words)) + " Woerter aus dem Wort-Thema '" + wordTheme + "' " + "verwenden: ")
            if (int(numberOfWords) <= 0):
                print("Ohne Woerter kann es keinen Buchenstabensalat geben!\n")
                numberOfWords = "notSet"
            elif (int(numberOfWords) > len(words)):
                print("Sie wollen mehr Woerter verwenden als zur Verfügung stehen.\nBitte reduzieren sie die Anzahl der Woerter.\n")
                numberOfWords = "notSet"


        if (gridWidth != "notSet" and gridHeight != "notSet" and wordTheme != "notSet" and numberOfWords != "notSet"):
            validInput = True
else:
    gridWidth = 20
    gridHeight = 21
    wordTheme = "fruit"
    words = ["APFEL", "BIRNE", "BANANE", "KIRSCHE", "ORANGE", "KIWI", "PFLAUME", "MELONE", "PFIRSICH",
             "TRAUBE",
             "ANANAS", "ERDBEERE", "BROMBEERE", "HIMBEERE", "JOHANNISBEERE", "MIRABELLE", "NEKTARINE",
             "MANDERINE",
             "KAKI", "QUITTE"]
    numberOfWords = 20


gridWidth = int(gridWidth)
gridHeight = int(gridHeight)
numberOfWords = int(numberOfWords)
grid = [["0" for i in range(gridWidth)] for j in range(gridHeight)]

usedWords = []



def add_word(direction):
    freePlaces = "no"
    randomWord = "none"
    randomRow = 0
    randomField = 0
    trys_freeplaces = 0

    while (freePlaces == "no"):
        trys_freeplaces = trys_freeplaces + 1
        randomWord = words[randint(0, len(words)-1)]
        randomRow = randint(0, (len(grid)-1)-len(randomWord))
        randomField = randint(0, (len(grid[0])-1)-len(randomWord))

        trys_randomwords = 0
        while (randomWord in usedWords):
            randomWord = words[randint(0, len(words) - 1)]

            if (trys_randomwords >= len(words)*10):
                exit("FEHLER! Es gibt keine Wörter mehr die in das Kreuzworträtsel hinzugefügt werden können\n"
                     "ohne das es doppelte Wörter gibt. Reduziere entweder die Anzahl der zu generierenden Wörter\n"
                     "oder erweitere die Liste der Wörter die benutzt werden können (Listenname 'words'). (Nur im Quellcode möglich)")
            trys_randomwords = trys_randomwords + 1

        if (trys_freeplaces >= len(grid)*len(grid[0])+1000):
            exit("FEHLER! Die Wörter konnten nicht zusammengestellt werden.\n"
                 "Möglicherweise sind es zu viele Wörter.\n"
                 "Bitte reduzieren Sie die Anzahl der Wörter.")

        counterHorizontal = 0
        counterVertical = 0

        for i in range(0, len(randomWord))
            testChar = list(randomWord)[i]
            try:
                if (grid[randomRow+counterVertical][randomField+counterHorizontal] == "0"):
                    freePlaces = "yes"
                elif (grid[randomRow+counterVertical][randomField+counterHorizontal] == testChar):
                    freePlaces = "yes"
                else:
                    freePlaces = "no"
                    break
            except:
                freePlaces = "no"
                break

            if (direction == "horizontal"):
                counterHorizontal = counterHorizontal + 1
            else:
                counterVertical = counterVertical + 1


    counterHorizontal = 0
    counterVertical = 0
    usedWords.append(randomWord)

    for char in randomWord:
        grid[randomRow+counterVertical][randomField+counterHorizontal] = char
        if (direction == "horizontal"):
            counterHorizontal = counterHorizontal + 1
        else:
            counterVertical = counterVertical + 1




def generate_words(words):
    lastDirection = "vertical"

    for i in range(0, words):
        if (lastDirection == "horizontal"):
            add_word("vertical")
            lastDirection = "vertical"
        else:
            add_word("horizontal")
            lastDirection = "horizontal"



def generate_chars():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    gridRow = 0
    gridField = 0

    for i in range(0, len(grid)*len(grid[0])):
        if (grid[gridRow][gridField] == "0"):
            grid[gridRow][gridField] = chars[randint(0, len(chars)-1)]

        if (gridField == len(grid[0])-1):
            gridRow = gridRow + 1
            gridField = 0
        else:
            gridField = gridField + 1



def save_result():
    i = 0
    with open("./buchstabensalat.txt", "w", encoding="utf-8") as file:
        file.write("Die folgenden Wörter müssen gefunden werden:\n\n")
        for word in usedWords:
            file.write(" -" + word + "- ")
            i = i + 1
            if (i == 4):
                file.write("\n")
                i = 0

        file.write("\n\n")

        for line in grid:
            for field in line:
                file.write(field.strip())
            file.write("\n")

generate_words(words=numberOfWords)
generate_chars()
save_result()


print("\t\t\t\t\t\tDie folgenden Wörter müssen gefunden werden:")
print(usedWords)
print("\n")

for line in grid:
    print(line)

print("Ihr Buchstabensalat wurde erfolgreich generiert!\n"
      "Öffnen Sie nun die 'buchstabensalat.txt'-Datei und kopieren Sie das Rätsel in z.B. eine *.docx-Datei\n"
      "welche Sie nun ausdrucken können. Viel Spaß beim rätseln :)!")
