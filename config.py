"""
秋招日报 - 配置
新媒体+电商=70%  嵌入式=30%  全部2027届
"""
import os

EMAIL_CONFIG = {
    "smtp_host": "smtp.qq.com",
    "smtp_port": 465,
    "sender": "1228358378@qq.com",
    "password": os.environ.get("QQ_SMTP_PASSWORD", ""),
    "receiver": "1228358378@qq.com",
}

# 新媒体+电商 = 70%，嵌入式 = 30%
FEATURED_JOBS = {
    "high": {
        "label": "🟢 70-90% 能拿到面试",
        "desc": "你的实习/项目经验直接对口，概率最高",
        "jobs": [
            # === 电商运营 ===
            {
                "track": "电商运营",
                "title": "商品运营管培生 / 运营管培生",
                "company": "拼多多 PDD",
                "location": "上海",
                "type": "2027届提前批",
                "deadline": "⏰ 8月23日截止",
                "why": "你的淘宝/1688双平台运营经验直接对口，提前批不影响正式批",
                "url": "https://careers.pddglobalhr.com/campus",
            },
            # === 新媒体运营 ===
            {
                "track": "新媒体运营",
                "title": "视频创意制作",
                "company": "拼多多 PDD",
                "location": "上海",
                "type": "2027届提前批",
                "deadline": "⏰ 8月23日截止",
                "why": "短视频全流程经验，从脚本到剪辑到投放你都做过",
                "url": "https://careers.pddglobalhr.com/campus",
            },
            # === 嵌入式 ===
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件工程师 / 电力电子硬件工程师",
                "company": "深圳市正浩创新科技",
                "location": "深圳南山",
                "type": "2027届研发提前批",
                "deadline": "⏰ 见岗位页",
                "why": "电子/嵌入式专业对口，中小厂竞争压力小",
                "url": "https://guet.ncss.cn/student/jobs/Nhn3AZULWjDEhWfCG9Qg2v/detail.html",
            },
        ],
    },
    "mid": {
        "label": "🟡 40-60% 能拿到面试",
        "desc": "经验能加分，重点投 · 新媒体+电商为主",
        "jobs": [
            # === 新媒体运营 ===
            {
                "track": "新媒体运营",
                "title": "直播运营 / 短视频编导 / 新媒体运营",
                "company": "好未来集团（学而思）",
                "location": "北京",
                "type": "2027届暑期实习（可转正）",
                "deadline": "⏰ 见岗位页",
                "why": "含直播+短视频+电商多方向，自媒体数据可当作品集",
                "url": "https://vy.ncss.cn/student/jobs/QgTTqE4vna6Zuc6XBGve3s/detail.html",
            },
            # === 电商运营 ===
            {
                "track": "电商运营",
                "title": "营销族储备实习生（电商/内容方向）",
                "company": "安克创新 Anker",
                "location": "深圳 / 杭州",
                "type": "2027届储备实习（可转正）",
                "deadline": "⏰ 全年滚动招聘",
                "why": "全球化品牌，深圳杭州有岗，实习转正率高",
                "url": "https://career.anker.com.cn",
            },
            # === 新媒体运营 ===
            {
                "track": "新媒体运营",
                "title": "游戏营销策划（抖音/快手/KOL方向）",
                "company": "某游戏公司",
                "location": "全国",
                "type": "2027届秋招",
                "deadline": "⏰ 见牛客网岗位页",
                "why": "抖音/快手/KOL推广+内容策划，新媒体运营方向",
                "url": "https://www.nowcoder.com/jobs/detail/454344",
            },
            # === 嵌入式 ===
            {
                "track": "嵌入式/硬件工程师",
                "title": "暑期实习生（芯片/硬件/智能机器人）",
                "company": "小鹏集团",
                "location": "广州 / 深圳",
                "type": "2027届实习（可转正）",
                "deadline": "⏰ 见岗位页",
                "why": "广州深圳有岗，实习门槛低于校招",
                "url": "https://3120ww.ncss.cn/student/m/jobs/KNiqQo5vuXpynyTGvurVQX/detail.html",
            },
        ],
    },
    "low": {
        "label": "🔵 10-30% 能拿到面试",
        "desc": "大厂/学历门槛高，投了不亏",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式硬件/软件工程师",
                "company": "宇树科技",
                "location": "杭州",
                "type": "2027届校招",
                "deadline": "⏰ 见岗位页",
                "why": "机器人赛道热门，嵌入式软硬件方向",
                "url": "https://fg.ncss.cn/student/jobs/6JsdAwQiZpBp4iLcXErRFh/detail.html",
            },
        ],
    },
}

QUICK_SEARCHES = [
    {"label": "Boss直聘 · 电商运营应届", "url": "https://www.zhipin.com/web/geek/job?query=电商运营%20平台运营&experience=401&degree=203"},
    {"label": "Boss直聘 · 新媒体运营应届", "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20内容运营&experience=401&degree=203"},
    {"label": "Boss直聘 · 嵌入式应届", "url": "https://www.zhipin.com/web/geek/job?query=嵌入式工程师%20硬件工程师&experience=401&degree=203"},
    {"label": "拼多多校招官网", "url": "https://careers.pddglobalhr.com/campus"},
    {"label": "安克创新校招", "url": "https://career.anker.com.cn"},
    {"label": "国家就业平台", "url": "https://www.ncss.cn/student/jobs/index.html"},
]

KEY_DATES = [
    {"date": "7月-8月中旬", "event": "提前批高峰期！拼多多8.23截止，现在立刻投"},
    {"date": "8月中旬-9月", "event": "秋招正式批大规模启动，岗位暴增"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
