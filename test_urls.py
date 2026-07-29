"""Test which URL formats actually work"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

tests = [
    # NowCoder search pages
    ("牛客网-校招搜索-嵌入式", "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式"),
    ("牛客网-校招搜索-电商运营", "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商运营"),
    ("牛客网-校招搜索-新媒体", "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=新媒体运营"),
    # NowCoder job detail (should fail)
    ("牛客网-岗位详情", "https://www.nowcoder.com/jobs/detail/450175"),
    # Boss直聘
    ("Boss直聘-嵌入式应届", "https://www.zhipin.com/web/geek/job?query=嵌入式工程师&experience=401"),
    ("Boss直聘-电商运营应届", "https://www.zhipin.com/web/geek/job?query=电商运营&experience=401"),
    # 51job
    ("前程无忧-嵌入式校招", "https://we.51job.com/pc/search?keyword=嵌入式工程师&keywordType=3"),
    # 应届生
    ("应届生求职网-搜索", "https://q.yingjiesheng.com/jobs/search/?keyword=嵌入式"),
]

for name, url in tests:
    try:
        r = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        final_url = r.url
        status = r.status_code
        length = len(r.text)
        # Check if it looks like a real page or a redirect to login
        is_login = 'login' in r.url.lower() or 'passport' in r.url.lower() or '请登录' in r.text[:500]
        is_blocked = 'waf' in r.text[:200].lower() or '验证' in r.text[:500]

        if is_login:
            result = "❌ 重定向到登录页"
        elif is_blocked:
            result = "❌ 被反爬拦截"
        elif status == 200 and length > 5000:
            result = f"✅ 正常 ({length}字节)"
        elif status == 200:
            result = f"⚠️ 页面较小 ({length}字节)"
        else:
            result = f"❌ HTTP {status}"

        print(f"{name}: {result}")
        print(f"  URL: {final_url[:120]}")
    except Exception as e:
        print(f"{name}: ❌ 连接失败 - {e}")
    print()
