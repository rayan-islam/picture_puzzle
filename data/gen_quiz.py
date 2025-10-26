import hashlib

def quiz():
    print('BEGIN TRANSACTION;')
    print('DELETE FROM quiz;')
    for line in open('puzzles.tsv', 'r', encoding='utf-8').readlines():
        vars = line.split('\t')
        id = vars[0].strip()
        link = vars[1].strip()
        answer = vars[2].strip()
        print('INSERT INTO quiz (id, link, answer) ')
        print(f'VALUES (\'{id}\', \'{link}\', \'{answer}\');')

    print('COMMIT;')

quiz()
