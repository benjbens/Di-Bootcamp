import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'benstreet'
PASSWORD = 'bens'
DATABASE = 'Menu'


def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()

class MenuItem:
    def __init__(self, name, price ):
        self.name = name
        self.price = price 

    def delete(self):
        delete_query = f'DELETE FROM dishes WHERE name = {self.name}'
        run_query(delete_query)

    def save (self):
        save_query = f"""insert into dishes (name, price) values ('{self.name}', {self.price})"""
        run_query(save_query)


    def update (self, new_price):
        self.price = new_price
        update_query = f"""UPDATE dishes (price) set price = {self.price} where name = {self.name}"""
        run_query(update_query)


    def all(self):
        all_query = "SELECT * FROM dishes"
        return run_query(all_query)

    
    def get_by_name(self):
        get_by_name_query = f"SELECT {self.name} FROM dishes"
        

item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
print(item.all())


