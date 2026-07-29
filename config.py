"""
秋招日报 - 配置
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
# 三条路线 × 精准岗位搜索链接
# 每个链接打开后是具体的岗位列表页，可一键投递
# ============================================================
TRACK_SEARCHES = {
    "嵌入式/硬件工程师": {
        "icon": "🔧",
        "searches": [
            {
                "label": "牛客网 · 嵌入式/硬件校招",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式&keyword=硬件工程师&keyword=单片机&keyword=电子工程师&keyword=STM32",
                "desc": "一键筛选所有嵌入式+硬件校招岗位"
            },
            {
                "label": "牛客网 · 嵌入式实习",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=嵌入式&keyword=硬件工程师&keyword=单片机",
                "desc": "嵌入式实习岗位（可转正优先）"
            },
            {
                "label": "Boss直聘 · 硬件/嵌入式校招",
                "url": "https://www.zhipin.com/web/geek/job?query=嵌入式工程师%20硬件工程师&experience=401&degree=203",
                "desc": "经验筛选应届生+本科，深圳/广州/东莞"
            },
            {
                "label": "前程无忧 · 电子/硬件校招",
                "url": "https://we.51job.com/pc/search?keyword=嵌入式%20硬件工程师%20电子工程师&keywordType=3&workYear=01",
                "desc": "51job校招频道，按应届生筛选"
            },
        ],
    },
    "电商运营": {
        "icon": "🛒",
        "searches": [
            {
                "label": "牛客网 · 电商运营校招",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商运营&keyword=平台运营&keyword=店铺运营&keyword=品类运营&keyword=商家运营",
                "desc": "一键筛选所有电商运营校招岗位"
            },
            {
                "label": "牛客网 · 电商运营实习",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=电商运营&keyword=平台运营&keyword=网店运营",
                "desc": "电商运营实习岗位"
            },
            {
                "label": "Boss直聘 · 电商运营应届",
                "url": "https://www.zhipin.com/web/geek/job?query=电商运营%20平台运营&experience=401&degree=203",
                "desc": "经验筛选应届生+本科"
            },
            {
                "label": "前程无忧 · 电商运营校招",
                "url": "https://we.51job.com/pc/search?keyword=电商运营%20平台运营%20店铺运营&keywordType=3&workYear=01",
                "desc": "51job校招频道"
            },
        ],
    },
    "新媒体运营": {
        "icon": "📱",
        "searches": [
            {
                "label": "牛客网 · 新媒体/内容校招",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=新媒体运营&keyword=内容运营&keyword=短视频运营&keyword=小红书&keyword=文案策划",
                "desc": "一键筛选所有新媒体+内容校招岗位"
            },
            {
                "label": "牛客网 · 新媒体实习",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=新媒体运营&keyword=内容运营&keyword=短视频",
                "desc": "新媒体运营实习岗位"
            },
            {
                "label": "Boss直聘 · 新媒体运营应届",
                "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20内容运营%20短视频&experience=401&degree=203",
                "desc": "经验筛选应届生+本科"
            },
            {
                "label": "前程无忧 · 新媒体校招",
                "url": "https://we.51job.com/pc/search?keyword=新媒体运营%20内容运营%20短视频&keywordType=3&workYear=01",
                "desc": "51job校招频道"
            },
        ],
    },
}

# ============================================================
# 精选具体岗位（手动筛选，定期更新）
# 这些是经过人工筛选、确实适合你的具体岗位
# ============================================================
FEATURED_JOBS = [
    # 嵌入式方向
    {
        "track": "嵌入式/硬件工程师",
        "title": "嵌入式软件开发（27届）",
        "company": "某科技公司",
        "location": "深圳",
        "salary": "18-22K×12薪",
        "deadline": "2026年7月-2029年7月",
        "url": "https://www.nowcoder.com/jobs/detail/439067",
        "note": "要求STM32、C语言，直接对口你的技能",
    },
    {
        "track": "嵌入式/硬件工程师",
        "title": "硬件技术工程师",
        "company": "华为",
        "location": "东莞松山湖",
        "salary": "16-26K×12薪",
        "deadline": "2026年10月",
        "url": "https://www.nowcoder.com/jobs/detail/280321",
        "note": "电子信息工程对口专业，广东本地",
    },
    {
        "track": "嵌入式/硬件工程师",
        "title": "嵌入式工程师（MCU）",
        "company": "诺瓦星云",
        "location": "深圳",
        "salary": "面议",
        "deadline": "2028年9月",
        "url": "https://www.nowcoder.com/jobs/detail/415327",
        "note": "明确要求STM32、GD32经验",
    },
    # 新媒体方向
    {
        "track": "新媒体运营",
        "title": "市场管培生（KOL运营/广告创意方向）",
        "company": "某互联网公司",
        "location": "上海",
        "salary": "面议",
        "deadline": "2027年7月1日",
        "url": "https://www.nowcoder.com/jobs/detail/340432",
        "note": "含短视频运营+内容策划方向，27届可投",
    },
    # 电商方向
    {
        "track": "电商运营",
        "title": "电商运营",
        "company": "启安谷科技",
        "location": "深圳",
        "salary": "面议",
        "deadline": "待确认",
        "url": "https://www.nowcoder.com/jobs/detail/450175",
        "note": "深圳电商运营岗，方向对口",
    },
]

# ============================================================
# 秋招时间节点
# ============================================================
KEY_DATES = [
    {"date": "8月中旬", "event": "大部分互联网大厂秋招正式批启动"},
    {"date": "8月下旬-9月", "event": "秋招网申高峰期，每天投递10-15家"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期，提前刷题"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录+春招提前批"},
]
