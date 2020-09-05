from socket import *


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    local_addr = ("", 9998)
    udp_socket.bind(local_addr)
    dest_ip = input("请输入对方ip:")
    try:
        dest_port = int(input("请输入对方端口"))
    except ValueError:
        print(ValueError)
    # dest_addr = ('192.168.1.24', 9999)
    while True:
        send_data = input("请输入要发送的数据:")
        if send_data == "exit":
            break
        # udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))
        # udp_socket.sendto(b"heheda", dest_addr)
    udp_socket.close()


if __name__ == '__main__':
    main()
