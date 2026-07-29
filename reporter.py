"""
秋招日报 HTML 生成
"""
from datetime import date
from config import TRACK_SEARCHES, FEATURED_JOBS, KEY_DATES


def build_report():
    today = date.today()
    weekday = ["一", "二", "三", "四", "五", "六", "日"][today.weekday()]

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body style="font-family:'Microsoft YaHei',sans-serif;max-width:600px;margin:0 auto;padding:0;background:#f0f2f5;">

<!-- 头部 -->
<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:28px 24px;text-align:center;">
  <h1 style="margin:0;font-size:22px;letter-spacing:4px;">🔔 秋招日报</h1>
  <p style="margin:10px 0 0;font-size:14px;opacity:0.85;">{today.year}年{today.month}月{today.day}日 · 周{weekday}</p>
</div>

<div style="padding:16px 16px 8px;">

<!-- ========== 精选岗位（具体可投） ========== -->
<div style="background:#fff;border-radius:10px;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 4px;font-size:16px;color:#1a1a2e;">⭐ 今日精选岗位（可直投）</h2>
  <p style="margin:0 0 12px;font-size:11px;color:#999;">人工筛选匹配你简历的岗位，点链接直接投递</p>
"""

    # Group featured jobs by track
    for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
        track_jobs = [j for j in FEATURED_JOBS if j["track"] == track_name]
        if not track_jobs:
            continue
        icon = TRACK_SEARCHES[track_name]["icon"]
        html += f'<div style="margin-bottom:10px;"><span style="font-size:14px;">{icon} <b>{track_name}</b></span></div>'
        for job in track_jobs:
            deadline_str = f' ⏰{job["deadline"]}' if job.get("deadline") else ""
            salary_str = f' 💰{job["salary"]}' if job.get("salary") else ""
            note_str = f'<br><span style="color:#888;font-size:11px;">💡 {job["note"]}</span>' if job.get("note") else ""
            html += f"""
  <div style="padding:8px 12px;margin:4px 0;background:#fefdf5;border-left:3px solid #f0c040;border-radius:3px;font-size:13px;">
    <a href="{job['url']}" style="color:#2c2c2c;text-decoration:none;font-weight:bold;">{job['title']}</a>
    <span style="color:#888;">· {job['company']}</span>
    <span style="color:#555;">📍{job['location']}</span>{salary_str}{deadline_str}
    <a href="{job['url']}" style="display:inline-block;margin-left:6px;padding:2px 8px;background:#4E7282;color:#fff;text-decoration:none;border-radius:3px;font-size:11px;">投递➚</a>
    {note_str}
  </div>"""

    html += """
</div>

<!-- ========== 一键搜索区 ========== -->
<div style="background:#fff;border-radius:10px;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 4px;font-size:16px;color:#1a1a2e;">🔍 一键搜索今日岗位</h2>
  <p style="margin:0 0 12px;font-size:11px;color:#999;">每个链接打开即显示该路线的校招岗位列表，按需投递</p>
"""

    for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
        track = TRACK_SEARCHES[track_name]
        html += f"""
  <div style="margin-bottom:12px;">
    <span style="font-size:14px;">{track['icon']} <b>{track_name}</b></span>
  </div>"""
        for s in track["searches"]:
            html += f"""
  <div style="margin:3px 0 3px 16px;font-size:12px;">
    ➤ <a href="{s['url']}" style="color:#4E7282;">{s['label']}</a><span style="color:#aaa;"> — {s['desc']}</span>
  </div>"""

    html += """
</div>

<!-- ========== 投递建议 ========== -->
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:16px 20px;margin-bottom:12px;">
  <h2 style="margin:0 0 6px;font-size:15px;color:#166534;">💪 今日行动清单</h2>
  <p style="margin:0;font-size:12px;color:#444;line-height:2;">
    📮 打开上方「一键搜索」链接，浏览今日最新岗位<br>
    ⭐ 优先投递「精选岗位」中匹配度最高的<br>
    📝 每次投递前微调简历关键词匹配JD<br>
    📊 建议今日投递 <b>10-15 家</b>（电商4 : 新媒体3 : 嵌入式3）<br>
    ⏰ 特别关注 <b>3天内截止</b> 的岗位优先投
  </p>
</div>

<!-- ========== 秋招节奏 ========== -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 8px;font-size:15px;color:#1a1a2e;">📅 秋招关键节点</h2>
  <ul style="margin:0;padding-left:16px;font-size:12px;color:#555;">"""

    for kd in KEY_DATES:
        html += f'<li style="margin-bottom:4px;"><b>{kd["date"]}</b>：{kd["event"]}</li>'

    html += f"""
  </ul>
</div>

</div>

<div style="text-align:center;padding:10px;font-size:10px;color:#aaa;">
  秋招日报 · 每日 8:00 自动生成 · 黄家俊专属
</div>

</body></html>"""

    return html
