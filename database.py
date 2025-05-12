import sqlite3

def startDb():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE,
              password TEXT
              )
""")
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            userID TEXT PRIMARY KEY,
            mainAmount REAL DEFAULT 0,
            investBTC REAL DEFAULT 0,
            soldBTC REAL DEFAULT 0,
            remainBTC REAL DEFAULT 0,
            investETH REAL DEFAULT 0,
            soldETH REAL DEFAULT 0,
            remainEth REAL DEFAULT 0,
            investSOL REAL DEFAULT 0,
            soldSOL REAL DEFAULT 0,
            remainSOL REAL DEFAULT 0,
            balanceTotal REAL DEFAULT 0,
            statsProfit REAL DEFAULT 0,
            spent REAL DEFAULT 0,
            timeSpent INTEGER DEFAULT 0,
            coinAmount INTEGER DEFAULT 0,
            FOREIGN KEY(userID) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()