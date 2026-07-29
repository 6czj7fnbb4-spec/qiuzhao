"""
日报生成模块 - 输出 HTML 邮件内容
"""
from datetime import date, timedelta


TIER_NAMES = {
    "reach": "🟡 可以冲一冲",
    "safe": "🟢 稳拿到",
    "chance": "🔵 概率小但有机会",
}

TRACK_ICONS = {
    "嵌入式/硬件工程师": "🔧",
    "电商运营": "🛒",
    "新媒体运营": "📱",
}


def build_report(classified, stats):
    """生成 HTML 日报"""
    today = date.today()
    weekday = ["一", "二", "三", "四", "五", "六", "日"][today.weekday()]

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body style="font-family:'Microsoft YaHei',sans-serif;max-width:650px;margin:0 auto;padding:16px;background:#f5f6f8;">

<!-- 头部 -->
<div style="background:#1a1a2e;color:#fff;padding:24px 20px;border-radius:10px 10px 0 0;text-align:center;">
  <h1 style="margin:0;font-size:22px;">🔔 秋招日报</h1>
  <p style="margin:6px 0 0;font-size:13px;opacity:0.8;">
    {today.year}年{today.month}月{today.day}日 · 周{weekday}
  </p>
</div>

<div style="background:#fff;padding:20px;border-radius:0 0 10px 10px;">
"""

    # 统计概览
    html += """<div style="background:#f0f4ff;padding:12px 16px;border-radius:8px;margin-bottom:20px;">
  <strong>📊 今日岗位统计</strong><br>"""
    for track, tiers in classified.items():
        total = sum(len(v) for v in tiers.values())
        html += f'  {TRACK_ICONS.get(track,"")} {track}：<b>{total}</b> 个新岗位　'
    html += "</div>"

    # 逐路线、逐档展示
    has_any = False
    for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
        tiers = classified.get(track_name, {})
        track_total = sum(len(v) for v in tiers.values())
        if track_total == 0:
            continue
        has_any = True

        html += f"""
<div style="margin-bottom:20px;">
  <h2 style="font-size:16px;border-bottom:2px solid #4E7282;padding-bottom:4px;color:#2c2c2c;">
    {TRACK_ICONS.get(track_name, '')} {track_name}
  </h2>
"""
        for tier_key in ["reach", "safe", "chance"]:
            jobs = tiers.get(tier_key, [])
            if not jobs:
                continue
            html += f"""
  <div style="margin:8px 0 4px;font-weight:bold;font-size:14px;color:#555;">
    {TIER_NAMES[tier_key]} <span style="color:#999;">({len(jobs)}个)</span>
  </div>
"""
            for j in jobs[:8]:  # 每档最多显示 8 条
                company = j.get("company", "") or j.get("title", "")
                title = j.get("title", "")
                deadline = j.get("deadline", "")
                link = j.get("link", "")
                source = j.get("source", "")

                deadline_html = ""
                if deadline:
                    deadline_html = f' <span style="color:#e74c3c;font-size:11px;">⏰ {deadline}</span>'

                link_html = ""
                if link:
                    link_html = f' <a href="{link}" style="color:#4E7282;font-size:11px;text-decoration:none;">[投递➚]</a>'

                html += f"""
  <div style="padding:6px 10px;margin:3px 0;background:#fafafa;border-left:3px solid #ddd;border-radius:3px;font-size:13px;">
    {company} · {title}　{deadline_html}　{link_html}
  </div>"""

        html += "</div>"

    if not has_any:
        html += """<div style="text-align:center;padding:30px;color:#999;">
  😴 今日暂无匹配岗位，可能招聘平台尚未更新或网络波动。
  <br>系统明天会继续为你搜索，不用慌！
</div>"""

    # 尾部
    html += f"""
</div>

<div style="text-align:center;padding:16px;font-size:11px;color:#999;">
  秋招日报 · 每日 {today.strftime('%H:%M')} 自动生成 · 仅为你推送匹配岗位<br>
  路线：{', '.join(TRACK_ICONS.get(k,'')+k for k in ['电商运营','新媒体运营','嵌入式/硬件工程师'])}
</div>

</body></html>"""

    return html
