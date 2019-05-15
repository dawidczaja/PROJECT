import pymysql
import os


class Configuration:

    def __init__(self, nazwa_pliku, host, user, haslo, baza):
        self.nazwa_pliku = nazwa_pliku
        self.__create_config(host, user, haslo, baza)

    def __create_config(self, host, user, haslo, baza):

        if (not os.path.isfile('./' + self.nazwa_pliku + ".txt")):
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

        self.kursor = self.conn.cursor()

        print("zalogowano")
        self.menu()

    def menu(self):

        while (True):

            dec = input("S - show whole table,"'\n'
                        "C - classification, "'\n'
                        'A - add' '\n'
                        'D - delete''\n'
                        'U - update''\n'
                        "Q - exit").upper()

            if (dec == "S"):
                self.select()
            if (dec == "C"):
                self.class_c()
            if (dec == "A"):
                self.add()
            if (dec == "D"):
                self.delete()
            if (dec == "U"):
                self.update()
            if (dec == "Q"):
                exit()
            else:
                print('błędna wartośc')

    def select(self):

        self.kursor.execute("select * from chapter_73")
        chapter_73 = self.kursor.fetchall()
        print(" | %3s | | %-12s | | %9s | | %10s | | %5s | | %-360s |" % (
            'id', 'HTS_code', 'left_mark', 'right_mark', 'depth', 'title'))

        i = 1
        for row in chapter_73:
            ID = 0
            LEFT_MARK = 1
            RIGHT_MARK = 2
            DEPTH = 3
            HTS_CODE = 4
            TITLE = 5
            print(" | %3i | | %-12s | | %9i | | %10i | | %5i | | %-360s |" % (
                row[ID], row[LEFT_MARK], row[RIGHT_MARK], row[DEPTH], row[HTS_CODE], row[TITLE]))
            i += 1

    def class_c(self):

        sec = input("Choose sort of part from the list: "'\n'
                    '\n'
                    "T - tube or pipe fitting; "'\n'
                    "B - back").upper()
        if (sec == 'T'):
            self.class_t()
        if (sec == 'B'):
            self.menu()
        else:
            print('błędna wartośc')
            print(self.class_c())

    def class_t(self):

        fec = input('Choose material from the list: ' '\n'
                '\n''CT  - cast steel and cast iron; ''\n'
                    'SST - stainless steel; ''\n'
                    'OS  - steel and other steel alloys; ''\n'
                #'AL  - aluminium and its alloys; ''\n'
                     'B  - back').upper()

        if (fec == 'CT'):
            self.class_ct()
        if (fec == 'SST'):
            self.class_sst()
        if (fec == 'OS'):
            self.class_st()
        if (fec == 'AL'):
            self.class_al()
        if (fec == 'B'):
            self.class_c()
        else:
            print('błędna wartośc')
            print(self.class_t())

    def class_ct(self):

        fec1 = input('Choose material from the list: ''\n'
                 '\n''NM - non-malleable cast iron [including gray iron]; ''\n'
                     'M  - malleable cast iron [including white iron]; ''\n'
                     'D  - ductile cast iron [spheroidal graphite cast iron]; ''\n'
                     'CS - cast steel; ''\n'
                     'OT - other; ''\n'
                     'B  - back').upper()

        if (fec1 == 'NM'):
            self.class_nm()
        if (fec1 == 'M'):
            self.class_m()
        if (fec1 == 'D'):
            self.class_d()
        if (fec1 == 'CS'):
            self.class_cs()
        if (fec1 == 'OT'):
            self.class_ot()
        if (fec1 == 'B'):
            self.class_t()
        else:
            print('błędna wartośc')
            print(self.class_ct())

    def class_sst(self):

        vec = input(' TH - threaded''\n'
                    'NTH - non-threaded''\n'
                    'B   - back''\n'
                    'Q   - exit').upper()

        if (vec == 'TH'):
            self.class_th()
        if (vec == 'NTH'):
            self.class_sth()
        if (vec == 'B'):
            self.class_t()
        else:
            print('błędna wartośc')
            print(self.class_sst())

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

        fec3 = input(' TH - threaded, NTH - non-threaded, B3 - back').upper()

        if (fec3 == 'TH'):
            self.class_ssth()
        if (fec3 == 'NTH'):
            self.class_ssnth()
        if (fec3 == 'B3'):
            self.class_t()
        else:
            print('błędna wartośc')
            print(self.class_st())

    def class_al(self):
        pass

    def class_nm(self):

        fec2 = input(' PS - used in pressure systems, ''\n'
                     'NPS - not used in pressure systems, ''\n'
                     'B   - back''\n'
                     'Q   - exit').upper()

        if (fec2 == 'PS'):
            self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                " where left_mark <=5 and right_mark >=6;")
            print(self.results())

        if (fec2 == 'NPS'):
            self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                " where left_mark <=7 and right_mark >=8;")
            print(self.results())

        if (fec2 == 'B'):
            self.class_ct()

        if (fec2 == 'Q'):
            exit()
        else:
            print('błędna wartośc')
            print(self.class_nm())

    def class_m(self):
        fec4 = input(' TH - threaded, ''\n'
                     'NTH - non-threaded, ''\n'
                     'ISO - bodies of compression fittings using ISO DIN 13 metric thread and circular junction '
                            'boxes without having a lid''\n'
                     '  B - back''\n'
                     '  Q - exit').upper()

        if (fec4 == 'TH'):
            self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title "
                                "from chapter_73 where left_mark <=12 and right_mark >=13;")

            print(self.results())

        if (fec4 == 'NTH' or 'ISO'):
            self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title "
                                "from chapter_73 where left_mark <=14 and right_mark >=15;")

            print(self.results())

        if (fec4 == 'B'):
            self.class_ct()

        if (fec4 == 'Q'):
            exit()
        else:
            print('błędna wartośc')
            print(self.class_m())

    def class_d(self):

        fec5 = input('ISO - threaded bodies of compression fittings using ISO DIN 13 metric thread''\n'
                     'TH  - other threaded''\n'
                     'NTH - non-threaded, ''\n'
                     'BB  - back''\n'
                     'Q   - exit').upper()

        if (fec5 == 'TH'):
            self.kursor.execute("select depth, concat(repeat('-', depth), hts_code) as hts_code, title "
                                "from chapter_73 where left_mark <=18 and right_mark >=19;")

            print(self.results())

        if (fec5 == 'NTH' or 'ISO'):
            print(self.class_ot())

        if (fec5 == 'BB'):
            print(self.class_t())

        if (fec5 == 'Q'):
            exit()
        else:
            print('błędna wartośc')
            print(self.class_d())

    def class_cs(self):

        print(self.class_ot())

    def class_ot(self):

        self.kursor.execute(
            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
            " where left_mark <=20 and right_mark >=21;")

        print(self.results())

    def class_th(self):
        fec6 = input('E  - elbows; ''\n'
                     'NB - bends; ''\n'
                     'SL - sleeves; ''\n'
                     'OT - other; ''\n'
                     'B  - back''\n'
                     'Q  - exit').upper()
        if (fec6 == 'E' or 'NB'):
            self.class_ebe()
        if (fec6 == 'SL'):
            self.class_sl()
        if (fec6 == 'OT'):
            self.class_ott()
        if (fec6 == 'B'):
            self.class_sst()
        if (fec6 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_th())

    def class_ebe(self):

        fec7 = input('A - For use in certain types of aircraft '
                     'OT - other; '
                     'B4 - back'
                     'Q - exit').upper()
        if (fec7 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=40 and right_mark >=41;")

            print(self.results())
        if (fec7 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=42 and right_mark >=43;")

            print(self.results())

        if (fec7 == 'B4'):
            self.class_th()
        if (fec7 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_ebe())

    def class_sl(self):

        fec8 = input('A - For use in certain types of aircraft ''\n'
                     'OT - other; ''\n'
                     'B4 - back''\n'
                     'Q - exit').upper()
        if (fec8 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=34 and right_mark >=35;")

            print(self.results())
        if (fec8 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=36 and right_mark >=37;")

            print(self.results())

        if (fec8 == 'B4'):
            self.class_th()
        if (fec8 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_sl())

    def class_ott(self):

        fec9 = input('A - For use in certain types of aircraft '
                     'OT - other; '
                     'B4 - back'
                     'Q - exit').upper()
        if (fec9 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=78 and right_mark >=79;")

            print(self.results())
        if (fec9 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=80 and right_mark >=81;")

            print(self.results())

        if (fec9 == 'B4'):
            self.class_th()
        if (fec9 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_ott())

    def class_sth(self):
        fec01 = input('F  - flanges; ''\n'
                      'TB - butt welding fittings''\n'
                      'OT - other; ''\n'
                      'B  - back''\n'
                      'Q  - exit').upper()
        if (fec01 == 'F'):
            self.class_f()
        if (fec01 == 'TB'):
            self.class_bt()
        if (fec01 == 'OT'):
            self.class_oot()
        if (fec01 == 'B'):
            self.class_sst()
        if (fec01 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_sth())

    def class_f(self):

        fec11 = input('A - For use in certain types of aircraft ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q - exit').upper()
        if (fec11 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=27 and right_mark >=28;")

            print(self.results())
        if (fec11 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=29 and right_mark >=30;")

            print(self.results())
        if (fec11 == 'B4'):
            self.class_sst()
        if (fec11 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_f())

    def class_oot(self):

        fec12 = input('A  - For use in certain types of aircraft ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q  - exit').upper()
        if (fec12 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=84 and right_mark >=85;")

            print(self.results())
        if (fec12 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=86 and right_mark >=87;")

            print(self.results())

        if (fec12 == 'B4'):
            self.class_sst()
        if (fec12 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_oot())

    def class_bt(self):
        fec02 = input('EE - elbows; ''\n'
                      'NB - bends; ''\n'
                      'OT - other; ''\n'
                      'B  - back''\n'
                      'Q  - exit').upper()
        if (fec02 == 'EE' or 'NB'):
            self.class_ee()
        if (fec02 == 'OT'):
            self.class_to()
        if (fec02 == 'B'):
            self.class_sth()
        if (fec02 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_bt())

    def class_ee(self):
        fec03 = input('AU - Of austenitic stainless steel grades, corresponding to AISI types 304, 304L, 316, 316L,''\n'
                           ' 316Ti, 321 and 321H and their equivalent in the other norms, with a greatest external ''\n'
                           'diameter not exceeding 406.4 mm and a wall thickness of 16 mm or less, with a roughness ''\n'
                           'average (Ra) of the internal surface not less than 0.8 micrometres, not flanged, ''\n'
                           'whether or not finished; ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q  - exit').upper()
        if (fec03 == 'AU'):
            self.class_au()
        if (fec03 == 'OT'):
            self.class_too()
        if (fec03 == 'B4'):
            self.class_sth()
        if (fec03 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_ee())

    def class_au(self):

        fec04 = input('A  - For use in certain types of aircraft ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q  - exit').upper()
        if (fec04 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=49 and right_mark >=50;")

            print(self.results())
        if (fec04 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=51 and right_mark >=52;")

            print(self.results())

        if (fec04 == 'B4'):
            self.class_sth()
        if (fec04 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_au())

    def class_too(self):
        fec05 = input('A - For use in certain types of aircraft ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q - exit').upper()
        if (fec05 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=55 and right_mark >=56;")
            print(self.results())
        if (fec05 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=57 and right_mark >=58;")
            print(self.results())
        if (fec05 == 'B4'):
            self.class_sth()
        if (fec05 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_too())

    def class_to(self):
        fec06 = input('AU - Of austenitic stainless steel grades, corresponding to AISI types 304, 304L, 316, 316L,''\n'
                           ' 316Ti, 321 and 321H and their equivalent in the other norms, with a greatest external ''\n'
                           'diameter not exceeding 406.4 mm and a wall thickness of 16 mm or less, with a roughness ''\n'
                           'average (Ra) of the internal surface not less than 0.8 micrometres, not flanged, ''\n'
                           'whether or not finished; ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q - exit').upper()
        if (fec06 == 'AU'):
            self.class_ua()
        if (fec06 == 'OT'):
            self.class_toto()
        if (fec06 == 'B4'):
            self.class_sth()
        if (fec06 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_to())

    def class_ua(self):

        fec07 = input('A  - For use in certain types of aircraft ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q  - exit').upper()
        if (fec07 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=49 and right_mark >=50;")

            print(self.results())
        if (fec07 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=51 and right_mark >=52;")

            print(self.results())
        if (fec07 == 'B4'):
            self.class_sth()
        if (fec07 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_ua())

    def class_toto(self):

        fec08 = input('A  - For use in certain types of aircraft ''\n'
                      'OT - other; ''\n'
                      'B4 - back''\n'
                      'Q  - exit').upper()
        if (fec08 == 'A'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=55 and right_mark >=56;")

            print(self.results())
        if (fec08 == 'OT'):
            self.kursor.execute(
                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                " where left_mark <=57 and right_mark >=58;")

            print(self.results())
        if (fec08 == 'B4'):
            self.class_to()
        if (fec08 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_toto())

    def class_ssth(self):

        fec22 = input('E - elbows; '
                     'BE - bends; '
                     'SL - sleeves; '
                     'OT - other; '
                     'B4 - back').upper()
        if (fec22 == 'E' or 'BE'):

            fec08 = input('A - For use in certain types of aircraft ''\n'
                          'OT - other; ''\n'
                          'B4 - back''\n'
                          'Q - exit').upper()
            if (fec08 == 'A'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=55 and right_mark >=56;")

                print(self.results())
            if (fec08 == 'OT'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=57 and right_mark >=58;")

                print(self.results())
            if (fec08 == 'B4'):
                self.class_to()
            if (fec08 == 'Q'):
                exit()
            else:
                print('zła wartosc')
                print(self.class_ssth())

        if (fec22 == 'SL'):

            fec08 = input('A - For use in certain types of aircraft ''\n'
                          'OT - other; ''\n'
                          'B4 - back''\n'
                          'Q - exit').upper()
            if (fec08 == 'A'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=55 and right_mark >=56;")

                print(self.results())
            if (fec08 == 'OT'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=57 and right_mark >=58;")

                print(self.results())
            if (fec08 == 'B4'):
                self.class_to()
            if (fec08 == 'Q'):
                exit()
            else:
                print('zła wartosc')
                print(self.class_ssth())

        if (fec22 == 'OT'):

            fec8 = input('A - For use in certain types of aircraft ''\n'
                         'OT - other; ''\n'
                         'B4 - back''\n'
                         'Q - exit').upper()
            if (fec8 == 'A'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=55 and right_mark >=56;")

                print(self.results())
            if (fec8 == 'OT'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=57 and right_mark >=58;")

                print(self.results())
            if (fec8 == 'B4'):
                self.class_to()
            if (fec8 == 'Q'):
                exit()
            else:
                print('zła wartosc')
                print(self.class_ot())
        if (fec22 == 'B4'):
            self.class_st()
        if (fec22 == 'Q'):
            exit()
        else:
            print('zła wartosc')
            print(self.class_ssth())

    def class_ssnth(self):

        fec2 = input('FL - flanges; ''\n'
                     'TT - butt welding fitting; ''\n'
                     'OT - other; ''\n'
                     'B4 - back').upper()
        if (fec2 == 'FL'):

            fec8 = input('A  - For use in certain types of aircraft ''\n'
                         'OT - other; ''\n'
                         'B4 - back''\n'
                         'Q  - exit').upper()
            if (fec8 == 'A'):
                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=93 and right_mark >=94;")

                print(self.results())
            if (fec8 == 'OT'):

                self.kursor.execute(
                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                    " where left_mark <=95 and right_mark >=96;")

                print(self.results())

            if (fec8 == 'Q'):
                exit()


        if (fec2 == 'TT'):
                fec92 = input('A - With greatest external diameter not exceeding 609,6 mm ''\n'
                             'OT - With greatest external diameter exceeding 609,6 mm ''\n'
                             'B4 - back''\n'
                             'Q  - exit').upper()
                if (fec92 == 'A'):
                    fec93 = input('A  - elbows and bends ''\n'
                                  'OT - other; ''\n'
                                  'B4 - back''\n'
                                  'Q  - exit').upper()
                    if (fec93 == 'A'):
                        fec94 = input('A - For use in certain types of aircraft ''\n'
                                     'OT - other; ''\n'
                                     'B4 - back''\n'
                                     'Q  - exit').upper()
                        if (fec94 == 'A'):
                            fec95 = input('TI - Consigned from Taiwan, Indonesia, Sri Lanka or the Philippines ''\n'
                                          'OT - other; ''\n'
                                          'Q  - exit').upper()
                            if (fec95 == 'TI'):
                                self.kursor.execute(
                                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=116 and right_mark >=117;")

                                print(self.results())
                            if (fec95 == 'OT'):
                                self.kursor.execute(
                                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=118 and right_mark >=119;")

                                print(self.results())
                        if (fec94 == 'OT'):
                            fec96 = input('TI - other threaded fittings ''\n'
                                          'OT - other; ''\n'
                                          'Q  - exit').upper()
                            if (fec96 == 'TI'):
                                self.kursor.execute(
                                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=122 and right_mark >=123;")

                                print(self.results())
                            if (fec96 == 'OT'):
                                fec97 = input('TI - Consigned from Taiwan ''\n'
                                              'I - Consigned from Indonesia ''\n'
                                              'S - Consigned from Sri Lanka ''\n'
                                              'P - Consigned from Philippines ''\n'
                                              'OT - other; ''\n'
                                              'Q - exit').upper()
                                if (fec97 == 'TI'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=125 and right_mark >=126;")

                                    print(self.results())
                                if (fec97 == 'I'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=127 and right_mark >=128;")

                                    print(self.results())
                                if (fec97 == 'S'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=129 and right_mark >=130;")

                                    print(self.results())
                                if (fec97 == 'P'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=131 and right_mark >=132;")

                                    print(self.results())

                                if (fec97 == 'OT'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=133 and right_mark >=134;")

                                    print(self.results())
                    if (fec93 == 'OT'):
                        fec94 = input('A - For use in certain types of aircraft ''\n'
                                     'OT - other; ''\n'
                                     'B4 - back''\n'
                                     'Q - exit').upper()
                        if (fec94 == 'A'):
                            fec95 = input('TI - Consigned from Taiwan, Indonesia, Sri Lanka or the Philippines ''\n'
                                          'OT - other; ''\n'
                                          'Q - exit').upper()
                            if (fec95 == 'TI'):
                                self.kursor.execute(
                                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=140 and right_mark >=141;")

                                print(self.results())
                            if (fec95 == 'OT'):
                                self.kursor.execute(
                                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=142 and right_mark >=143;")

                                print(self.results())
                        if (fec94 == 'OT'):
                            fec96 = input('TI - other threaded fittings ''\n'
                                          'OT - other; ''\n'
                                          'Q - exit').upper()
                            if (fec96 == 'TI'):
                                self.kursor.execute(
                                    "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                    " where left_mark <=146 and right_mark >=147;")

                                print(self.results())
                            if (fec96 == 'OT'):
                                fec97 = input('TI - Consigned from Taiwan ''\n'
                                              'I - Consigned from Indonesia ''\n'
                                              'S - Consigned from Sri Lanka ''\n'
                                              'P - Consigned from Philippines ''\n'
                                              'OT - other; ''\n'
                                              'Q - exit').upper()
                                if (fec97 == 'TI'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=149 and right_mark >=150;")

                                    print(self.results())
                                if (fec97 == 'I'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=151 and right_mark >=152;")

                                    print(self.results())
                                if (fec97 == 'S'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=153 and right_mark >=154;")

                                    print(self.results())
                                if (fec97 == 'P'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=155 and right_mark >=156;")

                                    print(self.results())

                                if (fec97 == 'OT'):
                                    self.kursor.execute(
                                        "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                        " where left_mark <=157 and right_mark >=158;")

                                    print(self.results())

                if (fec92 == 'OT'):
                    fec30 = input('A - elbows and bends ''\n'
                                  'OT - other; ''\n'
                                  'B4 - back''\n'
                                  'Q - exit').upper()
                    if (fec30 == 'A'):
                        fec31 = input('A - For use in certain types of aircraft ''\n'
                                     'OT - other; ''\n'
                                     'B4 - back''\n'
                                     'Q - exit').upper()
                        if (fec31 == 'A'):
                            self.kursor.execute(
                                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                " where left_mark <=166 and right_mark >=167;")

                            print(self.results())

                        if (fec31 == 'OT'):
                            self.kursor.execute(
                                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                " where left_mark <=168 and right_mark >=169;")

                            print(self.results())
                    if (fec30 == 'OT'):
                        fec32 = input('A - For use in certain types of aircraft ''\n'
                                     'OT - other; ''\n'
                                     'B4 - back''\n'
                                     'Q - exit').upper()
                        if (fec32 == 'A'):
                            self.kursor.execute(
                                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                " where left_mark <=172 and right_mark >=173;")

                            print(self.results())

                        if (fec32 == 'OT'):
                            self.kursor.execute(
                                "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                                " where left_mark <=174 and right_mark >=175;")

                            print(self.results())

        if (fec2 == 'OT'):
            fec8 = input('A - For use in certain types of aircraft ''\n'
                         'OT - other; ''\n'
                         'B4 - back''\n'
                         'Q - exit').upper()
            if (fec8 == 'A'):
                fec82 = input('A - With greatest external diameter not exceeding 609,6 mm ''\n'
                             'OT - other; ''\n'
                             'B4 - back''\n'
                             'Q - exit').upper()
                if (fec82 == 'A'):

                    fec83 = input('TI - Consigned from Taiwan, Indonesia, Sri Lanka or the Philippines ''\n'
                                 'OT - other; ''\n' 
                                 'Q - exit').upper()
                    if (fec83 == 'TI'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=189 and right_mark >=190;")

                        print(self.results())
                    if (fec83 == 'OT'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=191 and right_mark >=192;")

                        print(self.results())

            if (fec8 == 'OT'):
                fec84 = input('A - With greatest external diameter not exceeding 609,6 mm ''\n'
                              'OT - other; ''\n'
                              'B4 - back''\n'
                              'Q - exit').upper()
                if (fec84 == 'A'):

                    fec85 = input('TI - Consigned from Taiwan ''\n'
                                  'I - Consigned from Indonesia ''\n'
                                  'S - Consigned from Sri Lanka ''\n'
                                  'P - Consigned from Philippines ''\n'
                                  'OT - other; ''\n'
                                  'Q - exit').upper()
                    if (fec85 == 'TI'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=199 and right_mark >=200;")

                        print(self.results())
                    if (fec85 == 'I'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=201 and right_mark >=202;")

                        print(self.results())
                    if (fec85 == 'S'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=203 and right_mark >=204;")

                        print(self.results())
                    if (fec85 == 'P'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=205 and right_mark >=206;")

                        print(self.results())

                    if (fec85 == 'OT'):
                        self.kursor.execute(
                            "select depth, concat(repeat('-', depth), hts_code) as hts_code, title from chapter_73"
                            " where left_mark <=207 and right_mark >=208;")

                        print(self.results())
            if (fec8 == 'Q'):
                exit()
            else:
                print('zła wartosc')
                print(self.class_ssnth())
        if (fec2 == 'B4'):
            self.class_st()
        else:
            print('zła wartosc')
            print(self.class_ssnth())

    def results(self):

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

    def add(self):
        dac = input('R - add record; ''\n'
                    'B - add branch; ''\n'
                    'B4 - back').upper()
        if (dac == 'R'):

            a = input('Enter the left_mark:')
            print(type(a))
            aa = int(a)
            print(type(aa))
            self.kursor.execute("update chapter_76 set left_mark = left_mark + 2 where left_mark >= %i;" % aa)
            self.conn.commit()

            b = input('Enter the right_mark:')
            bb = int(b)

            self.kursor.execute("update chapter_76 set right_mark = right_mark +2 where right_mark >= %i;" % bb)
            self.conn.commit()

            f = input('enter the title:')
            d = input('enter the hts_code:')
            print(f, d)
            self.kursor.execute("insert into chapter_76 (HTS_code, Title) values (%s, %s);", (d, f))

            self.conn.commit()
            e = input('enter the depth:')
            g = input('enter the id:')
            gg = int(g)
            ee = int(e)

            self.kursor.execute("update chapter_76 set left_mark = %s where id = %s;", (aa, gg))
            self.conn.commit()
            self.kursor.execute("update chapter_76 set right_mark = %s where Id = %s;", [bb, gg])
            self.conn.commit()
            self.kursor.execute("update chapter_76 set Depth = %s where id = %s", [ee, gg])
            self.conn.commit()

            self.kursor.execute("select * from chapter_76 where left_mark = %i" % aa)

            chapter_76 = self.kursor.fetchall()

            print(" | %3s | | %-12s | | %9s | | %10s | | %5s | | %-360s |" % (
                'id', 'HTS_code', 'left_mark', 'right_mark', 'depth', 'title'))

            for row in chapter_76:
                ID = 0
                LEFT_MARK = 1
                RIGHT_MARK = 2
                DEPTH = 3
                HTS_CODE = 4
                TITLE = 5
                print(" | %3i | | %-12s | | %9i | | %10i | | %5i | | %-360s |" % (
                    row[ID], row[LEFT_MARK], row[RIGHT_MARK], row[DEPTH], row[HTS_CODE], row[TITLE]))
            print(self.menu())

        if (dac == 'B'):
            pass

    def delete(self):
        pass

    def update(self):
        pass




db = DBConnect(c)
