from PyQt4 import QtGui,QtCore
from signup import Ui_Dialog1
from hd import Ui_Dialog3
from nc import Ui_Dialog4
from c import Ui_Dialog5
from phonenum import Ui_Dialog6
from ac import Ui_Dialog7
from order import Ui_Dialog8
import MySQLdb as mdb
import sys

un=''
pw=''
staff={'egurunath':'guru','madan':'madan','harshith':'harshu','arun':'arun'}
class Dialog1(QtGui.QWidget, Ui_Dialog1):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getvalue)
        
    def getvalue(self):
    	global un
    	global pw
    	un=str(self.textEdit.toPlainText())
    	pw=str(self.textEdit_2.toPlainText())
    	un=un.strip()
    	pw=pw.strip()
        
    	self.window6 = Dialog6()
    	self.window6.show()
    	self.close()

        
name1=0
name2=0
cost1=0
cost2=1
q1=0
q2=2
tot1=0
tot2=3
b=''
num=''
final_total=0
class Dialog3(QtGui.QWidget, Ui_Dialog3):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)  	
        self.commandLinkButton.clicked.connect(self.home)
        self.comboBox.activated.connect(self.bigeats)
        self.comboBox_3.activated.connect(self.smalleats)
        self.comboBox_4.activated.connect(self.cakeaway)
        self.comboBox_5.activated.connect(self.combo)
        self.comboBox_6.activated.connect(self.sundaes)
        self.comboBox_7.activated.connect(self.sweet_treats)
        self.comboBox_8.activated.connect(self.bigeats_q)
        self.comboBox_2.activated.connect(self.smalleats_q)
        self.comboBox_9.activated.connect(self.cakeaway_q)
        self.comboBox_10.activated.connect(self.combo_q)
        self.comboBox_11.activated.connect(self.sundaes_q)
        self.comboBox_12.activated.connect(self.sweet_treats_q)
        final_total_str=str(final_total)
        self.textEdit.setText(final_total_str)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.order)
        
        self.con=mdb.connect('localhost',un,pw,'CoffeeShop')
        with self.con:
                self.cur=self.con.cursor()
        self.cur.execute("select * from Person_Details where Number=%s",(num))
        rows=self.cur.fetchall()
        print(rows)

    def order(self):
        self.window8=Dialog8()
        self.window8.show()
    def clear(self):
        self.tableWidget.clearContents()
        self.textEdit.clear()
        global name1,name2,cost1,cost2,q1,q2,tot1,tot2,final_total
        name1=0
        name2=0
        cost1=0
        cost2=1
        q1=0
        q2=2
        tot1=0
        tot2=3
        final_total=0

            
    def bigeats(self):
    	a=QtGui.QTableWidgetItem()
    	global b
    	b=self.comboBox.currentText()
        
    	a.setText(b)
        print(b),
    	global name1,name2	
    	self.tableWidget.setItem(name1,name2,a)
        name1=name1+1
    	
    def bigeats_q(self):
        c=QtGui.QTableWidgetItem()
        d=QtGui.QTableWidgetItem()
        e=QtGui.QTableWidgetItem()

        global cost1,cost2,q1,q2,tot1,tot2,b,final_total
        self.cur.execute("select Price from Big_eats where Name=%s",(b))
        for i in range(self.cur.rowcount):
                row=self.cur.fetchone()

                price=int(row[0])
        print(price),
        price1=str(price)
        c.setText(price1)

        self.tableWidget.setItem(cost1,cost2,c)
        cost1=cost1+1
        q=self.comboBox_8.currentText()
        e.setText(q)
        q=int(q)
        print(q),
        self.tableWidget.setItem(q1,q2,e)
        q1=q1+1
        total=price*q
        final_total+=total
        print(total)
        total_str=str(total)
        d.setText(total_str)
        self.tableWidget.setItem(tot1,tot2,d)
        tot1=tot1+1
        final_total_str=str(final_total)
        self.textEdit.setText(final_total_str)

    def smalleats(self):
        a=QtGui.QTableWidgetItem()
        global b
        b=self.comboBox_3.currentText()
        a.setText(b)
        print(b),
        global name1,name2 
        self.tableWidget.setItem(name1,name2,a)
        name1=name1+1

    def smalleats_q(self):
        c=QtGui.QTableWidgetItem()
        d=QtGui.QTableWidgetItem()
        e=QtGui.QTableWidgetItem()

        q=self.comboBox_2.currentText()
        e.setText(q)
        q=int(q)

        global cost1,cost2,q1,q2,tot1,tot2,b,final_total
        self.cur.execute("select Price from Small_eats where Name=%s",(b))
        for i in range(self.cur.rowcount):
                row=self.cur.fetchone()

                price=int(row[0])
        print(price),
        price1=str(price)
        c.setText(price1)
        print(q),
        self.tableWidget.setItem(cost1,cost2,c)
        cost1=cost1+1
        self.tableWidget.setItem(q1,q2,e)
        q1=q1+1
        total=price*q
        final_total+=total
        print(total)
        total_str=str(total)
        d.setText(total_str)
        self.tableWidget.setItem(tot1,tot2,d)
        tot1=tot1+1
        final_total_str=str(final_total)
        self.textEdit.setText(final_total_str)
    			
    def cakeaway(self):
        a=QtGui.QTableWidgetItem()
        global b
        b=self.comboBox_4.currentText()
        a.setText(b)
        print(b),
        global name1,name2
        self.tableWidget.setItem(name1,name2,a)
        name1=name1+1
        
    def cakeaway_q(self):
        c=QtGui.QTableWidgetItem()
        d=QtGui.QTableWidgetItem()
        e=QtGui.QTableWidgetItem()

        q=self.comboBox_9.currentText()
        e.setText(q)
        q=int(q)
        global cost1,cost2,q1,q2,tot1,tot2,b,final_total
        self.cur.execute("select Price from Cakeaway where Name=%s",(b))
        for i in range(self.cur.rowcount):
                row=self.cur.fetchone()

                price=int(row[0])
        print(price),
        print(q),
        price1=str(price)
        c.setText(price1)
        self.tableWidget.setItem(cost1,cost2,c)
        cost1=cost1+1
        self.tableWidget.setItem(q1,q2,e)
        q1=q1+1
        total=price*q
        final_total+=total
        print(total)
        total_str=str(total)
        d.setText(total_str)
        self.tableWidget.setItem(tot1,tot2,d)
        tot1=tot1+1
        final_total_str=str(final_total)
        self.textEdit.setText(final_total_str)
  		
    def combo(self):
        a=QtGui.QTableWidgetItem()
        global b
        b=self.comboBox_5.currentText()
        a.setText(b)
        print(b),
        global name1,name2
        self.tableWidget.setItem(name1,name2,a)
        name1=name1+1
       
    def combo_q(self):
        c=QtGui.QTableWidgetItem()
        d=QtGui.QTableWidgetItem()
        e=QtGui.QTableWidgetItem()

        q=self.comboBox_10.currentText()
        e.setText(q)
        q=int(q)
        global cost1,cost2,q1,q2,tot1,tot2,b,final_total
        self.cur.execute("select Price from Combo where Name=%s",(b))
        for i in range(self.cur.rowcount):
                row=self.cur.fetchone()

                price=int(row[0])
        print(price),
        print(q),
        price1=str(price)
        c.setText(price1)
        self.tableWidget.setItem(cost1,cost2,c)
        cost1=cost1+1
        self.tableWidget.setItem(q1,q2,e)
        q1=q1+1
        total=price*q
        final_total+=total
        print(total)
        total_str=str(total)
        d.setText(total_str)
        self.tableWidget.setItem(tot1,tot2,d)
        tot1=tot1+1
        final_total_str=str(final_total)
        self.textEdit.setText(final_total_str)

    def sundaes(self):
        a=QtGui.QTableWidgetItem()
        global b
        b=self.comboBox_6.currentText()

        a.setText(b)
        print(b),
        global name1,name2
        self.tableWidget.setItem(name1,name2,a)
        name1=name1+1
        
    def sundaes_q(self):
        c=QtGui.QTableWidgetItem()
        d=QtGui.QTableWidgetItem()
        e=QtGui.QTableWidgetItem()
        
        q=self.comboBox_11.currentText()
        e.setText(q)
        q=int(q)
        global cost1,cost2,q1,q2,tot1,tot2,b,final_total
        
        self.cur.execute("select Price from Sundaes where Name=%s",(b))
        for i in range(self.cur.rowcount):
                row=self.cur.fetchone()

                price=int(row[0])
        print(price),
        print(q),
        price1=str(price)
        c.setText(price1)
        self.tableWidget.setItem(cost1,cost2,c)
        cost1=cost1+1
        self.tableWidget.setItem(q1,q2,e)
        q1=q1+1
        total=price*q
        final_total+=total
        print(total)
        total_str=str(total)
        d.setText(total_str)
        self.ttableWidget.setItem(tot1,tot2,d)
        tot1=tot1+1
        final_total_str=str(final_total)
        self.teoxtEdit.setText(final_total_str)


    def sweet_treats(self):
        a=QtGui.QTableWidgetItem()
        global b
        b=self.comboBox_7.currentText()
        a.setText(b)
        print(b),
        global name1,name2
        self.tableWidget.setItem(name1,name2,a)
        name1=name1+1 

    def sweet_treats_q(self):
        c=QtGui.QTableWidgetItem()
        d=QtGui.QTableWidgetItem()
        e=QtGui.QTableWidgetItem()
        
        q=self.comboBox_12.currentText()
        e.setTexta(q)
        q=int(q)

        global cost1,cost2,q1,q2,tot1,tot2,b,final_total
        self.cur.execute("select Price from Sweet_Treats where Name=%s",(b))
        for i in range(self.cur.rowcount):
                row=self.cur.fetchone()

                price=int(row[0])
        print(price),
        print(q),
        price1=str(price)
        c.setText(price1)
        self.tableWidget.setItem(cost1,cost2,c)
        cost1=cost1+1
        self.tableWidget.setItem(q1,q2,e)
        q1=q1+1
        total=price*q
        final_total+=total
        print(total)
        total_str=str(total)
        d.setText(total_str)
        self.tableWidget.setItem(tot1,tot2,d)
        tot1=tot1+1
        final_total_str=str(final_total)
        self.textEdit.setText(final_total_str)

        
      		
    	
    def home(self):
    	self.window=Dialog6()
    	self.window.show()
    	self.close()	

class Dialog4(QtGui.QWidget, Ui_Dialog4):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.add_details)
        self.con=mdb.connect('localhost',un,pw,'CoffeeShop')
        with self.con:
                self.cur=self.con.cursor()

    def add_details(self):
    	num=str(self.textEdit.toPlainText())
    	name=str(self.textEdit_2.toPlainText())
    	addr1=str(self.textEdit_3.toPlainText())
    	addr2=str(self.textEdit_4.toPlainText())
    	addr3=str(self.textEdit_5.toPlainText())
    	self.cur.execute("insert into Person_Details values(%s,%s,%s,%s,%s)",(name,addr1,addr2,addr3,num))
    	self.close()
	

class Dialog5(QtGui.QWidget, Ui_Dialog5):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.show_details)
        self.con=mdb.connect('localhost',un,pw,'CoffeeShop')
        with self.con:
                self.cur=self.con.cursor()

    def show_details(self):
    	num=str(self.textEdit.toPlainText())
    	num=num.strip()
    	self.cur.execute("select * from Person_Details where Number=%s",(num))
    	rows=self.cur.fetchall()
    	for row in rows:
    		print(row)

class Dialog6(QtGui.QWidget, Ui_Dialog6):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sign_in)
        self.pushButton_2.clicked.connect(self.show_details)
        self.pushButton_3.clicked.connect(self.new_person)
        self.con=mdb.connect('localhost',un,pw,'CoffeeShop')
        with self.con:
                self.cur=self.con.cursor()

    def sign_in(self):
        self.window=Dialog1()
        self.window.show()
        self.close()
    
    def is_empty(self,rows):
        if(not rows):
        	return(True)
    def show_details(self):
        global num
        num=str(self.textEdit.toPlainText())
        num=num.strip()
        self.cur.execute("select * from Person_Details where Number=%s",(num))
        rows=self.cur.fetchall()
        if(self.is_empty(rows)):
        	self.window7=Dialog7()
        	self.window7.show()
        else:
        	self.window3 =Dialog3()
        	self.window3.show()
        	self.close()
    

    def new_person(self):
        self.window4 = Dialog4()
        self.window4.show()
    
class Dialog7(QtGui.QWidget, Ui_Dialog7):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cl)
    
    def cl(self):
        self.close()

class Dialog8(QtGui.QWidget, Ui_Dialog8):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.cl)
    def cl(self):
        self.close()





if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Dialog1()
    window.show()
    
    sys.exit(app.exec_())
