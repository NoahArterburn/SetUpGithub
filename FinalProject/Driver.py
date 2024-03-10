from Book import Book
from Catalogue import Catalogue
from ProrityJ import PriorityQueue
import os

if __name__ == "__main__":
    ABW = Book("Ascendance of a Bookworm")
    TWM = Book("The Water Magician")
    MM = Book("Making Magic")
    HM = Book("Hell Mode")
    OOO = Book("Overpowered, Oversummoned, and Over It!")
    DDEB = Book("Death's Daughter and the Ebony Blade")

    JC = Catalogue()
    TranslationQueue = PriorityQueue(JC)
    JC.addBook(ABW)
    JC.addBook(TWM)
    JC.addBook(MM)
    JC.addBook(HM)
    JC.addBook(OOO)
    JC.addBook(DDEB)
    JC.printC()
    print("")
    os.system("pause")

    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    TranslationQueue.translate(100)
    TranslationQueue.translate(35)
    TranslationQueue.translate(20)
    TranslationQueue.translate(40)
    TranslationQueue.translate(50)
    TranslationQueue.translate(99)
    print("")
    os.system("pause")

    TranslationQueue.enqueueAll()
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    print("")
    os.system("pause")

    JC.printC()
    print("")
    os.system("pause")
    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    os.system("pause")
    print(TranslationQueue.peek())
    print("")
    os.system("pause")
    TranslationQueue.translate(20)
    TranslationQueue.translate(-70)
    TranslationQueue.translate(10)
    print("")
    os.system("pause")

    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    os.system("pause")

    JC.printC()
    print("")
    os.system("pause")

    ID = Book("Infinite Dendrogram")
    RS = Book("Reincarnated as a Sword")
    A = Book("Arifureta")
    UUA = Book("The Unwanted Undead Adventurer")
    RWW = Book("Record of Wortenia War")
    JC.addBook(ID)
    JC.addBook(RS)
    JC.addBook(A)
    JC.addBook(UUA)
    JC.addBook(RWW)
    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    os.system("pause")

    TranslationQueue.translate(0)
    TranslationQueue.translate(-30)
    TranslationQueue.translate(100)
    TranslationQueue.translate(40)
    TranslationQueue.translate(60)
    TranslationQueue.translate(50)
    print("")
    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    os.system("pause")

    TranslationQueue.translate(0)
    TranslationQueue.translate(10)
    TranslationQueue.translate(30)
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    TranslationQueue.translate(0)
    TranslationQueue.translate(20)
    TranslationQueue.translate(10)
    TranslationQueue.translate(0)
    TranslationQueue.translate(50)
    TranslationQueue.translate(30)
    print("")
    JC.printC()
    print("")
    os.system("pause")

    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    TranslationQueue.translate(-5)
    TranslationQueue.translate(15)
    TranslationQueue.translate(10)
    TranslationQueue.translate(-5)
    TranslationQueue.translate(30)
    TranslationQueue.translate(-20)
    print("")
    os.system("pause")

    OOO.completed()
    TranslationQueue.enqueueAll()
    print(TranslationQueue.print_queue())
    os.system("pause")
    JC.printC()
