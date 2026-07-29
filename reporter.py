"""
秋招日报 HTML 生成
"""
from datetime import date
from config import TRACK_LINKS, DAILY_PICKS, KEY_DATES


def build_report():
    today = date.today()
    weekday = ["一", "二", "三", "四", "五", "六", "日"][today.weekday()]
    total_picks = sum(len(p["picks"]) for p in DAILY_PICKS)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body style="font-family:'Microsoft YaHei',sans-serif;max-width:600px;margin:0 auto;padding:0;background:#f0f2f5;">

<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:24px 20px;text-align:center;">
  <h1 style="margin:0;font-size:22px;letter-spacing:4px;">🔔 秋招日报</h1>
  <p style="margin:6px 0 0;font-size:14px;opacity:0.85;">
    {today.year}年{today.month}月{today.day}日 · 周{weekday} · {total_picks}个推荐搜索
  </p>
</div>

<div style="padding:14px 16px 6px;">

<!-- ================================================================ -->
<!-- 精选推荐 80% -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 4px;font-size:17px;color:#1a1a2e;">⭐ 今日推荐搜索</h2>
  <p style="margin:0 0 14px;font-size:11px;color:#999;">每个链接点开即显示对应岗位列表 · 登录后即可投递 · 已验证可正常访问</p>
"""

    for pick_group in DAILY_PICKS:
        tier = pick_group["tier"]
        picks = pick_group["picks"]

        if tier == "high":
            bg, border, emoji = "#f0fdf4", "#4ade80", "🟢"
        elif tier == "mid":
            bg, border, emoji = "#fefce8", "#facc15", "🟡"
        else:
            bg, border, emoji = "#eff6ff", "#93c5fd", "🔵"

        html += f"""
  <div style="margin-bottom:14px;">
    <div style="background:{bg};border-left:4px solid {border};border-radius:4px;padding:10px 14px;margin-bottom:8px;">
      <span style="font-size:15px;font-weight:bold;">{pick_group['label']}</span>
      <span style="font-size:11px;color:#999;"> · {len(picks)}个方向</span>
    </div>"""

        for p in picks:
            icon = TRACK_LINKS[p["track"]]["icon"]
            html += f"""
      <div style="margin:4px 0 4px 8px;padding:8px 12px;font-size:13px;line-height:1.7;background:#fafafa;border-radius:4px;">
        <b>{icon} {p['what']}</b><br>
        <span style="color:#666;font-size:12px;">💡 {p['why']}</span>
        <a href="{p['url']}" style="display:inline-block;margin-top:4px;padding:3px 14px;background:#4E7282;color:#fff;text-decoration:none;border-radius:4px;font-size:11px;font-weight:bold;">🔍 搜索这个方向</a>
      </div>"""
        html += "</div>\n"

    html += """
</div>

<!-- ================================================================ -->
<!-- 快捷搜索 20% -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:10px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 8px;font-size:15px;color:#1a1a2e;">🔍 三条路线 · 快捷搜索</h2>
"""

    for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
        track = TRACK_LINKS[track_name]
        html += f'<div style="margin-bottom:10px;"><span style="font-size:13px;">{track["icon"]} <b>{track_name}</b></span><br>'
        for link in track["links"]:
            html += f'<a href="{link["url"]}" style="display:inline-block;margin:2px 4px;padding:3px 10px;background:#f0f4ff;color:#4E7282;text-decoration:none;border-radius:4px;font-size:11px;border:1px solid #d0daf0;">{link["label"]}</a>'
        html += "</div>"

    html += """
</div>

<!-- ========== 今日行动 ========== -->
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:14px 20px;margin-bottom:10px;">
  <h2 style="margin:0 0 4px;font-size:14px;color:#166534;">💪 今日行动清单</h2>
  <p style="margin:0;font-size:12px;color:#444;line-height:2;">
    ⭐ 逐个点开上方推荐搜索 → 浏览岗位 → 匹配就投<br>
    📝 投递前快速匹配JD关键词，微调简历1-2处<br>
    📊 今日目标：<b>10-15家</b>｜已投：___ 家<br>
    📍 Boss直聘记得手动切换城市：深圳/广州/东莞/杭州/成都/长沙<br>
    🏫 额外关注学校就业网/双选会通知
  </p>
</div>

<!-- ========== 时间线 ========== -->
<div style="background:#fff;border-radius:10px;padding:14px 20px;margin-bottom:10px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 6px;font-size:14px;color:#1a1a2e;">📅 秋招时间线</h2>"""

    for kd in KEY_DATES:
        html += f'<div style="font-size:11px;margin-bottom:3px;color:#555;"><b>{kd["date"]}</b>：{kd["event"]}</div>'

    html += f"""
</div>

</div>

<div style="text-align:center;padding:8px;font-size:10px;color:#bbb;">
  秋招日报 · 每日 8:00 · 黄家俊专属 · 链接已验证可打开
</div>

</body></html>"""

    return html
