##browser stuff#



## random stuff##
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
timeout = 30

##functions needed ##


def writeToCsv(nameOfInfo, list):
    with open(r"C:\csvfiles\{nameOfInfo}.csv".format(nameOfInfo = nameOfInfo), "w", newline ="") as csvFile:
        writeInfoToCsv = csv.writer(csvFile, delimiter=",")
        writeInfoToCsv.writerow(list)

class getElementToCsv():
    def __init__(self, name, element,):
        self.name = name
        self.element = element
        self.elementList = elementSearch(self.name, self.element)

##secure info##
password = "Chunks2!"
username = "502045721"
