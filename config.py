"""
秋招日报 - 配置文件
"""
import os

# ============================================================
# 邮箱配置
# ============================================================
EMAIL_CONFIG = {
    "smtp_host": "smtp.qq.com",
    "smtp_port": 465,
    "sender": "1228358378@qq.com",
    "password": os.environ.get("QQ_SMTP_PASSWORD", ""),
    "receiver": "1228358378@qq.com",
}

# ============================================================
# 三条路线
# ============================================================
TRACKS = {
    "嵌入式/硬件工程师": {
        "icon": "🔧",
        "keywords": ["嵌入式", "STM32", "单片机", "PCB", "硬件工程师", "电子工程师", "C语言嵌入式"],
        "search_term": "嵌入式 OR 硬件工程师 OR 单片机 OR PCB",
    },
    "电商运营": {
        "icon": "🛒",
        "keywords": ["电商运营", "平台运营", "淘宝", "天猫", "1688", "店铺运营", "品类运营"],
        "search_term": "电商运营 OR 平台运营 OR 店铺运营",
    },
    "新媒体运营": {
        "icon": "📱",
        "keywords": ["新媒体运营", "内容运营", "短视频运营", "小红书运营", "公众号运营", "文案策划"],
        "search_term": "新媒体运营 OR 内容运营 OR 短视频运营",
    },
}

# ============================================================
# 目标公司（重点关注）
# ============================================================
WATCH_COMPANIES = [
    # 大厂
    {"name": "字节跳动", "url": "https://jobs.bytedance.com/campus"},
    {"name": "腾讯", "url": "https://join.qq.com/post.html"},
    {"name": "快手", "url": "https://campus.kuaishou.cn"},
    {"name": "小红书", "url": "https://job.xiaohongshu.com/campus"},
    {"name": "得物", "url": "https://app.mokahr.com/campus-recruitment/thedu"},
    # 电商/新消费
    {"name": "SHEIN", "url": "https://app.mokahr.com/campus-recruitment/shein"},
    {"name": "安克创新", "url": "https://career.anker.com/campus"},
    {"name": "蓝月亮", "url": "https://bluemoon.zhiye.com/campus"},
    {"name": "逸仙电商(完美日记)", "url": "https://app.mokahr.com/campus-recruitment/yatsen"},
    # 硬件/IoT
    {"name": "大疆", "url": "https://we.dji.com/cn/campus"},
    {"name": "OPPO", "url": "https://career.oppo.com/campus"},
    {"name": "vivo", "url": "https://hr.vivo.com/campus"},
    {"name": "格力", "url": "https://gree.zhiye.com/campus"},
    {"name": "美的", "url": "https://career.midea.com/campus"},
    {"name": "立讯精密", "url": "https://luxshare.zhiye.com/campus"},
]

# ============================================================
# 预筛选搜索链接（每条路线 × 每个平台）
# ============================================================
SEARCH_LINKS = {
    "嵌入式/硬件工程师": [
        {
            "name": "牛客网-校招职位",
            "url": "https://www.nowcoder.com/jobs/school/search?keyword=嵌入式&keyword=硬件工程师&keyword=单片机&keyword=电子工程师",
        },
        {
            "name": "Boss直聘-校招",
            "url": "https://www.zhipin.com/web/geek/job?query=嵌入式工程师&experience=401",
        },
        {
            "name": "应届生求职网",
            "url": "https://q.yingjiesheng.com/jobs/search/?keyword=嵌入式",
        },
        {
            "name": "前程无忧-校招",
            "url": "https://we.51job.com/pc/search?keyword=嵌入式%20硬件工程师&keywordType=3",
        },
    ],
    "电商运营": [
        {
            "name": "牛客网-校招职位",
            "url": "https://www.nowcoder.com/jobs/school/search?keyword=电商运营&keyword=平台运营&keyword=店铺运营",
        },
        {
            "name": "Boss直聘-校招",
            "url": "https://www.zhipin.com/web/geek/job?query=电商运营&experience=401",
        },
        {
            "name": "应届生求职网",
            "url": "https://q.yingjiesheng.com/jobs/search/?keyword=电商运营",
        },
        {
            "name": "前程无忧-校招",
            "url": "https://we.51job.com/pc/search?keyword=电商运营&keywordType=3",
        },
    ],
    "新媒体运营": [
        {
            "name": "牛客网-校招职位",
            "url": "https://www.nowcoder.com/jobs/school/search?keyword=新媒体运营&keyword=内容运营&keyword=短视频",
        },
        {
            "name": "Boss直聘-校招",
            "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营&experience=401",
        },
        {
            "name": "应届生求职网",
            "url": "https://q.yingjiesheng.com/jobs/search/?keyword=新媒体运营",
        },
        {
            "name": "前程无忧-校招",
            "url": "https://we.51job.com/pc/search?keyword=新媒体运营&keywordType=3",
        },
    ],
}

# ============================================================
# 秋招关键时间节点
# ============================================================
KEY_DATES = [
    {"date": "8月中旬", "event": "大部分互联网大厂秋招正式批启动"},
    {"date": "8月下旬-9月", "event": "秋招网申高峰期，建议每天投递10-15家"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录+春招提前批关注"},
]
