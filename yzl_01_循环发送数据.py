import socket


def main():
	# 创建一个套接字
	udp_use = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# bind绑定的是一个元组
	udp_use.bind(("192.168.111.128", 4545))
	while True:
		# 从键盘获取数据
		udp_date = input("请输入你要发的消息：")
		if udp_date == "exit":
			break
		# 可以使用套接字收发数据
		# udp_use.sendto(b"hhh", ("10.66.118.104", 8080))
		udp_use.sendto(udp_date.encode("utf-8"), ("192.168.111.132", 8080))

	# 关闭套接自字
	udp_use.close()


if __name__ == "__main__":
	main()