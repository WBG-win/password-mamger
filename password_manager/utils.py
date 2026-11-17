import base64


def encrypt_pwd(raw_str: ste) -> str:
    """
    密码编码： 原始字符串 -> base64字符串
    流程： str   --encode--> bytes --base64编码---> bytes --decode --> str
    注意： base64不是加密，只用来编码，用来练习字符转化
    """
    
    b = raw_str.encode("utf-8")
    b64 = base64.b64encode(b)
    return b64.decode("utf-8")

def decrypt_pwd(enc_str: str) -> str:
    """
    密码解析： 存起来的base64字符串 -> 原始明文密码
    流程： str --encode--> base64字节 --base64解码-->原始字节  --decode-->原始字符串
    """
    b = enc_str.encode("utf-8")
    raw_b = base64.b64decode(b)
    return raw_b.decode("utf-8")

#单独测试工具函数，直接运行这个文件测试编解码是否正常
if __name__ == "__main__":
    raw = "MyPass123"
    enc = encrpt_pwd
    dec = decrypt_pwd(enc)
    print("原始密码：", raw)
    print("编码后：", enc)
    print("解码后：", dec)