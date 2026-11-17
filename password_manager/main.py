from storage import load_data, save_data
from utils import encrypt_pwd, decrypt_pwd

def add_password(data, platform, account, password):
    """
    业务：新增一条密码记录
    :param data: 内存里存放所有密码的字典
    :param platform: 平台名称（例如github）
    :param account: 账号
    :param password: 明文密码
    """
    data[platform] = {
        "account": account,
        "password": encrypt_pwd(password)
    }
    save_data(data)
    print("✅ 添加成功")

def query_password(data, platform):
    """业务： 根据平台名查询账号密码"""
    if platform not in data:
        print("❌ 没有找到该平台")
        return
    info = data[platform]
    # 去除编码后的密码：解码回明文展示
    pwd = decrypt_pwd(info["password"])
    print(f"账号：{info['account']}, 密码：{pwd}")

def del_password(data, platform):
    """业务：删除指定平台的记录"""
    if platform not in data:
        print("❌ 没有找到该平台")
        return
    del data[platform]
    save_data(data)
    print("✅ 删除成功")

def show_menu():
    """打印菜单，接受用户输入选项，只负责展示和输出"""
    print("\n===== 密码管理器 =====")
    print("1. 添加账号密码")
    print("2. 查询密码")
    print("3. 删除记录")
    print("0. 退出")
    return input("请输入选择：")

def main():
    """程序主逻辑，总调度函数"""
    #程序启动第一步，加载本地数据到内存字典
    data = load_data()
    #while True 无线循环菜单，知道用户选择0退出
    while True:
        choice = show_menu()
        if choice == "1":
            plat = input("平台名称：")
            acc = input("账号：")
            pwd = input("密码：")
            add_password(data, plat, acc, pwd)
        elif choice == "2":
            plat = input("要查询的平台：")
            query_password(data, plat)
        elif choice == "3":
            plat = input("要删除平台：")
            del_password(data, plat)
        elif choice =="0":
            print("程序退出")
            break
        else:
            print("输入无效，请重新选择")



# Python项目标准入口：
# 如果我们直接运行这个文件 python main.py，就执行main()
# 如果别的文件 import main，main()不会自动执行
if __name__ == "__main__":
    main()