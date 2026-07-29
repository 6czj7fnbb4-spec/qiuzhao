"""
秋招日报 - 配置
所有岗位链接来自 ncss.cn（国家大学生就业服务平台）
已验证：无需登录，点击直达岗位详情页
"""
import os

EMAIL_CONFIG = {
    "smtp_host": "smtp.qq.com",
    "smtp_port": 465,
    "sender": "1228358378@qq.com",
    "password": os.environ.get("QQ_SMTP_PASSWORD", ""),
    "receiver": "1228358378@qq.com",
}

# ============================================================
# 精选岗位 - 全部来自 ncss.cn，点击直达岗位详情
# ============================================================
FEATURED_JOBS = {
    # 🟢 70-90%
    "high": {
        "label": "🟢 70-90% 能拿到面试",
        "desc": "中小厂/学历匹配/经验对口",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件工程师 / 电力电子硬件工程师",
                "company": "深圳市正浩创新科技",
                "location": "深圳南山",
                "type": "2027届研发提前批",
                "why": "深圳中小厂，电子/嵌入式专业直接对口，Altium Designer+PCB经验是加分项",
                "url": "https://guet.ncss.cn/student/jobs/Nhn3AZULWjDEhWfCG9Qg2v/detail.html",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式硬件工程师 / 嵌入式软件工程师",
                "company": "宇树科技",
                "location": "杭州",
                "type": "2027届校招",
                "why": "中小厂，嵌入式软硬件方向明确，你的STM32+Keil技能直接匹配",
                "url": "https://fg.ncss.cn/student/jobs/6JsdAwQiZpBp4iLcXErRFh/detail.html",
            },
            {
                "track": "电商运营",
                "title": "电商运营储干",
                "company": "蓝禾技术（行业头部品牌）",
                "location": "深圳龙华",
                "type": "校招",
                "why": "淘宝/天猫运营方向，接受应届生，你的2段电商实习直接对口",
                "url": "https://j.ncss.cn/student/jobs/Jb22Z6DSg9BCRXLEDSdVJ/detail.html",
            },
        ],
    },
    # 🟡 40-60% 主战场
    "mid": {
        "label": "🟡 40-60% 能拿到面试",
        "desc": "学校不占优但经验能加分，重点投",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件工程师 / GPU软件开发",
                "company": "芯动科技",
                "location": "武汉",
                "type": "2027届提前批",
                "why": "嵌入式软件+GPU方向，C语言是核心要求，你的专业对口",
                "url": "https://hust.ncss.cn/student/jobs/M5VjH1mxGnMLmg4ZfdRwZP/detail.html",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "暑期实习生（芯片/硬件/智能机器人）",
                "company": "小鹏集团",
                "location": "广州/深圳",
                "type": "2027届暑期实习（可转正）",
                "why": "实习门槛低于校招，表现好直接转正，广州深圳都有岗",
                "url": "https://3120ww.ncss.cn/student/m/jobs/KNiqQo5vuXpynyTGvurVQX/detail.html",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "校招实习（硬件/嵌入式/AI方向）",
                "company": "千寻智能",
                "location": "全国",
                "type": "2027届校招实习",
                "why": "硬件+嵌入式+AI多方向，你的课设项目可以展示动手能力",
                "url": "https://llcy.ncss.cn/student/jobs/GbEBXYVE6vXNJS8Rwe8zUE/detail.html",
            },
            {
                "track": "电商运营",
                "title": "JDS-创新零售采销（电商运营方向）",
                "company": "京东",
                "location": "北京/深圳等多地",
                "type": "校招",
                "why": "电商运营大厂岗，1688/淘宝经验是差异化优势",
                "url": "https://m.ncss.cn/student/m/jobs/GwhRTzF4pcsjkq3ti3GPcF/detail.html",
            },
            {
                "track": "新媒体运营",
                "title": "直播运营 / 短视频编导 / 活动新媒体运营",
                "company": "好未来集团（学而思母公司）",
                "location": "北京",
                "type": "2027届暑期实习（有转正机会）",
                "why": "含直播运营+短视频编导+电商运营多方向，你的自媒体经验加分",
                "url": "https://vy.ncss.cn/student/jobs/QgTTqE4vna6Zuc6XBGve3s/detail.html",
            },
        ],
    },
    # 🔵 10-30%
    "low": {
        "label": "🔵 10-30% 能拿到面试",
        "desc": "大厂/学历门槛高，投了不亏",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件开发 / PCB设计 / 嵌入式软件开发",
                "company": "比亚迪",
                "location": "深圳（主）/ 上海/重庆/西安",
                "type": "2027届校招",
                "why": "大厂，硬件方向全覆盖，PCB+嵌入式都是你的技能点",
                "url": "https://cumt.ncss.cn/student/jobs/4dy2cSjCCAnFcDfyPqi5vZ/detail.html",
            },
        ],
    },
}

# ============================================================
# 快捷搜索入口
# ============================================================
QUICK_SEARCHES = [
    {
        "label": "Boss直聘 · 嵌入式应届",
        "url": "https://www.zhipin.com/web/geek/job?query=嵌入式工程师%20硬件工程师&experience=401&degree=203",
    },
    {
        "label": "Boss直聘 · 电商运营应届",
        "url": "https://www.zhipin.com/web/geek/job?query=电商运营%20平台运营&experience=401&degree=203",
    },
    {
        "label": "Boss直聘 · 新媒体应届",
        "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20内容运营&experience=401&degree=203",
    },
    {
        "label": "国家就业平台 · 校招专区",
        "url": "https://www.ncss.cn/student/jobs/index.html",
    },
]

KEY_DATES = [
    {"date": "8月中旬", "event": "大厂秋招正式批大规模启动"},
    {"date": "8月下旬-9月", "event": "网申高峰，每天投10-15家"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
