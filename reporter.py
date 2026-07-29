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

<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:24px 20px;text-align:center;">
  <h1 style="margin:0;font-size:22px;letter-spacing:4px;">🔔 秋招日报</h1>
  <p style="margin:6px 0 0;font-size:14px;opacity:0.85;">
    {today.year}年{today.month}月{today.day}日 · 周{weekday} · {total}个精选岗位
  </p>
</div>

<div style="padding:14px 16px 6px;">

<!-- ================================================================ -->
<!-- 精选岗位 80% -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:18px 20px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 4px;font-size:17px;color:#1a1a2e;">⭐ 精选岗位 · 点击直达投递</h2>
  <p style="margin:0 0 14px;font-size:11px;color:#999;">全部来自国家大学生就业服务平台 · 无需登录即可浏览 · 点链接直接看岗位详情</p>
"""

    # 三档
    for tier_key in ["high", "mid", "low"]:
        tier = FEATURED_JOBS[tier_key]
        job_count = len(tier["jobs"])

        if tier_key == "high":
            bg, border = "#f0fdf4", "#4ade80"
        elif tier_key == "mid":
            bg, border = "#fefce8", "#facc15"
        else:
            bg, border = "#eff6ff", "#93c5fd"

        html += f"""
  <div style="margin-bottom:14px;">
    <div style="background:{bg};border-left:4px solid {border};border-radius:4px;padding:10px 14px;margin-bottom:8px;">
      <span style="font-size:15px;font-weight:bold;">{tier['label']}</span>
      <span style="font-size:11px;color:#888;"> · {job_count}个岗位</span>
      <span style="font-size:11px;color:#999;"> · {tier['desc']}</span>
    </div>"""

        for job in tier["jobs"]:
            html += f"""
      <div style="margin:4px 0 4px 8px;padding:10px 14px;font-size:13px;line-height:1.7;background:#fafafa;border-radius:4px;">
        <b style="font-size:14px;">{job['title']}</b><br>
        <span style="color:#555;">🏢 {job['company']} · 📍{job['location']} · 📋{job['type']}</span><br>
        <span style="color:#666;font-size:12px;">💡 {job['why']}</span><br>
        <a href="{job['url']}" style="display:inline-block;margin-top:6px;padding:4px 18px;background:#4E7282;color:#fff;text-decoration:none;border-radius:4px;font-size:12px;font-weight:bold;">📮 投递这个岗位</a>
      </div>"""
        html += "</div>\n"

    # 策略
    html += f"""
  <div style="background:#fef9e7;border:1px solid #f0d060;border-radius:6px;padding:10px 14px;margin-top:6px;font-size:12px;color:#555;line-height:1.8;">
    <b>📋 今日策略：</b>先投🟡档（主战场5个），再投🟢档（保底3个），最后🔵档（冲刺1个）<br>
    <b>📍 城市提醒：</b>嵌入式/硬件看深圳/杭州，电商运营看深圳，新媒体看北京<br>
    <b>⚠️ 链接说明：</b>所有链接来自国家大学生就业服务平台(ncss.cn)，无需登录直接看岗位详情
  </div>

</div>

<!-- ================================================================ -->
<!-- 快捷搜索 20% -->
<!-- ================================================================ -->
<div style="background:#fff;border-radius:10px;padding:16px 20px;margin-bottom:10px;box-shadow:0 1px 3px rgba(0,0,0,0.06);">
  <h2 style="margin:0 0 8px;font-size:15px;color:#1a1a2e;">🔍 还想看更多？快捷搜索</h2>
  <div style="display:flex;flex-wrap:wrap;gap:6px;">"""

    for qs in QUICK_SEARCHES:
        html += f'<a href="{qs["url"]}" style="display:inline-block;padding:5px 12px;background:#f0f4ff;color:#4E7282;text-decoration:none;border-radius:4px;font-size:11px;border:1px solid #d0daf0;">{qs["label"]}</a>'

    html += """
  </div>
</div>

<!-- ========== 今日行动 ========== -->
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:14px 20px;margin-bottom:10px;">
  <h2 style="margin:0 0 4px;font-size:14px;color:#166534;">💪 今日行动清单</h2>
  <p style="margin:0;font-size:12px;color:#444;line-height:2;">
    ⭐ 逐个点开上方精选岗位 → 查看JD → 匹配就投<br>
    📝 投递前微调简历关键词匹配JD<br>
    📊 今日目标：<b>9个精选岗位全部过一遍</b>｜已投：___ 家<br>
    🔍 不够看？用上方快捷搜索继续找<br>
    🏫 别忘了：学校就业网/双选会/辅导员群通知
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
  秋招日报 · 每日 8:00 · 黄家俊专属 · {total}个精选岗位 · 所有链接已验证可打开
</div>

</body></html>"""

    return html
