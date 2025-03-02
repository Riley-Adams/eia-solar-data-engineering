import psycopg2

try:
    # PostgreSQL credentials
    conn = psycopg2.connect(
        host="localhost",
        database="EIA - Solar Generation Data",
        user="postgres",
        password="9224"
    )
    
    # Create a cursor object
    cur = conn.cursor()
    
    # Execute a simple query
    cur.execute("SELECT version();")
    
    # Fetch the result
    db_version = cur.fetchone()
    print("PosgreSQL database version:", db_version)
    
    # close the cursor and connection
    cur.close()
    conn.close()
    print("Connection successful and closed.")
    
except Exception as e:
    print(f"Error: {e}")