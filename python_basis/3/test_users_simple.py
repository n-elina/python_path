import csv


def test_workers_are_adults_v1():
    with open('users.csv') as f:
        users = csv.DictReader(f, delimiter=';')
        workers = [user for user in users if user['status'] == 'worker']

    for worker in workers:
        assert int(worker['age']) >= 18, f'Worker {worker['name']} age must be >= 18'









        # workers = []
        # for user in users:
        #     if user['status'] == 'worker':       # вся эта конструкция равнозначна строчке выше - workers = [user for user in users if user['status'] == 'worker']
        #         workers.append(user)