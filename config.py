"""
秋招日报 - 配置
新媒体+电商=75%  嵌入式=25%  全部2027届
牛客网已移除，只保留可打开的链接
"""
import os

EMAIL_CONFIG = {
    "smtp_host": "smtp.qq.com",
    "smtp_port": 465,
    "sender": "1228358378@qq.com",
    "password": os.environ.get("QQ_SMTP_PASSWORD", ""),
    "receiver": "1228358378@qq.com",
}

FEATURED_JOBS = {
    "high": {
        "label": "🟢 70-90% 能拿到面试",
        "desc": "实习/项目直接对口，自媒体经验是差异化亮点",
        "jobs": [
            {
                "track": "新媒体运营",
                "title": "小红书运营实习生",
                "company": "乐学培优",
                "location": "广州 / 杭州 / 长沙 / 北京等",
                "type": "2027届提前批",
                "deadline": "⏰ 8月19日截止",
                "why": "小红书运营！你的小红书5W+数据就是最好的简历",
                "url": "https://campus.niuqizp.com/schedule-7ym85Mza5.html",
            },
            {
                "track": "新媒体运营",
                "title": "游戏运营 / 视频设计师",
                "company": "多益网络",
                "location": "广州 / 杭州 / 武汉 / 苏州",
                "type": "2027届秋招提前批",
                "deadline": "⏰ 8月31日截止",
                "why": "广州杭州有岗！游戏运营+视频设计，专业不限，8-10K/月",
                "url": "https://henau.goworkla.cn/module/position_details/id-469907/nid-8086",
            },
            {
                "track": "电商运营",
                "title": "商品运营管培生 / 运营管培生",
                "company": "拼多多 PDD",
                "location": "上海",
                "type": "2027届提前批",
                "deadline": "⏰ 8月23日截止",
                "why": "1688/淘宝运营经验直接对口，提前批不影响正式批",
                "url": "https://careers.pddglobalhr.com/campus",
            },
            {
                "track": "新媒体运营",
                "title": "视频创意制作",
                "company": "拼多多 PDD",
                "location": "上海",
                "type": "2027届提前批",
                "deadline": "⏰ 8月23日截止",
                "why": "脚本→拍摄→剪辑→投放全流程你都做过",
                "url": "https://careers.pddglobalhr.com/campus",
            },
        ],
    },
    "mid": {
        "label": "🟡 40-60% 能拿到面试",
        "desc": "经验能加分，新媒体+电商主战场",
        "jobs": [
            {
                "track": "新媒体运营",
                "title": "KOL运营 / 广告创意（短视频方向）",
                "company": "拼多多 PDD（市场管培生）",
                "location": "上海",
                "type": "2027届提前批",
                "deadline": "⏰ 8月23日截止",
                "why": "短视频达人投放+内容策略，自媒体运营方法论可复用",
                "url": "https://careers.pddglobalhr.com/campus",
            },
            {
                "track": "新媒体运营",
                "title": "运营管培生（新媒体/直播电商方向）",
                "company": "沈阳新东方",
                "location": "沈阳",
                "type": "2027届校招",
                "deadline": "⏰ 见岗位页",
                "why": "新媒体+直播电商方向，新东方直播板块扩展中",
                "url": "https://lzpu.bysjy.com.cn/detail/online?id=3530780",
            },
            {
                "track": "新媒体运营",
                "title": "直播运营 / 短视频编导 / 新媒体运营",
                "company": "好未来（学而思母公司）",
                "location": "北京",
                "type": "2027届暑期实习（可转正）",
                "deadline": "⏰ 见岗位页",
                "why": "直播+短视频+电商多方向，可转正",
                "url": "https://vy.ncss.cn/student/jobs/QgTTqE4vna6Zuc6XBGve3s/detail.html",
            },
            {
                "track": "电商运营",
                "title": "营销族储备实习生（电商/内容方向）",
                "company": "安克创新 Anker",
                "location": "深圳 / 杭州",
                "type": "2027届储备实习（可转正）",
                "deadline": "⏰ 全年滚动招聘",
                "why": "全球化品牌！深圳杭州有岗！2亿用户，实习转正率高",
                "url": "https://career.anker.com.cn",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件工程师 / 电力电子硬件工程师",
                "company": "正浩创新科技",
                "location": "深圳南山",
                "type": "2027届研发提前批",
                "deadline": "⏰ 见岗位页",
                "why": "深圳中小厂，电子/嵌入式专业对口",
                "url": "https://guet.ncss.cn/student/jobs/Nhn3AZULWjDEhWfCG9Qg2v/detail.html",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "暑期实习生（芯片/硬件/智能机器人）",
                "company": "小鹏集团",
                "location": "广州 / 深圳",
                "type": "2027届实习（可转正）",
                "deadline": "⏰ 见岗位页",
                "why": "广州深圳有岗！实习门槛低于校招，表现好转正",
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
                "why": "机器人赛道热门公司，嵌入式软硬件方向",
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
    {"label": "多益网络校招", "url": "https://henau.goworkla.cn/module/position_details/id-469907/nid-8086"},
]

KEY_DATES = [
    {"date": "7月-8月中旬", "event": "提前批高峰期！拼多多8.23/多益8.31/乐学8.19截止"},
    {"date": "8月中旬-9月", "event": "秋招正式批大规模启动，岗位暴增"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
