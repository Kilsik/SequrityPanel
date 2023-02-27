#  Bank security console
This is an internal repository for employees of the bank "Siyanie". If you got into the repository by accident, then you will not be able to run it, because you do not have access to the database,  but you can freely use the layout code or see how database queries are implemented.

The security panel is a website that can be connected to a remote database with visits and pass cards of our bank employees.

### How to install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To work, also set your DB settings via environment variables: HOST, PORT, BD_NAME, BD_USER, PASSWORD.
In the SECRET_KEY variable, save the secret key to access   your database.
### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.