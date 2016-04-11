from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='artists', password='artists_1',
                                 host='192.168.99.1',
                                 database='artists')
cnx.close()
