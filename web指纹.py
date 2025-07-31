import requests
import hashlib
import json
import re


class WebFingerprinter:
    def __init__(self, fingerprint_db):
        # 初始化Web指纹识别器，传入指纹数据库
        self.fingerprint_db = fingerprint_db

    def get_response(self, url):
        # 发送HTTP GET请求获取目标网站的响应
        try:
            response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            return response
        except requests.exceptions.RequestException as e:
            # 如果请求出错，打印错误信息并返回None
            print(f"Request error: {e}")
            return None

    def match_fingerprints(self, response):
        # 匹配指纹数据库中的规则，识别目标网站的技术栈
        results = []
        for fp in self.fingerprint_db:
            # 遍历指纹数据库中的每一条规则
            if fp['match_type'] == 'header':
                # 如果规则类型是HTTP头
                header_value = response.headers.get(fp['match_location'], '')
                # 获取指定的HTTP头值
                if fp['match_rule'] in header_value:
                # 如果规则匹配成功，添加到结果列表
                    results.append(fp['name'])
            elif fp['match_type'] == 'body':
                # 如果规则类型是HTML正文
                if re.search(fp['match_rule'], response.text):
                # 使用正则表达式匹配HTML正文
                    results.append(fp['name'])
            elif fp['match_type'] == 'file':
                # 如果规则类型是文件内容
                file_url = response.url.rstrip('/') + fp['match_location']
                file_content = requests.get(file_url, timeout=5).content
                # 获取文件内容
                file_md5 = hashlib.md5(file_content).hexdigest()
                # 计算文件内容的MD5值
                if file_md5 == fp['match_rule']:
                # 如果MD5值匹配成功，添加到结果列表
                    results.append(fp['name'])
        return results

    def fingerprint(self, url):
        response = self.get_response(url)
        if response is None:
            return []
        return self.match_fingerprints(response)


if __name__ == "__main__":
    # 指纹数据库
    fingerprint_db = [
        {
            "name": "用友-NC-Cloud",
            "category": "nc",
            "match_type": "header",
            "match_location": "Server",
            "match_rule": "NC-Cloud"
        },
        {
            "name": "GitLab",
            "category": "devops",
            "match_type": "body",
            "match_location": "<title>",
            "match_rule": "GitLab"
        },
        {
            "name": "爱快流控路由",
            "category": "network",
            "match_type": "file",
            "match_location": "/favicon.ico",
            "match_rule": "md5:123456789abcdef"
        },
        {
            "name": "Apache",
            "category": "webserver",
            "match_type": "header",
            "match_location": "Server",
            "match_rule": "Apache"
        },
        {
            "name": "WordPress",
            "category": "cms",
            "match_type": "string",
            "match_location": "wp-content",
            "match_rule": "/wp-content/"
        }
    ]

    # 资产列表
    assets = [
        "http://nc-cloud.com",
        "http://gitlab.com",
        "http://www.ikuai8.com"
    ]

    # 指纹识别
    fingerprinter = WebFingerprinter(fingerprint_db)
    for asset in assets:
        results = fingerprinter.fingerprint(asset)
        print(f"{asset} - Detected technologies: {results}")
