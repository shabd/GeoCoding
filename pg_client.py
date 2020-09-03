import psycopg2


def execute_query(query):
    username = 'postgres'
    password = 'password'
    database = 'postgres'
    host = '127.0.0.1'
    port = '5432'
    try:
        print("Connecting")
        connection = psycopg2.connect(
                            user=username,
                            password=password,
                            host=host,
                            port=port,
                            database=database
        )

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute(query)
        record = cursor.fetchall()
        return record

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")