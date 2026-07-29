"""Test which platforms allow direct job detail page access without login"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
}

# Test job detail pages from different platforms
tests = [
    # 国家大学生就业服务平台 (政府平台)
    ("国家就业平台", "https://www.ncss.cn/student/jobs/detail.html"),
    # 51job detail
    ("前程无忧-详情", "https://jobs.51job.com/shenzhen/156425189.html"),
    # 应届生求职网 detail
    ("应届生-详情", "https://q.yingjiesheng.com/jobs/detail/"),
    # Boss直聘 detail
    ("Boss直聘-详情", "https://www.zhipin.com/job_detail/abc123.html"),
]

for name, url in tests:
    try:
        r = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        status = r.status_code
        final_url = r.url
        length = len(r.text)

        # Check if redirected to login
        if 'login' in final_url.lower() or 'passport' in final_url.lower():
            print(f"{name}: ❌ 重定向到登录 → {final_url[:100]}")
        elif '请登录' in r.text[:1000] or '立即登录' in r.text[:1000]:
            print(f"{name}: ❌ 页面需要登录")
        elif status == 200 and length > 3000:
            # Check for job-related content
            has_job = '岗位' in r.text[:2000] or '职位' in r.text[:2000] or '招聘' in r.text[:2000] or '薪资' in r.text[:2000]
            if has_job:
                print(f"{name}: ✅ 可访问 ({length}字节，含岗位信息)")
            else:
                print(f"{name}: ⚠️ 可访问但可能不是岗位页 ({length}字节)")
        else:
            print(f"{name}: ❌ HTTP {status} len={length}")
        print(f"  Final URL: {final_url[:120]}")
    except Exception as e:
        print(f"{name}: ❌ {e}")
    print()
