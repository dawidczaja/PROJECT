import pymysql
import os

class Configuration:

    def __init__(self, nazwa_pliku, host, user, haslo, baza):
        self.nazwa_pliku = nazwa_pliku
        self.__create_config(host, user, haslo, baza)
    def __create_config(self, host, user, haslo, baza):

        if(not os.path.isfile('./' + self.nazwa_pliku + ".txt")):
            self.file = open(self.nazwa_pliku + ".txt", 'w')
            config_list = [host + "\n", user + "\n", haslo + "\n", baza + "\n"]
            self.file.writelines(config_list)
            self.file.close()

    def read_data(self):

        file = open(self.nazwa_pliku + ".txt", "r")
        data = []
        for line in file.read().splitlines():
            data.append(line)

        dictionary = {}

        dictionary["host"] = data[0]
        dictionary["user"] = data[1]
        dictionary["password"] = data[2]
        dictionary["baza"] = data[3]

        return dictionary


c = Configuration("config", "localhost", "root", "Dartmoor.77", "tariff")
print(c.read_data())

class DBConnect():

    def __init__(self, config):

        try:

            data = config.read_data()

            #conn = pymysql.connect(host='127.0.0.1', port='3306', user='root', pasword=, db='pymysql', charset="utf8")"""autocommit=True"""
            self.conn = pymysql.connect(data["host"], data['user'], data['password'], data['baza'], charset="utf8")
            self.logowanie()
            self.conn.close()

        except pymysql.MySQLError:
            print("bledne dane polaczenia")

    def logowanie(self):

        login = input("login")
        haslo = input("haslo")

        self.kursor = self.conn.cursor()

        self.kursor.execute("select * from logowanie where login = %s and password=%s", (login, haslo))
        #pobierz wyniki z zapytania select do zmiennej results
        results = self.kursor.fetchall()

        print(results)

        if (len(results)) == 1:

            print("zalogowano")
            self.menu()

        else:
            print("niepoprawny login i lub haslo")
            self.logowanie()
    def menu(self):

        while (True):

            dec = input("S - show, Q - exit").upper()

            if (dec == "S"):
                self.select()

            if (dec == "Q"):
                exit()

    def select(self):

        self.kursor.execute("select * from chapter_73")
        chapter_73 = self.kursor.fetchall()
        print(" | %3s | | %-12s | | %9s | | %10s | | %5s | | %-360s |" % (
        'id', 'HTS_code', 'left_mark', 'right_mark', 'depth', 'title'))

        i=1
        for row in chapter_73:

            ID = 0
            LEFT_MARK = 1
            RIGHT_MARK = 2
            DEPTH = 3
            HTS_CODE = 4
            TITLE = 5
            print(" | %3i | | %-12s | | %9i | | %10i | | %5i | | %-360s |" % (row[ID], row[LEFT_MARK], row[RIGHT_MARK], row[DEPTH], row[HTS_CODE], row[TITLE]))
            i+=1

db = DBConnect(c)












