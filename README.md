#简易密码管理器
#项目架构说明
1.storage.py：存储层：只负责json文件读写，和业务逻辑解耦
2.utils.py：工具层，字符串<->bytes转换，base64编解码，通用工具
3.main.py：程序入口，菜单交互、业务调度，调用下层模块
4.pwd_data.json: 程序运行自动生成，持久花花保存数据

#如何运行??
python main.py

#学习目标
- 模块化拆分：下层不依赖上层
- str encode -> bytes decode -> str
- try except 异常捕获
- try __name__ = "__main__"： 模块单独测试
> ⚠️ 提醒：base64只是编码，不是安全加密，这个项目仅用于Python架构练习，不要存放真实重要密码！
