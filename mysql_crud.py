import mysql.connector
import getpass # 🔑 Used to hide the password as you type

def run_mysql_app():
    # --- 1. Database Connection ---
    print("--- MySQL Login ---")
    db_user = input("Enter MySQL Username: ")
    
    # getpass.getpass() hides the password completely while typing.
    # If you want to see symbols like ****, you would need an extra library like 'pwinput'.
    db_password = getpass.getpass("Enter MySQL Password: ")

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=db_user,
            password=db_password,
            database="school_db"
        )
        cursor = connection.cursor()
        print(" Connection successful!")

        # --- 2. The CRUD Loop ---
        while True:
            print("\n--- 🛠️ MySQL CRUD Menu ---")
            print("1. Create | 2. Read | 3. Update | 4. Delete | 5. Exit")
            choice = input("Select (1-5): ")

            if choice == '5': 
                break

            scope = input("Apply to 'one' or 'many'? ").strip().lower()

            # --- CREATE ---
            if choice == '1':
                sql = "INSERT INTO students (id, name, grade) VALUES (%s, %s, %s)"
                if scope == 'one':
                    s_id = int(input("ID: "))
                    name = input("Name: ")
                    grade = input("Grade: ")
                    cursor.execute(sql, (s_id, name, grade))
                else:
                    data_list = []
                    while True:
                        inp = input("ID (or 'stop'): ")
                        if inp.lower() == 'stop': break
                        data_list.append((int(inp), input("Name: "), input("Grade: ")))
                    cursor.executemany(sql, data_list)
                connection.commit()

            # --- READ ---
            elif choice == '2':
                if scope == 'one':
                    s_id = input("Enter ID: ")
                    cursor.execute("SELECT * FROM students WHERE id = %s", (s_id,))
                    result = cursor.fetchone()
                    print(result if result else "Student not found.")
                else:
                    cursor.execute("SELECT * FROM students")
                    for row in cursor.fetchall(): 
                        print(row)

            # --- UPDATE ---
            elif choice == '3':
                val = input("New Grade: ")
                if scope == 'one':
                    target = input("ID to update: ")
                    cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (val, target))
                else:
                    target = input("Update everyone with current grade: ")
                    cursor.execute("UPDATE students SET grade = %s WHERE grade = %s", (val, target))
                connection.commit()

            # --- DELETE ---
            elif choice == '4':
                if scope == 'one':
                    target = input("ID to delete: ")
                    cursor.execute("DELETE FROM students WHERE id = %s", (target,))
                else:
                    target = input("Delete all with grade: ")
                    cursor.execute("DELETE FROM students WHERE grade = %s", (target,))
                connection.commit()

            print(f"Done! Rows affected: {cursor.rowcount}")

    except mysql.connector.Error as err:
        print(f" Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Connection closed.")

if __name__ == "__main__":
    run_mysql_app()