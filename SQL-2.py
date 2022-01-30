import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')
    result = org[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (result,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (result,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (result,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY org DESC '
#  list_host = []
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
#    host = row[0].split('@')
    #  Making list of dictionaries
 #   list_host.append({host[1]: row[1]})
#  resultdict = {}
#  for dictionary in list_host:
#    for key in dictionary:
#        try:
#            resultdict[key] += dictionary[key]
#        except KeyError:
#            resultdict[key] = dictionary[key]
#  x = sorted(resultdict.values())
#  num = 0
#  for i in range(len(x)):
#    if x[i] > num:
#        num = x[i]
#    else:
#        continue
#  print(num)
cur.close()
