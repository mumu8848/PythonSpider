import uiautomator2 as u2

def main():
    try:
        # 连接设备。如果有多台设备连接，请指定设备序列号。
        # 你可以通过 `adb devices` 命令查看所有连接的设备及其序列号。
        device = u2.connect()  # 如果只有一台设备连接，可以这样初始化

        # 打印设备信息以确认连接成功
        print(f"Connected to device: {device.info}")

        # 获取当前屏幕的 XML UI 层次结构
        xml_hierarchy = device.dump_hierarchy()

        # 点击微信
        device(text="微信").click()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()