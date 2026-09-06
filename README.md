# 🏥 BMI Management System

> 💻 A simple *BMI Management System* built using *Python 🐍 and MySQL 🗄️* to calculate, store, update, search, and track BMI records.

---

## 🌟 Project Overview

The *BMI Management System* is a console-based application developed using Python and MySQL.

It allows users to:

✨ Calculate their BMI
📝 Store personal BMI information
🔍 Search for users
✏️ Update existing records
🗑️ Delete users
📊 Track BMI history
📅 View previous BMI measurements

The project uses a relational database to maintain current BMI information and historical BMI records.

---

## 🚀 Features

### 👤 1. Add BMI User

Users can enter:

* 👨 Name
* 🎂 Age
* 📏 Height in centimeters
* ⚖️ Weight in kilograms

The system automatically calculates the BMI and determines the BMI category.

---

### 📋 2. View All BMI Records

Displays all registered users with:

text
🆔 User ID
👤 Name
🎂 Age
📏 Height
⚖️ Weight
🧮 BMI
📊 Category


---

### 🗑️ 3. Delete User

Users can delete an existing BMI record using the user's ID.

Example:

text
Enter user ID: 5

✅ User deleted successfully!


---

### ✏️ 4. Update User

Existing user information can be updated.

You can modify:

* 👤 Name
* 🎂 Age
* 📏 Height
* ⚖️ Weight

The system automatically recalculates:

text
🧮 BMI
📊 BMI Category


The new BMI measurement is also stored in the history table.

---

### 🔎 5. Search User

Users can search for a person using their name.

Example:

text
🔍 Enter name to search: Rahul


The system displays matching BMI records.

---

### 📈 6. BMI History

The system keeps track of previous BMI measurements.

Example:

text
👤 Rahul

📅 Date        ⚖️ Weight     🧮 BMI      📊 Category
------------------------------------------------------
📅 2026-09-01   70 kg        22.86       Normal
📅 2026-09-05   72 kg        23.51       Normal
📅 2026-09-10   75 kg        24.49       Normal


This makes it possible to track BMI changes over time.

---

## 🧮 BMI Formula

The system uses the standard BMI formula:

text
             Weight (kg)
BMI = ─────────────────────
          Height² (m)


For example:

text
⚖️ Weight = 70 kg
📏 Height = 175 cm = 1.75 m

BMI = 70 / (1.75 × 1.75)

🧮 BMI = 22.86


---

## 📊 BMI Categories

| 🧮 BMI Range      | 📊 Category |
| ----------------- | ----------- |
| 🔵 Less than 18.5 | Underweight |
| 🟢 18.5 – 24.9    | Normal      |
| 🟠 25 – 29.9      | Overweight  |
| 🔴 30 or above    | Obese       |

> ℹ️ These ranges are intended for general adult BMI classification and are not a medical diagnosis.

---

# 🛠️ Technologies Used

| Technology     | Purpose                                 |
| -------------- | --------------------------------------- |
| 🐍 *Python*  | Application development                 |
| 🗄️ *MySQL*  | Database management                     |
| 🔌 *PyMySQL* | Python–MySQL connection                 |
| 💻 *SQL*     | Database queries                        |
| 🔄 *CRUD*    | Create, Read, Update, Delete operations |

---

# 📂 Project Structure

text
🏥 BMI-Management-System/
│
├── 🐍 main.py
├── 🧮 calculations.py
├── 🔌 connection.py
├── 📄 README.md
└── 📦 requirements.txt


### 🐍 main.py

Contains the main menu and controls the flow of the application.

### 🧮 calculations.py

Contains the main application logic:

* 🧮 BMI calculation
* 📊 BMI category calculation
* ➕ Insert user
* 📋 View records
* ✏️ Update user
* 🗑️ Delete user
* 🔎 Search user
* 📈 Add BMI history
* 📅 View BMI history

### 🔌 connection.py

Contains the MySQL database connection.

---

# 🗄️ Database Design

The project uses a MySQL database called:

text
bmicalculator


The database contains two tables:

text
        👤 Bmi
          │
          │ 🔗 Foreign Key
          │
          ▼
    📈 Bmi_History


---

## 👤 Bmi Table

sql
CREATE TABLE Bmi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    height_cm FLOAT,
    weight_kgs FLOAT,
    bmi FLOAT,
    category VARCHAR(50)
);


### 📋 Columns

| Column          | Description           |
| --------------- | --------------------- |
| 🆔 id         | Unique user ID        |
| 👤 name       | User name             |
| 🎂 age        | User age              |
| 📏 height_cm  | Height in centimeters |
| ⚖️ weight_kgs | Weight in kilograms   |
| 🧮 bmi        | Calculated BMI        |
| 📊 category   | BMI category          |

---

# 📈 Bmi_History Table

sql
CREATE TABLE Bmi_History (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    height_cm FLOAT,
    weight_kgs FLOAT,
    bmi FLOAT,
    category VARCHAR(50),
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Bmi(id)
);


### 📋 Columns

| Column           | Description             |
| ---------------- | ----------------------- |
| 🆔 history_id  | Unique history ID       |
| 🔗 user_id     | Related user ID         |
| 📏 height_cm   | Recorded height         |
| ⚖️ weight_kgs  | Recorded weight         |
| 🧮 bmi         | Calculated BMI          |
| 📊 category    | BMI category            |
| 📅 recorded_at | Date and time of record |

---

# 🔗 Database Relationship

The project uses a *one-to-many relationship*.

text
             👤 One User
                 │
       ┌─────────┼─────────┐
       │         │         │
       ▼         ▼         ▼
   📈 Record  📈 Record  📈 Record
       1          2          3


For example:

text
👤 Rahul
   │
   ├── 📅 Sep 01 → 70 kg → BMI 22.86
   │
   ├── 📅 Sep 05 → 72 kg → BMI 23.51
   │
   └── 📅 Sep 10 → 75 kg → BMI 24.49


This means one user can have *multiple BMI history records*.

---

# ⚙️ Installation & Setup

## 1️⃣ Install Python

Check whether Python is installed:

bash
python --version


---

## 2️⃣ Install MySQL

Install MySQL Server and make sure the MySQL service is running.

---

## 3️⃣ Install PyMySQL

Run:

bash
pip install pymysql


---

## 4️⃣ Create the Database

Open MySQL and run:

sql
CREATE DATABASE bmicalculator;

USE bmicalculator;


Then create the tables shown above.

---

# 🔐 Database Configuration

Open:

text
🔌 connection.py


Configure your MySQL connection:

python
from pymysql import connect


def get_connection():

    connection = connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="bmicalculator"
    )

    return connection


⚠️ *Important:* Never upload your real MySQL password to GitHub.

For a real project, use environment variables such as .env instead of putting passwords directly in your source code.

---

# ▶️ Running the Project

After setting up the database, run:

bash
python main.py


You will see:

text
========================================
       🏥 BMI MANAGEMENT SYSTEM
========================================

1️⃣ View all BMI records
2️⃣ Insert BMI user
3️⃣ Delete user
4️⃣ Update user
5️⃣ Search user
6️⃣ Add BMI history
7️⃣ View BMI history
8️⃣ Exit

========================================
Enter your option:


---

# 💻 Example

### ➕ Adding a User

text
Enter your name: Rahul
Enter your age: 22
Enter your height in cms: 175
Enter your weight in kgs: 70

✅ Registered successfully!

🧮 BMI      : 22.86
📊 Category : Normal


### 📈 Adding a New BMI Measurement

text
Enter user ID: 1
Enter current height in cms: 175
Enter current weight in kgs: 75

✅ BMI HISTORY ADDED SUCCESSFULLY!

🧮 BMI      : 24.49
📊 Category : Normal


---

# 🧠 Concepts Learned

This project helped demonstrate several important concepts.

### 🐍 Python

* 🔹 Variables
* 🔹 Functions
* 🔹 Conditional statements
* 🔹 Loops
* 🔹 User input
* 🔹 Exception handling
* 🔹 Modules
* 🔹 Importing functions
* 🔹 Database connectivity

### 🗄️ MySQL

* 🔹 Database creation
* 🔹 Table creation
* 🔹 INSERT
* 🔹 SELECT
* 🔹 UPDATE
* 🔹 DELETE
* 🔹 WHERE
* 🔹 LIKE
* 🔹 JOIN
* 🔹 Foreign keys
* 🔹 One-to-many relationships

### 💡 Programming Concepts

* 🔹 CRUD operations
* 🔹 Data validation
* 🔹 BMI calculation
* 🔹 Database relationships
* 🔹 History tracking
* 🔹 Exception handling

---

# 🚀 Future Improvements

There are many ways to make this project more advanced:

### 🔐 User Authentication

* 👤 User registration
* 🔑 Login system
* 🔒 Password hashing
* 🚪 Logout

### 📊 Reports & Analytics

* 📈 BMI progress charts
* 📊 BMI statistics
* 📅 Monthly BMI reports
* ⚖️ Weight progress tracking
* 📉 BMI improvement tracking

### 📤 Data Export

* 📄 Export BMI report to PDF
* 📊 Export records to Excel
* 📁 Export records to CSV

### 🌐 Web Application

The console application can later be converted into a web application using:

text
🐍 Python
      ↓
🌐 Flask
      ↓
🎨 HTML + CSS
      ↓
⚡ JavaScript
      ↓
🗄️ MySQL


### 🎨 User Interface

A graphical interface can also be created using:

* 🖥️ Tkinter
* 🌐 Flask
* ⚛️ React
* 🎨 HTML/CSS/JavaScript

---

# 🏆 Project Goal

The goal of this project is to build a complete BMI tracking application that allows users to:

text
👤 Manage Users
       ↓
🧮 Calculate BMI
       ↓
📊 Categorize BMI
       ↓
💾 Store Records
       ↓
📈 Track BMI History
       ↓
📊 Analyze Progress


---

# 👨‍💻 Author

*Your Name*

🐍 Python | 🗄️ MySQL | 💻 Software Development

---

# 📜 License

This project is created for *educational and learning purposes*. 🎓

---

## ⭐ If you like this project

Give the repository a ⭐ and feel free to improve the project with your own features! 🚀
