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
                self.class_c()
            if (dec == "Q"):
                exit()
            else:
                print('błędna wartośc')

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

    def class_c(self):

        while (True):

            sec = input("Choose sort of part from the list: "'\n'
                        "T - tube or pipe fitting; "'\n'
                        "H - hose fitting. "'\n'
                        "B - back").upper()
            if (sec == 'T'):
                self.class_t()
            if (sec == 'H'):
                self.class_h()
            if (sec == 'B'):
                self.menu()
            else:
                print('błędna wartośc')

    def class_t(self):

        fec = input('Choose material from the list: ' '\n' 
                    'CT  - cast steel and cast iron; ''\n'
                    'SST - stainless steel; ''\n'
                    'ST  - steel and other steel alloys; ''\n'
                    'CU  - copper and its alloys; ''\n'
                    'AL  - aluminium and its alloys; ''\n'
                    'B2  - back').upper()

        if (fec == 'CT'):
            self.class_ct()
        if (fec == 'SST'):
            self.class_sst()
        if (fec == 'ST'):
            self.class_st()
        if (fec == 'CU'):
            self.class_cu()
        if (fec == 'AL'):
            self.class_al()
        if (fec == 'B2'):
            self.class_c()

    def class_ct(self):

        fec1 = input('Choose material from the list: ''\n'
                    'NM - non-malleable cast iron; ''\n'
                    'M  - malleable cast iron; ''\n'
                    'CS - cast steel; ''\n'
                    'OT - other; ''\n'
                    'B5 - back').upper()

        if (fec1 == 'NM'):
            self.class_nm()
        if (fec1 == 'M'):
            self.class_m()
        if (fec1 == 'CS'):
            self.class_cs()
        if (fec1 == 'OT'):
            self.class_ot()
        if (fec1 == 'B5'):
            self.class_t()

    def class_sst(self):
        fec1 = input(' TH - threaded, '
                     'NTH - non-threaded, '
                     'B6 - back').upper()

        if (fec1 == 'TH'):
            self.class_sth()
        if (fec1 == 'NTH'):
            self.class_snth()
        if (fec1 == 'B3'):
            self.class_t()

    def class_st(self):

        self.kursor.execute("select left_mark, right_mark, depth, concat(repeat ('-', (select count(parent.id)-1 "
                            "from chapter_73 as parent where node.left_mark between parent.left_mark and "
                            "parent.right_mark)), node.hts_code) as hts_code, title from chapter_73 as node where "
                            "node.left_mark between 91 and 215 order by node.left_mark;")

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
            self.class_th()
        if (fec1 == 'NTH'):
            self.class_nth()
        if (fec1 == 'B3'):
            self.class_t()

    def class_cu(self):
        pass

    def class_al(self):
        pass

    def class_nm(self):
        while (True):
            fec1 = input(' PS - used in pressure systems, ''\n'
                         'NPS - not used in pressure systems, ''\n'
                         'B   - back''\n'
                         'Q   - exit').upper()

            if (fec1 == 'PS'):
                self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=5 and right_mark >=6;")

                chapter_73 = self.kursor.fetchall()

                print(" | %5s | | %-20s | | %-82s | " % (
                    'depth', 'HTS_code', 'title'))

                for row in chapter_73:
                    DEPTH = 0
                    HTS_CODE = 1
                    TITLE = 2
                    print(" | %5s | | %-20s | | %-82s |" % (
                        row[DEPTH], row[HTS_CODE], row[TITLE]))
                print(self.menu())

            if (fec1 == 'NPS'):
                self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=7 and right_mark >=8;")

                chapter_73 = self.kursor.fetchall()

                print(" | %5s | | %-20s | | %-82s | " % (
                    'depth', 'HTS_code', 'title'))

                for row in chapter_73:
                    DEPTH = 0
                    HTS_CODE = 1
                    TITLE = 2
                    print(" | %5s | | %-20s | | %-82s |" % (
                        row[DEPTH], row[HTS_CODE], row[TITLE]))
                print(self.menu())

            if (fec1 == 'B'):
                self.class_ct()

            if (fec1 == 'Q'):
                exit()
            else:
                print('bledna wartosc')

    def class_m(self):
        while (True):

            fec1 = input(' TH - threaded, ''\n'
                         'NTH - non-threaded, ''\n'
                         'ISO - bodies of compression fittings using ISO DIN 13 metric thread and circular junction '
                         'boxes without having a lid''\n'
                         'B - back''\n'
                         'Q - exit').upper()

            if (fec1 == 'TH'):
                self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=12 and right_mark >=13;")

                chapter_73 = self.kursor.fetchall()

                print(" | %5s | | %-20s | | %-82s | " % (
                    'depth', 'HTS_code', 'title'))

                for row in chapter_73:
                    DEPTH = 0
                    HTS_CODE = 1
                    TITLE = 2
                    print(" | %5s | | %-20s | | %-82s |" % (
                        row[DEPTH], row[HTS_CODE], row[TITLE]))
                print(self.menu())

            if (fec1 == 'NTH' or 'ISO'):
                self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=14 and right_mark >=15;")

                chapter_73 = self.kursor.fetchall()

                print(" | %5s | | %-20s | | %-82s | " % (
                    'depth', 'HTS_code', 'title'))

                for row in chapter_73:
                    DEPTH = 0
                    HTS_CODE = 1
                    TITLE = 2
                    print(" | %5s | | %-20s | | %-82s |" % (
                        row[DEPTH], row[HTS_CODE], row[TITLE]))
                print(self.menu())

            if (fec1 == 'B'):
                self.class_ct()

            if (fec1 == 'Q'):
                exit()
            else:
                print('bledna wartosc')


            if (fec1 == 'CS'):
                self.class_cs()
            if (fec1 == 'OT'):
                self.class_ot()

    """
        def class_th(self):
        input(' TH - threaded, NTH - non-threaded, B3 - back').upper()
    """

    def class_thdd(self):

        fec2 = input('E - elbows; BE - bends; SL - sleeves; OT - other; B4 - back').upper()
        if (fec2 == 'E'):
            self.class_e()
        if (fec2 == 'BE'):
            self.class_be()
        if (fec2 == 'SL'):
            self.class_sl()
        if (fec2 == 'OT'):
            self.class_ot()
        if (fec2 == 'B4'):
            self.class_st()

        fec2 = input('E - elbows; '
                     'BE - bends; '
                     'SL - sleeves; '
                     'OT - other; '
                     'B4 - back').upper()
        if (fec2 == 'E'):
            self.class_e()
        if (fec2 == 'BE'):
            self.class_be()
        if (fec2 == 'SL'):
            self.class_sl()
        if (fec2 == 'OT'):
            self.class_ot()
        if (fec2 == 'B4'):
            self.class_st()

    def class_h(self):

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












