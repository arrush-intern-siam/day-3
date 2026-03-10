# Database CRUD Operations

This repository contains Python scripts designed to interact with both NoSQL and SQL database management systems. Created as part of an internship learning module, the code demonstrates how to connect to and perform basic Create, Read, Update, and Delete (CRUD) operations on MongoDB and MySQL databases.

## Repository Contents

* `mongodb_crud.py`: A Python script implementing CRUD operations for a MongoDB database collection.
* `mysql_crud.py`: A Python script demonstrating how to connect to, modify, and query a MySQL database.

## Getting Started

### Prerequisites

To run the scripts in this repository, you will need Python installed on your local machine, along with the appropriate database drivers. 

You can install the required Python packages using `pip`:

```bash
pip install pymongo mysql-connector-python
```
Note: You must also have active local or remote instances of MongoDB and MySQL running to execute the scripts successfully.

## Clone the repository:
```bash
git clone [https://github.com/arrush-intern-siam/day-3.git](https://github.com/arrush-intern-siam/day-3.git)
cd day-3
```
## Configure Database Connections:
Open `mongodb_crud.py` and `mysql_crud.py` in your code editor and ensure the connection strings, credentials, and database names match your local or remote database setups.

## Run the scripts:
Execute the Python files directly from your terminal:
```bash
python mongodb_crud.py
python mysql_crud.py
```
## Technologies Used
- Python
- MongoDB (NoSQL)
- MySQL (SQL)