# UDP Port 30000 測試伺服器

這個輕量級的 Python 腳本是一個簡單的 UDP 伺服器，設計用於在 Linux Ubuntu 系統上開啟並監聽 30000 端口。它的主要用途是作為一個測試目標，例如用來進行 Nmap 的 UDP 端口掃描 (`nmap -sU`) 測試。

當伺服器接收到任何 UDP 資料時，它會將收到的訊息和來源位址印出，並回傳一個簡單的確認訊息給客戶端。

## 快速開始

### 步驟 1: 下載程式碼

首先，將此儲存庫克隆到你的 Ubuntu 系統上：

```bash
git clone https://github.com/你的用戶名/你的儲存庫名.git
cd 你的儲存庫名
```

### 步驟 2: 執行伺服器

為了讓伺服器在背景持續運行，即使你關閉了終端機，我們可以使用 `nohup` 命令。

執行以下指令來啟動伺服器：

```bash
nohup python3 udp_server.py &
```

這個命令會執行以下動作：

- `nohup`：確保程式在終端機關閉後依然運行，不受 HUP 信號影響。
- `python3 udp_server.py`：啟動你的 Python 腳本。
- `&`：將程式放入背景執行，立即釋放終端機。

成功執行後，所有伺服器的輸出將被記錄到一個名為 `nohup.out` 的檔案中。

## 如何測試？

在另一台電腦上，你可以使用 Nmap 進行 UDP 端口掃描，以確認伺服器是否正常運行：

```bash
nmap -sU -p 30000 <你的伺服器IP地址>
```

如果掃描結果顯示 30000 端口為 `open|filtered`，則代表伺服器正在正常監聽。

## 停止伺服器

如果需要停止伺服器，你需要找到它的 PID (Process ID) 並終止它。

首先，使用 `pgrep` 命令找到 `udp_server.py` 程式的 PID：

```bash
pgrep -f "python3 udp_server.py"
```

這個命令會回傳一個或多個數字，這些就是程式的 PID。

接著，使用 `kill` 命令來終止程式。假設你找到的 PID 是 12345：

```bash
kill 12345
```
