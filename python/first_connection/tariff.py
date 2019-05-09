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


c = Configuration("config", "localhost", "root", "Dartmoor.77", "crud")
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

        self.kursor.execute("select * from logowanie where login = %s and passwd=%s", (login, haslo))
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

            dec = input("S - show, I - insert, D - delete, U - update, Q - exit").upper()

            if (dec == "S"):
                self.select()

            if (dec == "I"):
                self.insert()

            if (dec == "D"):
                self.delete()

            if (dec == "U"):
                self.update()

            if (dec == "Q"):
                exit()

    def select(self):

        self.kursor.execute("select * from pracownicy")
        pracownicy = self.kursor.fetchall()

        for pracownik in pracownicy:
            print(pracownik)
        i=1
        for row in pracownicy:

            NAME = 1
            SURNAME = 2
            PESEL = 3
            DATA_UR = 4
            print(" | %3i | | %10s | | %10s | | %12s | | %7s |" % (i, row[NAME], row[SURNAME], row[PESEL], row[DATA_UR]))
            i+=1

    def insert(self):

        imie = input("imie")
        nazwisko = input("nazwisko")
        pesel = input("pesel")
        data = input("data")

        self.kursor.execute('insert into pracownicy (imie, nazwisko, pesel, data_ur) values (%s,%s,%s,%s)', (imie, nazwisko, pesel, data))
        self.conn.commit()

    def delete(self):

        self.select()
        pesel = input("pesel")
        self.kursor.execute("delete from pracownicy where pesel = %s", pesel)
        dec=input("czy napewno? T/N").upper()
        if (dec == "T"):
            self.conn.commit()
        else:
            self.conn.rollback()
            print("wracasz do gry!")

    def update(self):
        self.select()
        pesel = input("podaj pesel pracownika")
        nazwisko = input("podaj nowe nazwisko")
        self.kursor.execute("UPDATE pracownicy SET nazwisko = %s where pesel = %s", (nazwisko, pesel))
        dec = input("czy napewno? T/N").upper()
        if (dec == "T"):
            self.conn.commit()
        else:
            self.conn.rollback()
            print("nie zmieniono")


db = DBConnect(c)











