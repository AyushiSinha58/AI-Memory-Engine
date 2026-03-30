import mysql.connector
from ml.testing import predict_message
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None

def store_memory(message, msg_type):
    pred, score = predict_message(message, msg_type)

    if pred == 0:
        print("Not important. Ignored.")
        return

    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    # Check if already exists
    cursor.execute("SELECT * FROM memory WHERE content = %s", (message,))
    existing = cursor.fetchone()

    if existing:
        print("Already exists, skipping.")
        cursor.close()
        conn.close()
        return

    query = """
    INSERT INTO memory (content, type, importance_score)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (message, msg_type, score))
    conn.commit()

    print(f"Stored: {message} (score: {score:.2f})")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    store_memory("I like Python", "preference")
    store_memory("ok", "casual")

def init_db():
    print("\nChecking DB connection...")
    conn = get_connection()

    if conn:
        print("Database connected")
        conn.close()
    else:
        print("Database connection failed")