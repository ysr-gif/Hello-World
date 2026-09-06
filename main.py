"""1、设计一个类可以完成数据的封装
   2、设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
   3、读取文件，生产数据对象
   4、进行数据需要的逻辑运算
"""


from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("C:\\Users\\YAO\\Desktop\\2011年1月销售额.txt")
json_file_reader = JsonFileReader("C:\\Users\\YAO\\Desktop\\2011年2月销售额.txt")


jan_data: list[Record]= text_file_reader.read_data()
feb_data: list[Record]= json_file_reader.read_data()

all_data: list[Record]= jan_data + feb_data



conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

cursor = conn.cursor()

conn.select_db("py_sql")

for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province) "\
          f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)


conn.close()