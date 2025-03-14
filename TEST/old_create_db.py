import sqlite3

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = ('TEST.db')
conn = sqlite3.connect(dbname)

# データベースへのコネクションを閉じる。(必須)
conn.close()
#参考 https://proengineer.internous.co.jp/content/columnfeature/20735