from app.database import engine

try:
    connection = engine.connect()

    print("Connected PostgreSQL successfully!")

    connection.close()

except Exception as e:
    print(e)