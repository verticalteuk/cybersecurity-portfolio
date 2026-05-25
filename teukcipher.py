from pysqlcipher3 import dbapi2 as sqlite

def try_pwd(pwd, db):
    try:
        db.execute(f"PRAGMA key = '{pwd}'")
        db.execute('SELECT * FROM sqlite_master LIMIT 1')
    except sqlite.DatabaseError:
        print("working")
        return ''
    else:
        print(f'{pwd} is the correct password')
        return pwd


if __name__ =="__main__":
    with open('serpents.dict', 'rt') as f:
        dictionary = f.readlines()
    conn = sqlite.connect('data.db')
    c = conn.cursor()
    validated_pwd = ''
    for pwd in dictionary:
        validated_pwd = try_pwd(pwd.strip(), c)
        if validated_pwd:
            break
    print(validated_pwd)