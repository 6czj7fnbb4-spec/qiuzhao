"""
秋招日报 - 配置
只使用搜索列表页链接（无需登录即可查看岗位列表）
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
# 精选岗位推荐
# 告诉你搜什么、找哪家公司、注意什么
# 链接是搜索页（无需登录即可浏览岗位列表）
# ============================================================
FEATURED_JOBS = {
    "high": {
        "label": "🟢 70-90% 能拿到面试",
        "desc": "学历/经验高度匹配，你的简历竞争力强",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "what": "硬件开发工程师 · PCB设计方向",
                "where": "牛客网校招 → 搜索「硬件开发 PCB Altium」",
                "why": "明确要求Altium Designer+PCB设计，专业完全对口",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=硬件开发&keyword=PCB&keyword=Altium",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "硬件开发 · 广东地区",
                "where": "牛客网校招 → 搜索「硬件开发」筛选广东",
                "why": "硬件开发岗位，电子类专业优先，中小厂居多",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=硬件开发&keyword=电子工程师",
            },
            {
                "track": "电商运营",
                "what": "电商运营 · 广东地区",
                "where": "牛客网校招 → 搜索「电商运营 平台运营 店铺运营」",
                "why": "2段电商实习+全链路运营经验，直接就对口",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商运营&keyword=平台运营&keyword=店铺运营",
            },
            {
                "track": "电商运营",
                "what": "电商运营 · Boss直聘",
                "where": "Boss直聘 → 搜「电商运营」→筛「应届生」→城市选深圳/广州/东莞",
                "why": "Boss直聘中小厂多，直接和HR沟通，效率最高",
                "search_url": "https://www.zhipin.com/web/geek/job?query=电商运营&experience=401&degree=203",
            },
            {
                "track": "新媒体运营",
                "what": "新媒体运营 · 全平台",
                "where": "牛客网校招 → 搜索「新媒体运营 内容运营 短视频」",
                "why": "公众号+小红书实操经验，有数据有案例，面试时能讲",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=新媒体运营&keyword=内容运营&keyword=短视频运营",
            },
            {
                "track": "新媒体运营",
                "what": "新媒体/内容运营 · Boss直聘",
                "where": "Boss直聘 → 搜「新媒体运营」→筛「应届生」",
                "why": "中小企业新媒体岗多，你的自媒体数据是差异化亮点",
                "search_url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20内容运营&experience=401&degree=203",
            },
        ],
    },
    "mid": {
        "label": "🟡 40-60% 能拿到面试",
        "desc": "学校不占优但实习/项目能加分，建议重点投",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "what": "嵌入式软件开发 · STM32方向",
                "where": "牛客网校招 → 搜索「嵌入式 STM32 单片机」",
                "why": "你的核心技能就是STM32+C语言，课设项目面聊时能展示",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式&keyword=STM32&keyword=单片机",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "嵌入式软件工程师 · 中型企业",
                "where": "牛客网校招 → 搜索「嵌入式软件 C语言 Keil」",
                "why": "C语言+Keil开发经验是硬通货，中小厂更看重动手能力",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式软件&keyword=C语言",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "硬件技术工程师",
                "where": "牛客网校招 → 搜索「硬件技术 电子工程师」",
                "why": "电子类专业对口岗，原理图/PCB经验加分",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=硬件技术&keyword=电子工程师",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "嵌入式实习（可转正）",
                "where": "牛客网实习 → 搜索「嵌入式 硬件」",
                "why": "实习门槛低于校招，表现好直接转正",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=嵌入式&keyword=STM32",
            },
            {
                "track": "电商运营",
                "what": "平台运营/品类运营",
                "where": "牛客网校招 → 搜索「平台运营 品类运营 商家运营」",
                "why": "你的1688+淘宝双平台经验是稀缺的，很多应届生没有",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=平台运营&keyword=品类运营&keyword=商家运营",
            },
            {
                "track": "电商运营",
                "what": "电商运营 · 中小厂/品牌方",
                "where": "Boss直聘 → 搜「电商运营」→ 筛20-499人规模",
                "why": "中小品牌方电商部，对你来说是最容易进的",
                "search_url": "https://www.zhipin.com/web/geek/job?query=电商运营&experience=401&degree=203&scale=302,303",
            },
            {
                "track": "电商运营",
                "what": "产品运营 · 互联网公司",
                "where": "牛客网校招 → 搜索「产品运营 用户运营」",
                "why": "你的数据分析思维+运营实操经验可以迁移到产品运营",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=产品运营&keyword=用户运营",
            },
            {
                "track": "新媒体运营",
                "what": "市场管培生 · KOL/短视频方向",
                "where": "牛客网校招 → 搜索「KOL运营 达人运营 内容营销」",
                "why": "含短视频达人投放+内容策略，你的自媒体实操直接对口",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=KOL运营&keyword=内容营销&keyword=短视频",
            },
            {
                "track": "新媒体运营",
                "what": "视频创意/短视频制作",
                "where": "牛客网校招 → 搜索「视频创意 短视频制作 剪辑」",
                "why": "你有短视频全流程经验，从脚本到剪辑到投放都做过",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=视频创意&keyword=短视频&keyword=新媒体",
            },
            {
                "track": "新媒体运营",
                "what": "新媒体运营 · 小红书/公众号方向",
                "where": "Boss直聘 → 搜「小红书运营」或「公众号运营」→ 应届生",
                "why": "你的小红书+公众号数据可以直接当作品集展示",
                "search_url": "https://www.zhipin.com/web/geek/job?query=小红书运营%20公众号运营&experience=401",
            },
        ],
    },
    "low": {
        "label": "🔵 10-30% 能拿到面试",
        "desc": "大厂/学历门槛高，但投了不亏，万一呢",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "what": "华为 · 硬件/嵌入式岗",
                "where": "牛客网校招 → 搜索「硬件」→ 筛选「华为」",
                "why": "东莞松山湖，电子信息工程对口，薪资16-40K",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=硬件技术&keyword=嵌入式&company=华为",
            },
            {
                "track": "嵌入式/硬件工程师",
                "what": "大厂通用软件开发/嵌入式",
                "where": "牛客网校招 → 搜索「通用软件 嵌入式 校招」",
                "why": "BSP驱动/嵌入式系统方向，提前批可能降低学历门槛",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=通用软件&keyword=嵌入式",
            },
            {
                "track": "电商运营",
                "what": "京东/拼多多 · 电商运营/采销",
                "where": "牛客网校招 → 搜索「京东 拼多多 电商」",
                "why": "大厂电商核心岗，你的实习经验能拿来硬刚",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商&company=京东",
            },
            {
                "track": "新媒体运营",
                "what": "小米/大厂 · 运营岗",
                "where": "牛客网校招 → 搜索「产品运营」→ 筛选大厂",
                "why": "内容运营/用户运营方向，深圳有岗",
                "search_url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=产品运营&keyword=内容运营",
            },
        ],
    },
}

# ============================================================
# 快捷搜索入口（6个核心搜索链接）
# ============================================================
QUICK_SEARCHES = [
    {
        "label": "嵌入式/硬件校招",
        "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式&keyword=硬件工程师&keyword=STM32&keyword=单片机",
    },
    {
        "label": "嵌入式/硬件实习",
        "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=嵌入式&keyword=硬件工程师&keyword=STM32",
    },
    {
        "label": "电商运营校招",
        "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商运营&keyword=平台运营&keyword=店铺运营",
    },
    {
        "label": "电商运营实习",
        "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=电商运营&keyword=平台运营",
    },
    {
        "label": "新媒体/内容校招",
        "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=新媒体运营&keyword=内容运营&keyword=短视频运营",
    },
    {
        "label": "新媒体/内容实习",
        "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=新媒体运营&keyword=内容运营",
    },
]

KEY_DATES = [
    {"date": "8月中旬", "event": "大厂秋招正式批大规模启动"},
    {"date": "8月下旬-9月", "event": "网申高峰，每天投10-15家（电商4:新媒体3:嵌入式3）"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
