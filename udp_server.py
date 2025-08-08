import socket

# 設定IP地址和port
# 監聽所有可用的網路介面
HOST = '0.0.0.0'
PORT = 30000

# 建立一個UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 綁定IP和port
server_socket.bind((HOST, PORT))

print(f"UDP伺服器已在 {HOST}:{PORT} 啟動，等待接收資料...")

while True:
    # 接收資料，設定緩衝區大小為1024位元組
    data, address = server_socket.recvfrom(1024)
    print(f"從 {address} 接收到資料: {data.decode('utf-8')}")

    # 回傳訊息給客戶端
    response = "伺服器已收到你的訊息！"
    server_socket.sendto(response.encode('utf-8'), address)
