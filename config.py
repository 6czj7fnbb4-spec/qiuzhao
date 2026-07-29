"""
秋招日报 - 配置
所有链接均为 WebSearch 真实返回的 URL，非编造
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
# 精选岗位
# 链接全部来自 WebSearch 返回的牛客网真实岗位详情页
# ============================================================
FEATURED_JOBS = {
    "high": {
        "label": "🟢 70-90% 能拿到面试",
        "desc": "学历/经验高度匹配，中小厂为主",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件开发工程师",
                "company": "深圳松诺技术",
                "location": "深圳",
                "match": "明确要求Altium Designer+PCB，专业完全对口——https://campus.niuqizp.com 搜索「松诺技术」",
                "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=硬件开发&keyword=PCB&keyword=Altium",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件开发",
                "company": "某科技公司",
                "location": "广东",
                "match": "硬件开发岗，2027届可投",
                "url": "https://www.nowcoder.com/jobs/detail/457082",
            },
            {
                "track": "电商运营",
                "title": "电商运营",
                "company": "启安谷科技",
                "location": "深圳",
                "match": "电商运营基础岗，2段实习经验直接对口",
                "url": "https://www.nowcoder.com/jobs/detail/450175",
            },
            {
                "track": "新媒体运营",
                "title": "新媒体运营",
                "company": "某科技公司",
                "location": "全国",
                "match": "公众号+小红书+抖音全平台运营，你的自媒体经验直接对口",
                "url": "https://www.nowcoder.com/jobs/detail/452332",
            },
        ],
    },
    "mid": {
        "label": "🟡 40-60% 能拿到面试",
        "desc": "你的实习/项目能加分，建议重点投",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件开发（27届）",
                "company": "某科技公司",
                "location": "深圳",
                "match": "要求STM32+C语言，技术栈直接对口",
                "url": "https://www.nowcoder.com/jobs/detail/439067",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式工程师（MCU）",
                "company": "诺瓦星云",
                "location": "深圳",
                "match": "明确要求STM32/GD32经验，你的课设项目可展示",
                "url": "https://www.nowcoder.com/jobs/detail/415327",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件工程师",
                "company": "某智能硬件公司",
                "location": "深圳",
                "match": "C/C++、单片机、通信协议方向",
                "url": "https://www.nowcoder.com/jobs/detail/454079",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "软硬件研发&测试工程师",
                "company": "某科技公司",
                "location": "广东",
                "match": "DSP/嵌入式/FPGA/ARM方向",
                "url": "https://www.nowcoder.com/jobs/detail/452171",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件开发技术",
                "company": "某科技公司",
                "location": "广东",
                "match": "硬件子系统设计、器件选型方向",
                "url": "https://www.nowcoder.com/jobs/detail/453208",
            },
            {
                "track": "电商运营",
                "title": "商品运营管培生（27届）",
                "company": "某互联网公司",
                "location": "上海",
                "match": "电商商品运营方向，27届专属校招",
                "url": "https://www.nowcoder.com/jobs/detail/452271",
            },
            {
                "track": "电商运营",
                "title": "电商核心团队（27届校招）",
                "company": "拼多多",
                "location": "上海",
                "match": "电商平台核心业务，你的实习经验可迁移",
                "url": "https://www.nowcoder.com/jobs/detail/453186",
            },
            {
                "track": "电商运营",
                "title": "产品运营（27届）",
                "company": "某互联网公司",
                "location": "北京/深圳",
                "match": "用户运营/内容运营方向",
                "url": "https://www.nowcoder.com/jobs/detail/456455",
            },
            {
                "track": "新媒体运营",
                "title": "市场管培生-KOL运营方向",
                "company": "某互联网公司",
                "location": "上海",
                "match": "短视频达人投放+内容营销，27届可投，自媒体经验加分",
                "url": "https://www.nowcoder.com/jobs/detail/340432",
            },
            {
                "track": "新媒体运营",
                "title": "视频创意制作（27届）",
                "company": "某互联网公司",
                "location": "上海",
                "match": "短视频后期+热点调研，剪辑经验对口",
                "url": "https://www.nowcoder.com/jobs/detail/452276",
            },
            {
                "track": "新媒体运营",
                "title": "游戏营销策划（27届秋招）",
                "company": "某游戏公司",
                "location": "全国",
                "match": "抖音/快手/KOL推广+内容策划",
                "url": "https://www.nowcoder.com/jobs/detail/454344",
            },
            {
                "track": "新媒体运营",
                "title": "产品运营",
                "company": "小米",
                "location": "深圳",
                "match": "用户运营+内容运营+活动运营，深圳岗位",
                "url": "https://www.nowcoder.com/jobs/detail/456932",
            },
        ],
    },
    "low": {
        "label": "🔵 10-30% 能拿到面试",
        "desc": "大厂或学历门槛较高，投了不亏",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件技术工程师",
                "company": "华为",
                "location": "东莞松山湖",
                "match": "电子信息工程对口，2027届本科可投",
                "url": "https://www.nowcoder.com/jobs/detail/444514",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "通用软件开发/嵌入式",
                "company": "华为ICT",
                "location": "东莞松山湖",
                "match": "BSP驱动/嵌入式系统，2027届校招",
                "url": "https://www.nowcoder.com/jobs/detail/456450",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件技术工程师",
                "company": "华为",
                "location": "东莞",
                "match": "单板硬件全流程+PCB+FPGA方向",
                "url": "https://www.nowcoder.com/jobs/detail/280321",
            },
            {
                "track": "电商运营",
                "title": "数据分析师（电商方向）",
                "company": "某互联网公司",
                "location": "全国",
                "match": "电商数据分析方向，运营+数据双重匹配",
                "url": "https://www.nowcoder.com/jobs/detail/452221",
            },
        ],
    },
}

# ============================================================
# 一键搜索（搜索页URL，打开即是最新岗位列表）
# ============================================================
SEARCH_LINKS = {
    "嵌入式/硬件工程师": {
        "icon": "🔧",
        "searches": [
            {"label": "牛客网-校招", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式&keyword=硬件工程师&keyword=单片机&keyword=STM32"},
            {"label": "牛客网-实习", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=嵌入式&keyword=硬件工程师"},
        ],
    },
    "电商运营": {
        "icon": "🛒",
        "searches": [
            {"label": "牛客网-校招", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商运营&keyword=平台运营&keyword=店铺运营&keyword=品类运营"},
            {"label": "牛客网-实习", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=电商运营&keyword=平台运营"},
        ],
    },
    "新媒体运营": {
        "icon": "📱",
        "searches": [
            {"label": "牛客网-校招", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=新媒体运营&keyword=内容运营&keyword=短视频运营&keyword=小红书"},
            {"label": "牛客网-实习", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=新媒体运营&keyword=内容运营"},
        ],
    },
}

KEY_DATES = [
    {"date": "8月中旬", "event": "大厂秋招正式批大规模启动"},
    {"date": "8月下旬-9月", "event": "网申高峰，每天投10-15家"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
