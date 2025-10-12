import hashlib

def user():
    print('SET TRANSACTION READ WRITE;')

    for line in open('users.tsv', 'r', encoding='utf-8').readlines():
        vars = line.split('\t')
        id = vars[0].strip()
        name = vars[1].strip()
        pwd = vars[2].strip()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()

        token = vars[10].strip() + 'Z'
        if id=='admin':
            role = 'ADMIN'
        else:
            role ='TEAM'
        print('INSERT INTO \"user\"(id, last_time, level_completed, name, pwd, role, token)')
        print(f'VALUES (\'{id}\', NOW(), 0, \'{name}\', \'{pwd}\', \'{role}\', \'{token}\');')

    print('COMMIT;')

user()