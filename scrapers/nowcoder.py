"""
牛客网校招日程爬虫
"""
import requests
from bs4 import BeautifulSoup
from config import SCRAPER_CONFIG


def scrape_nowcoder():
    """抓取牛客网校招日程，返回岗位列表"""
    jobs = []
    try:
        # 牛客网校招日程页
        url = SCRAPER_CONFIG["nowcoder"]["schedule_url"]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        resp = requests.get(url, headers=headers, timeout=15)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "lxml")

        # 牛客网校招日程用表格展示：公司/招聘类型/截止日期/详情
        # 查找表格行
        rows = soup.select("table tbody tr")
        if not rows:
            rows = soup.select(".schedule-table tr")
        if not rows:
            rows = soup.select("tr[class*='row']")

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 3:
                continue
            company = cols[0].get_text(strip=True)
            job_type = cols[1].get_text(strip=True) if len(cols) > 1 else ""
            deadline = cols[2].get_text(strip=True) if len(cols) > 2 else ""
            link = ""
            a_tag = row.find("a")
            if a_tag and a_tag.get("href"):
                link = a_tag["href"]
                if link.startswith("/"):
                    link = SCRAPER_CONFIG["nowcoder"]["base_url"] + link

            jobs.append({
                "company": company,
                "title": job_type,
                "deadline": deadline,
                "link": link,
                "source": "牛客网",
            })

        print(f"[牛客网] 抓到 {len(jobs)} 条记录")
    except Exception as e:
        print(f"[牛客网] 抓取失败: {e}")

    return jobs


if __name__ == "__main__":
    results = scrape_nowcoder()
    for j in results[:10]:
        print(j)
