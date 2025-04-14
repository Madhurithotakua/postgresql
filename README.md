# ☕ Coffee Machine with PostgreSQL Integration

A terminal-based Python project simulating a coffee machine that manages sales, inventory, and stores transaction data into a PostgreSQL database.

---

## 🚀 Features

- Offers three types of coffee: `espresso`, `filtercoffee`, `cappuccino`
- Tracks and updates ingredient resources: water, milk, coffee
- Accepts Indian currency: ₹1, ₹2, ₹5, ₹10, and ₹20 notes
- Calculates change and validates transactions
- Records sales and resource status in a PostgreSQL database

---

## 🛠️ Technologies Used

- **Python 3**
- **PostgreSQL**
- **psycopg2** (PostgreSQL adapter for Python)

---

## 🧾 SQL Setup

Make sure PostgreSQL is installed and running. Then, create the database and required tables.

### 🔸 Create Database

```sql
CREATE DATABASE madhuri;

🧪 How to Run
### Install dependencies:

pip install psycopg2
Update DB credentials in connect_db() function.

### Run the script:

python coffee_machine.py
