from socket import *
import struct

# 大端小端 个人小端 服务器大端口   规定网络上全部已大端传送 网络字节序 大端
# !H8sb5sb  H占两个字节的坑  1会替换掉 8s test.jpg 8个字节 b 0  5s octet 5个字节 b 0
sendData = struct.pack("!H8sb5sb", 1, "test.jpg", 0, "octet", 0)

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto(sendData, ("192.168.1.24", 69))

udpSocket.close()
