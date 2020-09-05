from socket import *
import threading


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("输入要发送的数据: ")
        # udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        # udp_socket.sendto(b"heheda", dest_addr)
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))
        print("已发送")


def recv_msg(udp_socket):
    while True:
        # udp_socket.sendto(b"heheda", dest_addr)
        recv_data = udp_socket.recvfrom(1024)
        print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    local_addr = ("", 9999)
    udp_socket.bind(local_addr)
    # dest_addr = ('192.168.1.24', 9999)
    dest_ip = input("请输入对方ip:")
    try:
        dest_port = int(input("请输入对方端口"))
    except ValueError:
        print(ValueError)
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
