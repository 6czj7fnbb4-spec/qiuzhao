"""
邮件发送模块 - 通过 QQ SMTP 发送日报
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG


def send_report(html_content):
    """发送 HTML 日报邮件"""
    config = EMAIL_CONFIG
    if not config["password"]:
        print("[邮件] 警告：SMTP 密码未设置，跳过发送")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🔔 秋招日报 | 新岗位已更新"
    msg["From"] = config["sender"]
    msg["To"] = config["receiver"]

    msg.attach(MIMEText(html_content, "html", "utf-8"))

    try:
        with smtplib.SMTP_SSL(config["smtp_host"], config["smtp_port"]) as server:
            server.login(config["sender"], config["password"])
            server.sendmail(config["sender"], config["receiver"], msg.as_string())
        print("[邮件] 日报发送成功 ✅")
        return True
    except Exception as e:
        print(f"[邮件] 发送失败: {e}")
        return False
