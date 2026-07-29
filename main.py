"""
秋招日报 - 主入口
每天早上 8:00 由 GitHub Actions 触发执行
"""
from datetime import datetime
from reporter import build_report
from mailer import send_report


def main():
    print(f"[秋招日报] 开始执行 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 生成日报 HTML
    html = build_report()
    print(f"[生成] 日报 HTML {len(html)} 字符")

    # 发送邮件
    print("[发送] 正在发送邮件...")
    success = send_report(html)

    if success:
        print("✅ 日报发送成功！")
    else:
        print("❌ 发送失败，请检查 QQ_SMTP_PASSWORD 密钥是否正确配置")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
