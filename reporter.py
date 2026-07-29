"""
秋招日报 HTML 生成
"""
from datetime import date
from config import FEATURED_JOBS, SEARCH_LINKS, KEY_DATES


def build_report():
    today = date.today()
    weekday = ["一", "二", "三", "四", "五", "六", "日"][today.weekday()]

    # 统计
    total_featured = sum(len(tier["jobs"]) for tier in FEATURED_JOBS.values())

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body style="font-family:'Microsoft YaHei',sans-serif;max-width:600px;margin:0 auto;padding:0;background:#f0f2f5;">

<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:26px 24px;text-align:center;">
  <h1 style="margin:0;font-size:22px;letter-spacing:4px;">🔔 秋招日报</h1>
  <p style="margin:8px 0 0;font-size:14px;opacity:0.85;">{today.year}年{today.month}月{today.day}日 · 周{weekday} · 精选{total_featured}个岗位</p>
</div>

<div style="padding:14px 16px 6px;">

<!-- ================================================================ -->
<!-- 精选岗位 - 占80%篇幅 -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 2px;font-size:17px;color:#1a1a2e;">⭐ 今日精选岗位</h2>
  <p style="margin:0 0 14px;font-size:11px;color:#999;">全部真实校招岗位 · 点击「投递➚」直达投递页面 · 非公司官网</p>
"""

    # 按三档输出：high -> mid -> low
    for tier_key in ["high", "mid", "low"]:
        tier = FEATURED_JOBS[tier_key]
        job_count = len(tier["jobs"])

        # 档位标题样式随档位变化
        if tier_key == "high":
            bg, border = "#f0fdf4", "#4ade80"
        elif tier_key == "mid":
            bg, border = "#fefce8", "#facc15"
        else:
            bg, border = "#eff6ff", "#93c5fd"

        html += f"""
  <div style="margin-bottom:14px;">
    <div style="background:{bg};border:1px solid {border};border-radius:6px;padding:8px 12px;margin-bottom:6px;">
      <span style="font-size:14px;font-weight:bold;">{tier['label']}</span>
      <span style="font-size:11px;color:#888;margin-left:6px;">（{job_count}个岗位）</span>
      <span style="font-size:11px;color:#999;">— {tier['desc']}</span>
    </div>"""

        # Group jobs by track within each tier
        for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
            track_jobs = [j for j in tier["jobs"] if j["track"] == track_name]
            if not track_jobs:
                continue
            icon = SEARCH_LINKS[track_name]["icon"]
            html += f'<div style="margin:2px 0 4px 6px;font-size:12px;color:#666;">{icon} {track_name}</div>'

            for job in track_jobs:
                scale_str = f' · {job["scale"]}' if job.get("scale") else ""
                salary_str = f'<br><span style="color:#888;">💰 {job["salary"]}</span>' if job.get("salary") else ""
                match_str = f'<br><span style="color:#666;font-size:11px;">🎯 {job["match"]}</span>' if job.get("match") else ""

                html += f"""
      <div style="padding:7px 10px;margin:2px 0 2px 10px;background:#fafafa;border-left:3px solid {border};border-radius:3px;font-size:12.5px;">
        <a href="{job['url']}" style="color:#2c2c2c;text-decoration:none;font-weight:bold;">{job['title']}</a>
        <span style="color:#888;"> · {job['company']}</span>
        <span style="color:#555;">📍{job['location']}</span>{scale_str}
        <a href="{job['url']}" style="display:inline-block;margin-left:4px;padding:1px 7px;background:#4E7282;color:#fff;text-decoration:none;border-radius:3px;font-size:10px;">投递➚</a>
        {salary_str}{match_str}
      </div>"""
        html += "</div>\n"

    # 投递策略提示
    html += f"""
  <div style="background:#fef9e7;border:1px solid #f0d060;border-radius:6px;padding:10px 14px;margin-top:8px;font-size:12px;color:#555;line-height:1.8;">
    <b>📋 投递策略：</b>先投🟡档（你的主战场），再投🟢档（保底），最后投🔵档（随手一搏）。<br>
    <b>💰 薪资参考：</b>嵌入式 7-22K | 电商运营 7-18K | 新媒体 6-13K（本科非985/211参考offershow）
  </div>

</div>

<!-- ================================================================ -->
<!-- 一键搜索区 - 占20%篇幅 -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:10px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 6px;font-size:15px;color:#1a1a2e;">🔍 一键搜索更多岗位</h2>
  <p style="margin:0 0 8px;font-size:11px;color:#999;">精选岗位不够看？点下面链接，每天都有新岗位上线</p>
"""

    for track_name in ["电商运营", "新媒体运营", "嵌入式/硬件工程师"]:
        track = SEARCH_LINKS[track_name]
        html += f'<span style="font-size:12px;">{track["icon"]} <b>{track_name}</b></span>　'
        links_html = []
        for s in track["searches"]:
            links_html.append(f'<a href="{s["url"]}" style="color:#4E7282;font-size:11px;">{s["label"]}</a>')
        html += " · ".join(links_html) + "<br>"

    html += """
</div>

<!-- ========== 行动清单 ========== -->
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:14px 20px;margin-bottom:10px;">
  <h2 style="margin:0 0 4px;font-size:14px;color:#166534;">💪 今日行动清单</h2>
  <p style="margin:0;font-size:12px;color:#444;line-height:2;">
    ⭐ 优先投上方精选岗位（尤其🟡档）<br>
    🔍 点「一键搜索」浏览今日最新发布<br>
    📝 每次投递前微调简历关键词匹配JD<br>
    📊 建议今日投递 <b>10-15 家</b>｜已投：___ 家<br>
    🏫 关注学校双选会/宣讲会（竞争仅限本校，机会最大）
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
  秋招日报 · 每日 8:00 自动发送 · 黄家俊专属 · {total_featured}个精选岗位
</div>

</body></html>"""

    return html
