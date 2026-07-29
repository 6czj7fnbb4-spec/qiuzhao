"""
应届生求职网爬虫
"""
import requests
from bs4 import BeautifulSoup
from config import SCRAPER_CONFIG


def scrape_yingjiesheng():
    """抓取应届生求职网最新校招信息"""
    jobs = []
    try:
        base = SCRAPER_CONFIG["yingjiesheng"]["base_url"]
        # 校招信息页
        urls = [
            f"{base}/comm/search?s=0&k=%E6%A0%A1%E6%8B%9B",
            f"{base}/comm/search?s=0&k=%E5%BA%94%E5%B1%8A",
        ]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        seen = set()
        for url in urls:
            try:
                resp = requests.get(url, headers=headers, timeout=15)
                resp.encoding = "gb2312"
                soup = BeautifulSoup(resp.text, "lxml")

                # 查找职位列表
                items = soup.select(".job_list li, .info_li, .result_list li")
                if not items:
                    items = soup.select("ul li a[href*='job']")

                for item in items:
                    a_tag = item.find("a") if item.name != "a" else item
                    if not a_tag:
                        continue
                    title = a_tag.get_text(strip=True)
                    link = a_tag.get("href", "")
                    if not title or not link:
                        continue
                    if link.startswith("/"):
                        link = base + link

                    key = title + link
                    if key in seen:
                        continue
                    seen.add(key)

                    # 尝试提取公司和日期
                    parent_text = item.get_text(strip=True) if item.name != "a" else ""
                    company = ""
                    deadline = ""
                    if "—" in parent_text:
                        parts = parent_text.split("—")
                        if len(parts) >= 2:
                            company = parts[0].strip()
                            deadline = parts[-1].strip()

                    jobs.append({
                        "company": company,
                        "title": title,
                        "deadline": deadline,
                        "link": link,
                        "source": "应届生求职网",
                    })

                print(f"[应届生求职网] {url} 抓到 {len(jobs)} 条")
            except Exception as e:
                print(f"[应届生求职网] {url} 抓取失败: {e}")
                continue

    except Exception as e:
        print(f"[应届生求职网] 整体失败: {e}")

    return jobs


if __name__ == "__main__":
    results = scrape_yingjiesheng()
    for j in results[:10]:
        print(j)
