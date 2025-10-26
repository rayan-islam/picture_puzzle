import hashlib

def user():
    print('BEGIN TRANSACTION;')
    print('DELETE FROM \"user\";')
    for line in open('users.tsv', 'r', encoding='utf-8').readlines():
        vars = line.split('\t')
        name = vars[0].strip()
        id = vars[1].strip()
        pwd = vars[2].strip()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()

        if id=='rayan.islam':
            role = 'ADMIN'
        else:
            role ='TEAM'
        print('INSERT INTO \"user\"(id, last_time, level_completed, name, pwd, role, token)')
        print(f'VALUES (\'{id}\', CURRENT_TIMESTAMP, 0, \'{name}\', \'{pwd}\', \'{role}\', \'token\');')

    print('COMMIT;')

user()