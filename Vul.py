import sqlite3

def vulnerable_login(username, password):
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()

    # ❌ VULNERABLE: Direct string concatenation with user input
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing login query")  # Avoid logging sensitive query contents

    cur.execute(query)

    result = cur.fetchone()
    conn.close()
    return result
