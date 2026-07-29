import requests, re

h = {'User-Agent': 'Mozilla/5.0'}
jobs = [
    ('正浩创新', 'https://guet.ncss.cn/student/jobs/Nhn3AZULWjDEhWfCG9Qg2v/detail.html'),
    ('宇树科技', 'https://fg.ncss.cn/student/jobs/6JsdAwQiZpBp4iLcXErRFh/detail.html'),
    ('蓝禾技术', 'https://j.ncss.cn/student/jobs/Jb22Z6DSg9BCRXLEDSdVJ/detail.html'),
    ('芯动科技', 'https://hust.ncss.cn/student/jobs/M5VjH1mxGnMLmg4ZfdRwZP/detail.html'),
    ('小鹏', 'https://3120ww.ncss.cn/student/m/jobs/KNiqQo5vuXpynyTGvurVQX/detail.html'),
    ('千寻智能', 'https://llcy.ncss.cn/student/jobs/GbEBXYVE6vXNJS8Rwe8zUE/detail.html'),
    ('京东JDS', 'https://m.ncss.cn/student/m/jobs/GwhRTzF4pcsjkq3ti3GPcF/detail.html'),
    ('好未来', 'https://vy.ncss.cn/student/jobs/QgTTqE4vna6Zuc6XBGve3s/detail.html'),
]

for name, url in jobs:
    try:
        r = requests.get(url, headers=h, timeout=10)
        years = re.findall(r'20\d\d届', r.text)
        unique_years = list(set(years))
        # Also check for "2027" in text
        has_2027 = '2027' in r.text[:10000]
        has_2026 = '2026' in r.text[:10000]
        print(f"{name}: 届别={unique_years} 含2027={has_2027} 含2026={has_2026}")
    except Exception as e:
        print(f"{name}: Error - {e}")
