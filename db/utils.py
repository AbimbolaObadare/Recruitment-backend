from db.session import database, SQLALCHEMY_DATABASE_URL


async def check_db_connected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("Database is connected (^_^)")
    except Exception as e:
        print("Looks like db is missing or is there is some problem in connection,see below traceback")
        raise e
