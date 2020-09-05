from socket import *


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    local_addr = ("", 9999)
    udp_socket.bind(local_addr)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)
    udp_socket.close()


if __name__ == '__main__':
    main()
