from connection import get_connection


# --------------------------------
# PRINT BMI RECORDS
# --------------------------------

def print_bmi_records(bmi_records):

    if not bmi_records:
        print("No records found.")
        return

    for bmi in bmi_records:
        print(f"User ID           : {bmi[0]}")
        print(f"Name              : {bmi[1]}")
        print(f"Age               : {bmi[2]}")
        print(f"Height            : {bmi[3]} cm")
        print(f"Weight            : {bmi[4]} kg")
        print(f"BMI               : {bmi[5]}")
        print(f"Category          : {bmi[6]}")
        print("===============================")


# --------------------------------
# CALCULATE BMI
# --------------------------------

def calculate_bmi(weight_kgs, height_cm):

    height_m = height_cm / 100

    bmi = round(weight_kgs / (height_m ** 2), 2)

    return bmi


# --------------------------------
# GET BMI CATEGORY
# --------------------------------

def get_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# --------------------------------
# VIEW ALL BMI RECORDS
# --------------------------------

def bmi_records():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM Bmi"

    cursor.execute(query)

    records = cursor.fetchall()

    print_bmi_records(records)

    cursor.close()
    connection.close()


# --------------------------------
# INSERT USER
# --------------------------------

def inserting_bmi_user():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        height_cm = float(input("Enter your height in cms: "))
        weight_kgs = float(input("Enter your weight in kgs: "))

        bmi = calculate_bmi(weight_kgs, height_cm)

        category = get_category(bmi)

        query = """
        INSERT INTO Bmi
        (name, age, height_cm, weight_kgs, bmi, category)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            age,
            height_cm,
            weight_kgs,
            bmi,
            category
        )

        cursor.execute(query, values)

        connection.commit()

        # Get newly created user ID
        user_id = cursor.lastrowid

        # Add first BMI record to history
        history_query = """
        INSERT INTO Bmi_History
        (user_id, weight_kgs, height_cm, bmi, category)
        VALUES (%s, %s, %s, %s, %s)
        """

        history_values = (
            user_id,
            weight_kgs,
            height_cm,
            bmi,
            category
        )

        cursor.execute(history_query, history_values)

        connection.commit()

        print()
        print("User registered successfully!")
        print(f"User ID : {user_id}")
        print(f"BMI     : {bmi}")
        print(f"Category: {category}")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# --------------------------------
# DELETE USER
# --------------------------------

def deleting_user(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = "DELETE FROM Bmi WHERE id = %s"

        cursor.execute(query, (user_id,))

        if cursor.rowcount == 0:
            print("User not found.")

        else:
            connection.commit()
            print("User deleted successfully!")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# --------------------------------
# UPDATE USER
# --------------------------------

def updating_user():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        user_id = int(input("Enter user ID: "))

        query = "SELECT * FROM Bmi WHERE id = %s"

        cursor.execute(query, (user_id,))

        user = cursor.fetchone()

        if user is None:
            print("User not found.")
            return

        print()
        print("Current user details:")
        print(f"Name   : {user[1]}")
        print(f"Age    : {user[2]}")
        print(f"Height : {user[3]} cm")
        print(f"Weight : {user[4]} kg")

        print()

        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        height_cm = float(input("Enter new height: "))
        weight_kgs = float(input("Enter new weight: "))

        bmi = calculate_bmi(weight_kgs, height_cm)

        category = get_category(bmi)

        update_query = """
        UPDATE Bmi
        SET name = %s,
            age = %s,
            height_cm = %s,
            weight_kgs = %s,
            bmi = %s,
            category = %s
        WHERE id = %s
        """

        values = (
            name,
            age,
            height_cm,
            weight_kgs,
            bmi,
            category,
            user_id
        )

        cursor.execute(update_query, values)

        # Save new measurement in history
        history_query = """
        INSERT INTO Bmi_History
        (user_id, weight_kgs, height_cm, bmi, category)
        VALUES (%s, %s, %s, %s, %s)
        """

        history_values = (
            user_id,
            weight_kgs,
            height_cm,
            bmi,
            category
        )

        cursor.execute(history_query, history_values)

        connection.commit()

        print()
        print("User updated successfully!")
        print(f"New BMI     : {bmi}")
        print(f"New category: {category}")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# --------------------------------
# SEARCH USER
# --------------------------------

def search_user():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        name = input("Enter name to search: ")

        query = """
        SELECT * FROM Bmi
        WHERE name LIKE %s
        """

        cursor.execute(query, (f"%{name}%",))

        records = cursor.fetchall()

        print_bmi_records(records)

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# --------------------------------
# ADD BMI HISTORY
# --------------------------------

def add_bmi_history():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        user_id = int(input("Enter user ID: "))

        # Check if user exists
        query = "SELECT * FROM Bmi WHERE id = %s"

        cursor.execute(query, (user_id,))

        user = cursor.fetchone()

        if user is None:
            print("User not found.")
            return

        print(f"User: {user[1]}")

        height_cm = float(input("Enter current height in cms: "))
        weight_kgs = float(input("Enter current weight in kgs: "))

        bmi = calculate_bmi(weight_kgs, height_cm)

        category = get_category(bmi)

        history_query = """
        INSERT INTO Bmi_History
        (user_id, weight_kgs, height_cm, bmi, category)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            user_id,
            weight_kgs,
            height_cm,
            bmi,
            category
        )

        cursor.execute(history_query, values)

        # Also update current BMI in main table
        update_query = """
        UPDATE Bmi
        SET height_cm = %s,
            weight_kgs = %s,
            bmi = %s,
            category = %s
        WHERE id = %s
        """

        update_values = (
            height_cm,
            weight_kgs,
            bmi,
            category,
            user_id
        )

        cursor.execute(update_query, update_values)

        connection.commit()

        print()
        print("BMI history added successfully!")
        print(f"BMI     : {bmi}")
        print(f"Category: {category}")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


# --------------------------------
# VIEW BMI HISTORY
# --------------------------------

def view_bmi_history():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        user_id = int(input("Enter user ID: "))

        query = """
        SELECT
            h.history_id,
            b.name,
            h.weight_kgs,
            h.height_cm,
            h.bmi,
            h.category,
            h.recorded_at
        FROM Bmi_History h
        JOIN Bmi b
        ON h.user_id = b.id
        WHERE h.user_id = %s
        ORDER BY h.recorded_at
        """

        cursor.execute(query, (user_id,))

        records = cursor.fetchall()

        if not records:
            print("No BMI history found.")
            return

        print()
        print("========== BMI HISTORY ==========")

        for record in records:

            print(f"History ID : {record[0]}")
            print(f"Name       : {record[1]}")
            print(f"Weight     : {record[2]} kg")
            print(f"Height     : {record[3]} cm")
            print(f"BMI        : {record[4]}")
            print(f"Category   : {record[5]}")
            print(f"Date       : {record[6]}")
            print("---------------------------------")

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()
    
    
    

    
    