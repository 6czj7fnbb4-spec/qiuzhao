"""
检查 ncss.cn 岗位是否过期，提取截止日期
"""
import requests, re
from config import FEATURED_JOBS

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
}

for tier_key in ["high", "mid", "low"]:
    tier = FEATURED_JOBS[tier_key]
    for job in tier["jobs"]:
        url = job["url"]
        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.encoding = 'utf-8'
            text = r.text

            # Look for deadline patterns
            deadline_patterns = [
                r'截止.*?(\d{4}[-/年]\d{1,2}[-/月]\d{1,2}[日号]?)',
                r'(\d{4}[-/年]\d{1,2}[-/月]\d{1,2}[日号]?).*?截止',
                r'网申.*?(\d{4}[-/年]\d{1,2}[-/月]\d{1,2})',
                r'投递.*?(\d{4}[-/年]\d{1,2}[-/月]\d{1,2})',
                r'招聘时间.*?(\d{4}[-/年]\d{1,2}[-/月]\d{1,2})',
                r'结束时间.*?(\d{4}[-/]\d{1,2}[-/]\d{1,2})',
                r'报名时间.*?(\d{4}[-/年]\d{1,2}[-/月]\d{1,2})',
            ]

            deadline = None
            for pat in deadline_patterns:
                m = re.search(pat, text)
                if m:
                    deadline = m.group(1)
                    break

            # Check if page says "已结束" or "已下架"
            is_expired = any(kw in text[:2000] for kw in ['已结束', '已下架', '已过期', '报名结束', '招聘已结束', '职位已关闭'])

            status = "❌已过期" if is_expired else ("✅进行中" if deadline else "⚠️未知")
            dl_info = f" 截止: {deadline}" if deadline else " 截止日未标注"

            print(f"{status}{dl_info} | {job['company']} | {job['title'][:40]}")
            print(f"  URL: {url}")
        except Exception as e:
            print(f"❌抓取失败 | {job['company']} | {e}")
        print()
