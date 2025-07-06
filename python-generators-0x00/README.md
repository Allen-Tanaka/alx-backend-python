# Python Generators – Task 0: Database Seeding

This project is part of the **ALX Backend Python** curriculum and focuses on setting up a MySQL database, creating a table, and populating it with user data using a CSV file. The goal is to prepare data streaming with generators in later tasks.

---

## 📁 Directory

`python-generators-0x00/`

---

## 📌 Task: Getting Started with Python Generators

### Objective

Create a generator-ready Python setup by:
- Connecting to a MySQL server
- Creating a database `ALX_prodev`
- Creating a table `user_data`
- Populating the table using `user_data.csv`

---

## 📜 Table Structure: `user_data`

| Column Name | Data Type | Constraints |
|-------------|-----------|-------------|
| `user_id`   | UUID / VARCHAR(36) | Primary Key, Indexed |
| `name`      | VARCHAR     | NOT NULL |
| `email`     | VARCHAR     | NOT NULL |
| `age`       | DECIMAL     | NOT NULL |

---

## 📂 Files

- `seed.py`: Main script to connect, create database, create table, and seed from CSV.
- `user_data.csv`: Sample data (must be in the same directory).
- `0-main.py`: Test file to verify database setup and insertion.
- `README.md`: Project documentation.

---

## 🧪 How to Run

### 1. Start MySQL
Ensure MySQL server is running and accessible.

### 2. Run the script
```bash
python3 0-main.py
