CoffeeShop Application

Home Delivery coffeeshop application in python

==========================================================================================================================

Pre-requisites to run the Program 


Download packages for Pyqt4 Designer and SIP to support it.

http://www.riverbankcomputing.com/software/pyqt/download

Download sources of the latest SIP - sip-4.12.4.tar.gz (Linux, UNIX, MacOS/X source). Unpack them and enter the directory:

python3 configure.py 
make
sudo make install


Download the sources of the latest PyQt - PyQt-x11-gpl-4.8.5.tar.gz (Linux, UNIX source), and install it:

python configure.py 
make
Notice, that i am launching python3 instead of python.

Download MYSQLdb module

After installing all this:
1) Put the everything what has been provided in one folder and open the folder in the terminal
2) Create the database in the following steps below:
mysql> CREATE DATABASE CoffeeShop;
Query OK, 1 row affected (0.02 sec)
We create a new CoffeeShop database. We will use this database throughout the tutorial.
mysql> CREATE USER 'databasename'@'localhost' IDENTIFIED BY 'name';
Query OK, 0 rows affected (0.00 sec)
mysql> USE CoffeeShop;
Database changed

mysql> GRANT ALL ON CoffeeShop.* TO 'databasename'@'localhost';
Query OK, 0 rows affected (0.00 sec)
We create a new database user. We grant all privileges to this user for all tables of the testdb database.

Now run the coffee.py file
3) Now run the sign_main.py file
4) Now you can follow the ongoing events on the output interface as mentioned in the report.


