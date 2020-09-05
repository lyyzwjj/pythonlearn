import time

for i in range(1, 101):
    print("\r%.2f%%" % i, end='')
    # print("=", end='')
    time.sleep(0.1)

print("")
