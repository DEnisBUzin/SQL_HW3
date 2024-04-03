import psycopg2

class DataBase:

    def __init__(self, user: str, password: str, name_db: str):
        self.user = user
        self.password = password
        self.name_db = name_db


    def create_structure(self):
        global cursor, connection
        try:
            connection = psycopg2.connect(user=self.user, password=self.password, database=self.name_db)
            cursor = connection.cursor()

            cursor.execute("DROP TABLE IF EXISTS client_information")
            cursor.execute("DROP TABLE IF EXISTS client_number")

            sql_query_client = """CREATE TABLE IF NOT EXISTS client_information (
                                    id SERIAL PRIMARY KEY, 
                                    first_name VARCHAR(20), 
                                    second_name VARCHAR(20), 
                                    email VARCHAR(20));"""
            cursor.execute(sql_query_client)

            sql_query_number = """CREATE TABLE IF NOT EXISTS client_mobile(
                                    id SERIAL PRIMARY KEY,
                                    mobile INTEGER,
                                    client_id INTEGER REFERENCES client_information(id));"""
            cursor.execute(sql_query_number)
            connection.commit()
            print("[INFO] Tables created successfully.")
        except Exception as er:
            print(f"[ERROR] Failed to insert record into publisher table: {er}")
        finally:
            cursor.close()
            connection.close()
            print("[INFO] Connection is closed")


if __name__ == '__main__':
    newClass = DataBase('postgres', '310535', 'client')
    newClass.create_structure()
