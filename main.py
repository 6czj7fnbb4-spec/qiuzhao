"""
秋招日报 - 主入口
每天早上 8:00 由 GitHub Actions 触发执行
"""
import sys
from datetime import datetime

from scrapers.nowcoder import scrape_nowcoder
from scrapers.yingjiesheng import scrape_yingjiesheng
from filters import filter_and_classify
from reporter import build_report
from mailer import send_report


def main():
    print(f"[秋招日报] 开始执行 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 1. 抓取各平台岗位
    print("\n[1/4] 正在抓取岗位数据...")
    all_jobs = []
    all_jobs.extend(scrape_nowcoder())
    all_jobs.extend(scrape_yingjiesheng())
    print(f"[1/4] 共抓取原始岗位 {len(all_jobs)} 个")

    if not all_jobs:
        print("[警告] 没有抓到任何岗位，可能是网络问题或平台改版")
        # 即使没有数据也发一封提醒邮件
        html = """
        <h2>😴 秋招日报 - 今日无更新</h2>
        <p>今天未能从招聘平台获取数据，可能原因：</p>
        <ul>
          <li>平台反爬机制临时升级</li>
          <li>网络波动导致抓取失败</li>
          <li>平台页面结构有变动</li>
        </ul>
        <p>系统明天会继续尝试，不用担心~</p>
        """
        send_report(html)
        return

    # 2. 筛选 + 三档分类
    print("\n[2/4] 正在筛选匹配...")
    classified = filter_and_classify(all_jobs)
    total_matched = sum(
        sum(len(v) for v in tiers.values())
        for tiers in classified.values()
    )
    print(f"[2/4] 匹配到 {total_matched} 个相关岗位")

    # 3. 统计
    stats = {}
    for track, tiers in classified.items():
        stats[track] = {k: len(v) for k, v in tiers.items()}

    # 4. 生成日报并发送
    print("\n[3/4] 正在生成日报...")
    html = build_report(classified, stats)
    print(f"[3/4] 日报生成完成 ({len(html)} 字符)")

    print("\n[4/4] 正在发送邮件...")
    success = send_report(html)

    if success:
        print(f"\n✅ 完成! 日报已发送到 1228358378@qq.com")
    else:
        print(f"\n❌ 邮件发送失败，请检查 SMTP 配置")
        sys.exit(1)


if __name__ == "__main__":
    main()
