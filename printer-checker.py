import MySQLdb
import subprocess
import time


class Monitoring(): # 
    """class for printer monitoring count cartridge"""

    def __init__(self, host='0.0.0.0',user='developer', passwd='developer', db='printer_monitor'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM Printer WHERE p_id=4")
        self.data = self.cursor.fetchall()


    def get_printers(self, data): # method get printers in database
        print(self.data)
        p_id = self.data[0][0]
        ip = self.data[0][3]
        oid = self.data[0][5]
        return ip, oid, p_id


    def get_counter(self, ip, oid, p_id): # method get counter cartridge count
        print("IS OK")
        ip = ip
        oid = oid
        p_id = p_id
        request = subprocess.Popen(["snmpwalk", "-v", "2c", "-c", "public", ip, oid], stdout=subprocess.PIPE)
        response = request.communicate()
        counter = response[0].decode('utf-8')[43:]
        return counter


    def set_counter(self, counter): # method save counter cartridge in database
        counter = counter
        p_id = self.data[0][0]
        print("=============RECIEVING DATA IN DB=======================")
        self.cursor.execute("INSERT INTO Monitoring (m_counter, m_date, m_info, m_status) VALUES(%s, NOW(), %s, true )", (counter, p_id ))
        self.db.commit()
        self.cursor.close()
        print("===========IS OK ! DATA RECIEVE======================================")


if __name__ == '__main__':
    printer = Monitoring()
    # print(printer.data)
    ip,oid,p_id = printer.get_printers(printer.data)
    print(ip,oid,p_id)
    counter = printer.get_counter(ip,oid,p_id)
    print(counter)
    write_counter = printer.set_counter(counter)
    #time.sleep(30)
