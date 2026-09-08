import socket
#创建socket对象
socket_client = socket.socket()
#连接服务器
socket_client.connect(('localhost', 8080))
while True:
#发送消息
    msg = input("Enter message: ")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("utf-8"))
#接收返回消息
    recv_data = socket_client.recv(1024)
    print(f"Recieved:,{recv_data.decode('utf-8')}")
#关闭链接
socket_client.close()