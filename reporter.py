"""
日报生成 - 预筛选搜索链接 + 公司监控
"""
from datetime import date
from config import TRACKS, SEARCH_LINKS, WATCH_COMPANIES, KEY_DATES


def build_report():
    """生成 HTML 日报"""
    today = date.today()
    weekday = ["一", "二", "三", "四", "五", "六", "日"][today.weekday()]

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body style="font-family:'Microsoft YaHei',sans-serif;max-width:600px;margin:0 auto;padding:0;background:#f0f2f5;">

<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:28px 24px;text-align:center;">
  <h1 style="margin:0;font-size:22px;letter-spacing:4px;">🔔 秋招日报</h1>
  <p style="margin:10px 0 0;font-size:14px;opacity:0.85;">
    {today.year}年{today.month}月{today.day}日 · 周{weekday}
  </p>
</div>

<div style="padding:20px 20px 10px;">

<!-- 一键搜索区 -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:14px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 12px;font-size:15px;color:#1a1a2e;">📌 今日岗位 · 一键直达</h2>
  <p style="margin:0 0 10px;font-size:12px;color:#888;">点击链接查看各平台最新校招岗位（已按你的路线+地点预筛选）</p>
"""

    for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
        track = TRACKS[track_name]
        links = SEARCH_LINKS.get(track_name, [])
        html += f"""
  <div style="margin-bottom:10px;">
    <span style="font-size:14px;">{track['icon']} <b>{track_name}</b></span>
    <span style="font-size:12px;color:#999;">（{', '.join(track['keywords'][:3])}...）</span>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:6px;">"""
        for link in links:
            html += f'<a href="{link["url"]}" style="display:inline-block;padding:5px 12px;background:#f0f4ff;color:#4E7282;text-decoration:none;border-radius:4px;font-size:12px;border:1px solid #d0daf0;">{link["name"]}</a>'
        html += "</div>\n"

    html += """
</div>

<!-- 重点关注公司 -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:14px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 10px;font-size:15px;color:#1a1a2e;">🏢 今日核查清单</h2>
  <p style="margin:0 0 8px;font-size:12px;color:#888;">建议每天抽查其中3-5家，看校招岗位是否更新</p>
  <div style="display:flex;flex-wrap:wrap;gap:5px;">"""

    for company in WATCH_COMPANIES:
        html += f'<a href="{company["url"]}" style="display:inline-block;padding:4px 10px;background:#fef9e7;color:#b8860b;text-decoration:none;border-radius:4px;font-size:11px;border:1px solid #f0d060;">{company["name"]}</a>'

    html += """
  </div>
</div>

<!-- 秋招节奏提醒 -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:14px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 8px;font-size:15px;color:#1a1a2e;">📅 秋招关键节点</h2>
  <ul style="margin:0;padding-left:16px;font-size:12px;color:#555;">"""

    for kd in KEY_DATES:
        html += f'<li style="margin-bottom:4px;"><b>{kd["date"]}</b>：{kd["event"]}</li>'

    html += f"""
  </ul>
</div>

<!-- 今日投递建议 -->
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:16px 20px;margin-bottom:14px;">
  <h2 style="margin:0 0 6px;font-size:15px;color:#166534;">💪 今日投递建议</h2>
  <p style="margin:0;font-size:12px;color:#444;line-height:1.8;">
    📮 建议今日投递：<b>10-15 家</b><br>
    🎯 投递比例：电商运营 40% | 新媒体 30% | 嵌入式 30%<br>
    📝 每次投递前：快速浏览岗位JD，微调简历关键词匹配<br>
    ⏰ 截止日期提示：关注 <b>3天内截止</b> 的岗位优先投
  </p>
</div>

</div>

<div style="text-align:center;padding:12px;font-size:10px;color:#999;">
  秋招日报 · 每日 8:00 自动生成 · 黄家俊专属
</div>

</body></html>"""

    return html
