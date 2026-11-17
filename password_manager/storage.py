import json

#定义常量，数据保存的文件名，统一管理
DATA_FILE = "pwd_data.json"


def load_data():
    """
    加载本地保存的密码数据
    返回： 字典 {平台名:账号密码信息}
    如文件不存在，不报错，返回空
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            #json.load:把文件里的json文本转化为python字典
            return json.load(f)
    except FileNotFoundError:   
            #用于捕获异常
        return {}
    
def save_data(data):
    """
    把内存的数据，写入到保存的json文件
    参数是data，保存字典密码
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        #json.dump: python字典转化为json文本，写入文件
        #ensure_ascii=False: 中文不转义： indent=2，格式缩进
        json.dump(data, f, ensure_ascii=False, indent=2)

# 下面这一段：只有直接运行 storage.py 的时候才执行，用来单独测试这个模块
# 被main.py import导入的时候，这段代码不会运行
if __name__ == "__main__":
    test = load_data()
    print("当前加载的数据：", test)