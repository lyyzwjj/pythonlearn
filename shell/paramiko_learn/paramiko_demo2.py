# coding:utf-8

import sys
import paramiko
import threading


def getConnection(ip, username, password, command, port=22):
    """
    :param ip: 服务器的ip
    :param username:  服务器的用户名称
    :param password:  服务器的密码
    :param CMD:  服务器的命令
    :param port:  服务器的端口
    """
    ssh = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(policy)
    ssh.connect(
        hostname=ip,  # 服务器的ip
        port=port,  # 服务器的端口
        username=username,  # 服务器的用户名
        password=password  # 用户名对应的密码
    )
    stdin, stdout, stderr = ssh.exec_command(command)

    result = stdout.read().decode()

    error = stderr.read().decode()

    print("+++++++++++++++++++++++start++++++++++++++++++++")
    print("[connect success] | ip : %s" % ip)
    print("result: \n %s" % result)
    if error != " ":
        print("error: \n %s" % error)
    print("+++++++++++++++++++++++done++++++++++++++++++++")

    ssh.close()


# 多线程执行脚本
def main(host_list, command):
    thread_list = []
    for ip, username, password in host_list:
        thread = threading.Thread(target=getConnection, args=(ip, username, password, command))
        thread_list.append(thread)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == "__main__":
    host_list = [
        ("hadoop1", "root", "wzzst310"),
        ("hadoop2", "root", "wzzst310"),
        ("hadoop3", "root", "wzzst310"),
        ("hadoop4", "root", "wzzst310"),
        ("hadoop5", "root", "wzzst310"),
    ]
    command = sys.argv[1]
    main(host_list, command)
    # /usr/local/apache-zookeeper-3.6.1-bin/bin/zkServer.sh start
    # /usr/local/apache-zookeeper-3.6.1-bin/bin/zkServer.sh stop
    # /usr/local/kafka_2.13-2.5.0/bin/zookeeper-server-start.sh -daemon /usr/local/kafka_2.13-2.5.0/config/zookeeper.properties
    # /usr/local/kafka_2.13-2.5.0/bin/zookeeper-server-start.sh /usr/local/kafka_2.13-2.5.0/config/zookeeper.properties
    # /usr/local/kafka_2.13-2.5.0/bin/zookeeper-server-stop.sh
    # /usr/local/apache-zookeeper-3.6.1-bin/bin/zkServer.sh start;/usr/local/kafka_2.13-2.5.0/bin/zookeeper-server-start.sh -daemon /usr/local/kafka_2.13-2.5.0/config/zookeeper.properties
    # /usr/local/apache-zookeeper-3.6.1-bin/bin/zkServer.sh stop;/usr/local/kafka_2.13-2.5.0/bin/zookeeper-server-stop.sh
