import sqlite3

class robot_data():
    def __init__(self):
        self.con = sqlite3.connect('database.db')

        self.c = self.con.cursor()
        try:
            self.con.execute("""CREATE TABLE paller (
        		id INTEGER PRIMARY KEY AUTOINCREMENT,
                navn STRING,
                plads11 STRING,
                plads12 STRING,
                plads13 STRING,
                plads14 STRING,
                plads21 STRING,
                plads22 STRING,
                plads23 STRING,
                plads24 STRING,
                plads31 STRING,
                plads32 STRING,
                plads33 STRING,
                plads34 STRING,
                plads41 STRING,
                plads42 STRING,
                plads43 STRING,
                plads44 STRING
                )""")

            self.c.execute("""INSERT INTO paller (navn, plads11, plads12, plads13, plads14, plads21, plads22, plads23,
                plads24, plads31, plads32, plads33, plads34, plads41, plads42, plads43, plads44) VALUES
                (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", ("Medicin til børn i Afrika",
                'y', 'gb', 'gby', 'r', 'rb', 'br', 'gr', 'yb', 'gbrb', 'gby', 'r', 'rb', 'br', 'gr', 'yb', 'gbrb'))

            self.con.commit()

            print('Created table "paller"')

        except Exception as e:
            print(e)
            #print('Paller findes allerede')

    def new_order(self, order, navn):

        p = []

        for i in range(len(order)):
            p.append(order[i].get())

        self.c.execute("""INSERT INTO paller (navn, plads11, plads12, plads13, plads14, plads21, plads22, plads23,
            plads24, plads31, plads32, plads33, plads34, plads41, plads42, plads43, plads44) VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (navn, p[0], p[1], p[2], p[3], p[4], p[5], p[6],
            p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15]))


        print('Order "{}" has been created'.format(navn))
        self.con.commit()


    def get_ordrer(self):
        #self.c = self.con.cursor()

        #r_set = self.c.execute("""SELECT id, navn FROM paller""")
        #for order in self.c:
        #    print('Order #{} has name {}'.format(order[0], order[1]))

        r_set = self.con.execute("""SELECT navn, id FROM paller""")
        print(r_set)
        return r_set

    def del_palle(self):
        pass

    def produce_palle(self, id):
        product = self.con.execute("""SELECT plads11, plads12, plads13, plads14,
                                            plads21, plads22, plads23, plads24,
                                            plads31, plads32, plads33, plads34,
                                            plads41, plads42, plads43, plads44
                                        FROM paller WHERE id = {}""".format(id))

        return product
