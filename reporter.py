"""
秋招日报 HTML 生成
"""
from datetime import date
from config import FEATURED_JOBS, QUICK_SEARCHES, KEY_DATES


def build_report():
    today = date.today()
    weekday = ["一", "二", "三", "四", "五", "六", "日"][today.weekday()]

    total = sum(len(t["jobs"]) for t in FEATURED_JOBS.values())

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body style="font-family:'Microsoft YaHei',sans-serif;max-width:600px;margin:0 auto;padding:0;background:#f0f2f5;">

<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:26px 24px;text-align:center;">
  <h1 style="margin:0;font-size:22px;letter-spacing:4px;">🔔 秋招日报</h1>
  <p style="margin:8px 0 0;font-size:14px;opacity:0.85;">{today.year}年{today.month}月{today.day}日 · 周{weekday} · {total}个搜索指南</p>
</div>

<div style="padding:14px 16px 6px;">

<!-- ================================================================ -->
<!-- 精选岗位 - 80% -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 4px;font-size:17px;color:#1a1a2e;">⭐ 今日推荐搜索</h2>
  <p style="margin:0 0 14px;font-size:11px;color:#999;">按你的三条路线 + 学历实际 + 面试概率筛选 · 点链接 → 登录牛客网 → 浏览岗位 → 投递</p>
"""

    # 三档输出
    for tier_key in ["high", "mid", "low"]:
        tier = FEATURED_JOBS[tier_key]
        job_count = len(tier["jobs"])

        if tier_key == "high":
            bg, border, badge = "#f0fdf4", "#4ade80", "🟢"
        elif tier_key == "mid":
            bg, border, badge = "#fefce8", "#facc15", "🟡"
        else:
            bg, border, badge = "#eff6ff", "#93c5fd", "🔵"

        html += f"""
  <div style="margin-bottom:14px;">
    <div style="background:{bg};border-left:4px solid {border};border-radius:4px;padding:8px 12px;margin-bottom:8px;">
      <span style="font-size:14px;font-weight:bold;">{tier['label']}</span>
      <span style="font-size:11px;color:#888;"> · {job_count}个方向</span>
      <span style="font-size:11px;color:#999;"> · {tier['desc']}</span>
    </div>"""

        for job in tier["jobs"]:
            html += f"""
      <div style="margin:3px 0 3px 8px;padding:7px 10px;font-size:12.5px;line-height:1.7;border-bottom:1px solid #f0f0f0;">
        <b>{job['what']}</b><br>
        <span style="color:#888;">🔍 {job['where']}</span><br>
        <span style="color:#666;">💡 {job['why']}</span>
        <a href="{job['search_url']}" style="display:inline-block;margin-top:3px;padding:2px 10px;background:#4E7282;color:#fff;text-decoration:none;border-radius:3px;font-size:11px;">搜索➚</a>
      </div>"""
        html += "</div>\n"

    # 投递策略
    html += f"""
  <div style="background:#fef9e7;border:1px solid #f0d060;border-radius:6px;padding:10px 14px;margin-top:6px;font-size:12px;color:#555;line-height:1.8;">
    <b>📋 今日策略：</b>先搜🟡档（你的主战场），再搜🟢档（保底），最后🔵档（随手一搏）<br>
    <b>📍 城市筛选：</b>牛客网/Boss直聘里手动筛 深圳/广州/东莞/杭州/成都/长沙<br>
    <b>💰 薪资参考（本科非985/211）：</b>嵌入式 7-22K | 电商运营 7-18K | 新媒体 6-13K
  </div>

</div>

<!-- ================================================================ -->
<!-- 快捷搜索 - 20% -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:10px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 8px;font-size:15px;color:#1a1a2e;">🔍 快捷搜索入口</h2>
  <div style="display:flex;flex-wrap:wrap;gap:6px;">"""

    for qs in QUICK_SEARCHES:
        html += f'<a href="{qs["url"]}" style="display:inline-block;padding:5px 12px;background:#f0f4ff;color:#4E7282;text-decoration:none;border-radius:4px;font-size:11px;border:1px solid #d0daf0;">{qs["label"]}</a>'

    html += """
  </div>
</div>

<!-- ========== 行动清单 ========== -->
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:14px 20px;margin-bottom:10px;">
  <h2 style="margin:0 0 4px;font-size:14px;color:#166534;">💪 今日行动清单</h2>
  <p style="margin:0;font-size:12px;color:#444;line-height:2;">
    ⭐ 打开上方推荐搜索 → 登录牛客网 → 浏览岗位 → 一键投递<br>
    🔍 每条搜索点开后，按「最新发布」排序，优先投今天发布的<br>
    📝 投递前打开简历，快速匹配JD里的关键词（微调1-2处即可）<br>
    📊 建议今日投递 <b>10-15 家</b>｜已投：___ 家<br>
    🏫 额外关注：学校就业网/双选会/辅导员群通知
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
  秋招日报 · 每日 8:00 · 黄家俊专属 · {total}个搜索方向
</div>

</body></html>"""

    return html
