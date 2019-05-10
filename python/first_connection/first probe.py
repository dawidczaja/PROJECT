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

            dec = input("S - show whole table, C - classification, Q - exit").upper()

            if (dec == "S"):
                self.select()
            if (dec == "C"):
                self.class_1_type()
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
            print(" | %3i | | %-12s | | %9i | | %10i | | %5i | | %-360s |" % (
                row[ID], row[LEFT_MARK], row[RIGHT_MARK], row[DEPTH], row[HTS_CODE], row[TITLE]))
            i+=1

    def class_1_type(self):

        sec = input("Choose sort of part from the list: T - tube or pipe fitting; H - hose fitting. B1 - back").upper()

        if (sec == 'T'):
            self.class_2_matF()
        if (sec == 'H'):
            self.class_3_matH()
        if (sec == 'B1'):
            self.menu()

    def class_2_matF(self):

        fec = input('Choose material from the list: '
                    'CT - cast steel and cast iron; '
                    'SST - stainless steel; '
                    'ST - steel and other steel alloys; '
                    'CU - copper and its alloys; '
                    'AL - aluminium and its alloys; '
                    'B2 - back').upper()

        if (fec == 'CT'):
            bec = input('Choose material from the list: ; B - back')
        if (fec == 'SST'):
            fec4 = input()
        if (fec == 'ST'):

            self.kursor.execute("select left_mark, right_mark, depth, concat(repeat ('-', (select count(parent.id)-1 from chapter_73 as parent where node.left_mark between parent.left_mark and parent.right_mark)), node.hts_code) as hts_code, title from chapter_73 as node where node.left_mark between 91 and 215 order by node.left_mark;")
            chapter_73 = self.kursor.fetchall()
            print(" | %9s | | %10s | | %5s | | %-20s | | %-360s | " % (
                'left_mark', 'right_mark', 'depth', 'HTS_code', 'title'))

            for row in chapter_73:

                LEFT_MARK = 0
                RIGHT_MARK = 1
                DEPTH = 2
                HTS_CODE = 3
                TITLE = 4
                print(" | %9s | | %10s | | %5s | | %-20s | | %-360s |" % (
                    row[LEFT_MARK], row[RIGHT_MARK], row[DEPTH], row[HTS_CODE], row[TITLE]))

            fec1 = input(' TH - threaded, NTH - non-threaded, B3 - back').upper()

            if (fec1 == 'TH'):
                fec2 = input('E - elbows; BE - bends; SL - sleeves; OT - other; B4 - back').upper()
                if (fec2 == 'E'):
                    pass
            if (fec1 == 'NTH'):
                pass
            if (fec1 == 'B3'):
                print(fec)

        if (fec == 'CU'):
            pass

        if (fec == 'AL'):
            pass

        if (fec == 'B2'):
            pass

        if (fec == 'B2'):
            pass
            self.class_1_type()

    def class_3_matH(self):

        pec = input(
            'What material is it made of? Choose from the list: '
            'CT - cast steel and cast iron; SST - stainless steel; '
            'ST - steel and other steel alloys; C - copper and its alloys; A - aluminium and its alloys; B - back')

        if (pec == ''):
            bec = input('What material is it made of? Choose from the list: cast steel and cast iron; '
            'ST - steel and other steel alloys; C - copper and its alloys; A - aluminium and its alloys; B - back')

        if (pec == 'B'):
            self.menu()


db = DBConnect(c)












