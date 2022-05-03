import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'benstreet'
PASSWORD = 'bens'
DATABASE = 'users'


def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

def create_table_query(name, **kwargs):
    q = f'Create table {name} ('
    for field_name, field_type in kwargs.items():
        q += f'{field_name} {field_type},'
    return q[:-1] + ')'


def add_user_query(user_name, password):
    q = f"INSERT INTO user_passwords (user_name, user_password) VALUES ('{user_name}', '{password}') RETURNING id, user_name, user_password;"
    return run_query(q)

new_user = add_user_query('benji', '1234')
q = create_table_query('user_passwords', id= "Serial primary key", username='VarChar (100)', password = "VarChar(50)")
run_query(q)
# 1st part - registering 

# registering

# 2nd part - Login

# login 