import csv
import sqlite3


def create_db_with_csv(name, rows):
    print("blah")

    '''
    example data and header
    Name,Location,Year Established,Area
    Acadia National Park,Maine,1919,48876.58
    '''

    db_name = name + '.db'
    csv_name = name + '.csv'

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    #
    # automate this more at some point
    cur.execute("""DROP TABLE IF EXISTS natlpark""")
    cur.execute("""CREATE TABLE natlpark
            (name text, state text, year integer, area float)""")

    with open(csv_name, 'r') as f:
        reader = csv.reader(f.readlines()[1:])  # exclude header line
        cur.executemany("""INSERT INTO natlpark VALUES (?,?,?,?)""",
                        (row for row in reader))

    conn.commit()
    conn.close()


row_content = 1
create_db_with_csv('park', row_content)
