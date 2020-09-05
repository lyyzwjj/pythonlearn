from socket import *


def send_msg(udp_socket):
    dest_ip = input("请输入对方ip:")
    try:
        dest_port = int(input("请输入对方端口"))
    except ValueError:
        print(ValueError)
    send_data = input("请输入要发送的数据:")
    # udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    # udp_socket.sendto(b"heheda", dest_addr)
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    # udp_socket.sendto(b"heheda", dest_addr)
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    local_addr = ("", 9999)
    udp_socket.bind(local_addr)
    # dest_addr = ('192.168.1.24', 9999)
    while True:
        print("------xxx聊天气xxx------")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op = input("请输入功能")
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误,请重新输入")
    udp_socket.close()


if __name__ == '__main__':
    main()
