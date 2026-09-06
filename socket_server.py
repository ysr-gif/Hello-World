
import socket
#创建socket对象
socket_sever = socket.socket()
#绑定ip地址和窗口
socket_sever.bind(('localhost', 8080))
#监听窗口
socket_sever.listen(1)
#listen方法内接受一个整数传参数，表示接受的链接数量
#等待客户端连接
#result:tuple = socket_sever.accept()
#conn = result[0]         #客户端的链接对象
#address = result[1]      #客户端的地址信息
conn, address = socket_sever.accept()
#accept方法返回的是二元元组（链接对象，客户端地址信息）
#可以通过 变量1，变量2 = socket_sever.accept()的形式，直接接受二元元组内的两个元素
#accept方法，是阻塞的方法，等待客户端的连接，如果没有链接，就卡在这一行不向下执行了


print(f"Connection address:,{address}")

#接受客户端信息,要使用客户端和服务端的本次链接对象，而非socket_sever对象
data = conn.recv(1024).decode("utf-8")
#recv接收的参数是缓冲区大小，一般给1024
#recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数转换为字符串对象

print(f"Received data:{data}")

#发送回复消息
msg = input("Enter message: ").encode("utf-8")
conn.send(msg)
#关闭链接
conn.close()
socket_sever.close()