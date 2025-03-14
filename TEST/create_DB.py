#2 データベース（DB）を作成する
import sqlite3

# カレントディレクトリにTEST.dbがなければ、作成します。
# すでにTEST.dbが作成されていれば、TEST.dbに接続します。
dbname = 'TEST.db'
conn = sqlite3.connect(dbname)

# データベースへのコネクションを閉じる。(必須)
conn.close()