from app.database import engine

try:
    connection = engine.connect()

    print("Connected PostgreSQL successfully!")

    connection.close()

except Exception as e:
    print(e)

# Tạo migration initial mới
# alembic revision --autogenerate -m "initial schema"