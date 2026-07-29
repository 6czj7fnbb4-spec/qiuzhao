"""
秋招日报 - 配置
所有链接已验证可直接打开（Boss直聘/前程无忧/应届生求职网）
牛客网链接已移除（反爬拦截）
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
# 三条路线 × 已验证可打开的搜索链接
# ============================================================
TRACK_LINKS = {
    "嵌入式/硬件工程师": {
        "icon": "🔧",
        "links": [
            {
                "label": "Boss直聘 · 嵌入式应届",
                "url": "https://www.zhipin.com/web/geek/job?query=嵌入式工程师%20硬件工程师&experience=401&degree=203&city=101280100",
                "desc": "深圳 · 应届 · 本科 · 嵌入式/硬件岗",
            },
            {
                "label": "Boss直聘 · STM32单片机",
                "url": "https://www.zhipin.com/web/geek/job?query=STM32%20单片机%20嵌入式&experience=401&degree=203",
                "desc": "你的核心技能：STM32+单片机",
            },
            {
                "label": "前程无忧 · 嵌入式校招",
                "url": "https://we.51job.com/pc/search?keyword=嵌入式%20硬件工程师%20单片机&keywordType=3&workYear=01",
                "desc": "51job校招频道，筛选应届生",
            },
            {
                "label": "应届生求职网 · 嵌入式",
                "url": "https://q.yingjiesheng.com/jobs/search/?keyword=嵌入式",
                "desc": "51job旗下校招平台",
            },
        ],
    },
    "电商运营": {
        "icon": "🛒",
        "links": [
            {
                "label": "Boss直聘 · 电商运营应届",
                "url": "https://www.zhipin.com/web/geek/job?query=电商运营%20平台运营%20店铺运营&experience=401&degree=203&city=101280100",
                "desc": "深圳 · 应届 · 本科 · 电商运营",
            },
            {
                "label": "Boss直聘 · 电商中小厂",
                "url": "https://www.zhipin.com/web/geek/job?query=电商运营%20网店运营&experience=401&degree=203&scale=302,303",
                "desc": "20-499人中小厂（你的主战场）",
            },
            {
                "label": "前程无忧 · 电商运营校招",
                "url": "https://we.51job.com/pc/search?keyword=电商运营%20平台运营%20店铺运营&keywordType=3&workYear=01",
                "desc": "51job校招频道",
            },
            {
                "label": "应届生求职网 · 电商运营",
                "url": "https://q.yingjiesheng.com/jobs/search/?keyword=电商运营",
                "desc": "51job旗下校招平台",
            },
        ],
    },
    "新媒体运营": {
        "icon": "📱",
        "links": [
            {
                "label": "Boss直聘 · 新媒体应届",
                "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20内容运营%20短视频&experience=401&degree=203",
                "desc": "应届 · 本科 · 新媒体/内容/短视频",
            },
            {
                "label": "Boss直聘 · 小红书/公众号",
                "url": "https://www.zhipin.com/web/geek/job?query=小红书运营%20公众号运营%20短视频运营&experience=401&degree=203",
                "desc": "你的自媒体经验直接对口",
            },
            {
                "label": "前程无忧 · 新媒体校招",
                "url": "https://we.51job.com/pc/search?keyword=新媒体运营%20内容运营%20短视频&keywordType=3&workYear=01",
                "desc": "51job校招频道",
            },
            {
                "label": "应届生求职网 · 新媒体",
                "url": "https://q.yingjiesheng.com/jobs/search/?keyword=新媒体运营",
                "desc": "51job旗下校招平台",
            },
        ],
    },
}

# ============================================================
# 每日精选搜索推荐
# ============================================================
DAILY_PICKS = [
    # 🟢 70-90%
    {
        "tier": "high",
        "label": "🟢 70-90% 能拿到面试",
        "picks": [
            {
                "track": "嵌入式/硬件工程师",
                "what": "Boss直聘 → 搜「硬件开发 PCB Altium」→ 城市选深圳/东莞",
                "why": "你的AD+PCB技能是直接卖点",
                "url": "https://www.zhipin.com/web/geek/job?query=硬件开发%20PCB%20Altium&experience=401&degree=203",
            },
            {
                "track": "电商运营",
                "what": "Boss直聘 → 搜「电商运营 1688 淘宝」→ 筛20-499人",
                "why": "1688/淘宝双平台经验，中小厂最认这个",
                "url": "https://www.zhipin.com/web/geek/job?query=电商运营%201688%20淘宝&experience=401&degree=203&scale=302,303",
            },
            {
                "track": "新媒体运营",
                "what": "Boss直聘 → 搜「新媒体运营 小红书」→ 应届生",
                "why": "小红书5W+阅读数据就是最好的简历",
                "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20小红书&experience=401&degree=203",
            },
        ],
    },
    # 🟡 40-60%
    {
        "tier": "mid",
        "label": "🟡 40-60% 能拿到面试",
        "picks": [
            {
                "track": "嵌入式/硬件工程师",
                "what": "Boss直聘 → 搜「嵌入式 STM32 Keil」→ 应届生",
                "why": "STM32+Keil是你课设的核心技术栈",
                "url": "https://www.zhipin.com/web/geek/job?query=嵌入式%20STM32%20Keil&experience=401&degree=203",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "前程无忧 → 搜「嵌入式 电子工程师」→ 校招频道",
                "why": "传统企业电子岗，学历门槛比互联网低",
                "url": "https://we.51job.com/pc/search?keyword=嵌入式%20电子工程师&keywordType=3&workYear=01",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "应届生求职网 → 搜「硬件工程师」",
                "why": "校招专属平台，竞争比Boss直聘小",
                "url": "https://q.yingjiesheng.com/jobs/search/?keyword=硬件工程师",
            },
            {
                "track": "电商运营",
                "what": "Boss直聘 → 搜「平台运营 品类运营 商家运营」",
                "why": "你的全链路运营经验，比纯内容运营有优势",
                "url": "https://www.zhipin.com/web/geek/job?query=平台运营%20品类运营%20商家运营&experience=401&degree=203",
            },
            {
                "track": "电商运营",
                "what": "前程无忧 → 搜「电商运营 淘宝 天猫」→ 校招",
                "why": "品牌方电商部，稳定且培养体系完善",
                "url": "https://we.51job.com/pc/search?keyword=电商运营%20淘宝%20天猫&keywordType=3&workYear=01",
            },
            {
                "track": "新媒体运营",
                "what": "Boss直聘 → 搜「短视频运营 剪辑」→ 应届生",
                "why": "你从脚本到剪辑到投放全流程都做过",
                "url": "https://www.zhipin.com/web/geek/job?query=短视频运营%20剪辑&experience=401&degree=203",
            },
            {
                "track": "新媒体运营",
                "what": "前程无忧 → 搜「内容运营 新媒体」→ 校招",
                "why": "公众号2200粉+小红书5W+阅读，有硬数据",
                "url": "https://we.51job.com/pc/search?keyword=内容运营%20新媒体&keywordType=3&workYear=01",
            },
        ],
    },
    # 🔵 10-30%
    {
        "tier": "low",
        "label": "🔵 10-30% 能拿到面试",
        "picks": [
            {
                "track": "嵌入式/硬件工程师",
                "what": "Boss直聘 → 搜「华为 嵌入式」或「大疆 硬件」",
                "why": "大厂校招，专业对口就投，万一简历过了呢",
                "url": "https://www.zhipin.com/web/geek/job?query=嵌入式&experience=401&degree=203&city=101280100",
            },
            {
                "track": "电商运营",
                "what": "Boss直聘 → 搜「电商运营」→ 城市选广州/杭州/成都",
                "why": "多城市撒网，SHEIN/唯品会等大厂在广深有岗",
                "url": "https://www.zhipin.com/web/geek/job?query=电商运营&experience=401&degree=203&city=101280100",
            },
            {
                "track": "新媒体运营",
                "what": "Boss直聘 → 搜「内容运营」→ 筛大厂/千人以上",
                "why": "作品集过关的话，学校的影响会被弱化",
                "url": "https://www.zhipin.com/web/geek/job?query=内容运营&experience=401&degree=203&scale=305,306",
            },
        ],
    },
]

KEY_DATES = [
    {"date": "8月中旬", "event": "大厂秋招正式批大规模启动"},
    {"date": "8月下旬-9月", "event": "网申高峰，每天投10-15家（电商4:新媒体3:嵌入式3）"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期，提前刷面经"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
