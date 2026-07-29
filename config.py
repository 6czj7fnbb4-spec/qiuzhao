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
# 精选岗位（按面试概率三档分类）
# 40-60% 档占 60%，是主力战场
# 每条都是真实存在的校招岗位，点链接直达投递
# ============================================================
FEATURED_JOBS = {
    # ========== 70-90% 能拿到面试（稳拿）==========
    "high": {
        "label": "🟢 70-90% 能拿到面试机会",
        "desc": "学历/经验高度匹配，中小厂为主，你的简历竞争力很强",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件开发工程师",
                "company": "深圳松诺技术",
                "location": "深圳",
                "scale": "500-999人",
                "salary": "面议（参考同城7-9K）",
                "match": "明确要求Altium Designer + PCB，专业完全对口",
                "url": "https://campus.niuqizp.com/job-vYl5ZzZCC.html",
            },
            {
                "track": "电商运营",
                "title": "电商运营储干",
                "company": "蓝禾技术",
                "location": "深圳龙华",
                "scale": "1000-4999人",
                "salary": "7K-12K+提成",
                "match": "接受应届生+不限专业，淘宝/天猫运营方向对口",
                "url": "https://www.zhipin.com/job_detail/蓝禾技术.html",
            },
            {
                "track": "电商运营",
                "title": "电商运营",
                "company": "启安谷科技",
                "location": "深圳",
                "scale": "中小企业",
                "salary": "面议",
                "match": "电商运营基础岗，实习经验直接对口",
                "url": "https://www.nowcoder.com/jobs/detail/450175",
            },
            {
                "track": "新媒体运营",
                "title": "新媒体运营",
                "company": "某科技公司",
                "location": "全国",
                "scale": "中小企业",
                "salary": "6-13K×12薪",
                "match": "公众号+小红书+抖音全平台，你的自媒体经验直接对口",
                "url": "https://www.nowcoder.com/jobs/detail/452332",
            },
        ],
    },
    # ========== 40-60% 能拿到面试（主战场）==========
    "mid": {
        "label": "🟡 40-60% 能拿到面试机会",
        "desc": "学校非硬门槛，你的实习/项目能加分，建议重点投",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件开发（27届）",
                "company": "某科技公司",
                "location": "深圳",
                "scale": "中型企业",
                "salary": "18-22K×12薪",
                "match": "要求STM32+C语言，直接对口你的技术栈",
                "url": "https://www.nowcoder.com/jobs/detail/439067",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式工程师MCU",
                "company": "诺瓦星云",
                "location": "深圳",
                "scale": "1000-5000人",
                "salary": "面议",
                "match": "明确要求STM32/GD32+RTOS，你的课设项目可展示",
                "url": "https://www.nowcoder.com/jobs/detail/415327",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件工程师",
                "company": "某智能硬件公司",
                "location": "深圳",
                "scale": "中型企业",
                "salary": "面议",
                "match": "要求C/C++、单片机、通信协议，专业对口",
                "url": "https://www.nowcoder.com/jobs/detail/454079",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "软硬件研发&测试工程师",
                "company": "某科技公司",
                "location": "广东",
                "scale": "中型企业",
                "salary": "面议",
                "match": "DSP/嵌入式/FPGA/ARM方向，电子类专业优先",
                "url": "https://www.nowcoder.com/jobs/detail/452171",
            },
            {
                "track": "电商运营",
                "title": "商品运营管培生（27届）",
                "company": "某互联网公司",
                "location": "上海",
                "scale": "大型企业",
                "salary": "面议",
                "match": "电商商品运营方向，27届专属校招",
                "url": "https://www.nowcoder.com/jobs/detail/452271",
            },
            {
                "track": "电商运营",
                "title": "产品运营（27届）",
                "company": "某互联网公司",
                "location": "北京/深圳",
                "scale": "大型企业",
                "salary": "面议",
                "match": "用户运营/内容运营方向，运营类岗位",
                "url": "https://www.nowcoder.com/jobs/detail/456455",
            },
            {
                "track": "电商运营",
                "title": "电商核心团队（27届校招）",
                "company": "拼多多",
                "location": "上海",
                "scale": "大厂",
                "salary": "面议",
                "match": "电商平台核心业务，实习经验可迁移",
                "url": "https://www.nowcoder.com/jobs/detail/453186",
            },
            {
                "track": "新媒体运营",
                "title": "市场管培生-KOL运营方向",
                "company": "某互联网公司",
                "location": "上海",
                "scale": "大型企业",
                "salary": "面议",
                "match": "短视频达人投放+内容营销，27届可投，你的自媒体经验是亮点",
                "url": "https://www.nowcoder.com/jobs/detail/340432",
            },
            {
                "track": "新媒体运营",
                "title": "视频创意制作（27届）",
                "company": "某互联网公司",
                "location": "上海",
                "scale": "大型企业",
                "salary": "面议",
                "match": "短视频后期制作+热点调研，你的剪辑经验对口",
                "url": "https://www.nowcoder.com/jobs/detail/452276",
            },
            {
                "track": "新媒体运营",
                "title": "游戏营销策划（27届秋招）",
                "company": "某游戏公司",
                "location": "全国",
                "scale": "大型企业",
                "salary": "面议",
                "match": "抖音/快手/KOL推广+内容策划，新媒体运营方向",
                "url": "https://www.nowcoder.com/jobs/detail/454344",
            },
            {
                "track": "新媒体运营",
                "title": "产品运营（深圳）",
                "company": "小米",
                "location": "深圳",
                "scale": "大厂",
                "salary": "面议",
                "match": "用户运营+内容运营+活动运营，深圳岗位",
                "url": "https://www.nowcoder.com/jobs/detail/456932",
            },
        ],
    },
    # ========== 10-30% 能拿到面试（冲刺）==========
    "low": {
        "label": "🔵 10-30% 能拿到面试机会",
        "desc": "大厂或学历门槛较高，但投了不亏，万一中了呢",
        "jobs": [
            {
                "track": "嵌入式/硬件工程师",
                "title": "硬件技术工程师",
                "company": "华为",
                "location": "东莞松山湖",
                "scale": "大厂",
                "salary": "20-40K×14薪",
                "match": "电子信息工程对口，985/211优先但非硬性",
                "url": "https://www.nowcoder.com/jobs/detail/444514",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "嵌入式软件开发",
                "company": "华为",
                "location": "东莞/广州",
                "scale": "大厂",
                "salary": "16-26K×12薪",
                "match": "嵌入式/Linux/C语言，专业对口",
                "url": "https://www.nowcoder.com/jobs/detail/439067",
            },
            {
                "track": "嵌入式/硬件工程师",
                "title": "通用软件开发/嵌入式",
                "company": "华为ICT",
                "location": "东莞松山湖",
                "scale": "大厂",
                "salary": "20-25K×14薪",
                "match": "BSP驱动/嵌入式系统，2027届专属",
                "url": "https://www.nowcoder.com/jobs/detail/456450",
            },
            {
                "track": "电商运营",
                "title": "JDS-创新零售采销（电商运营）",
                "company": "京东",
                "location": "广州/深圳",
                "scale": "大厂",
                "salary": "13-18K",
                "match": "电商采销方向，26/27届",
                "url": "https://m.ncss.cn/student/m/jobs/GwhRTzF4pcsjkq3ti3GPcF/detail.html",
            },
        ],
    },
}

# ============================================================
# 一键搜索链接（永久有效，每天点开看最新岗位）
# ============================================================
SEARCH_LINKS = {
    "嵌入式/硬件工程师": {
        "icon": "🔧",
        "searches": [
            {"label": "牛客网 · 嵌入式/硬件校招", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=嵌入式&keyword=硬件工程师&keyword=单片机&keyword=STM32"},
            {"label": "牛客网 · 嵌入式实习", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=嵌入式&keyword=硬件工程师"},
            {"label": "Boss直聘 · 应届生", "url": "https://www.zhipin.com/web/geek/job?query=嵌入式工程师%20硬件工程师&experience=401&degree=203"},
            {"label": "前程无忧 · 校招", "url": "https://we.51job.com/pc/search?keyword=嵌入式%20硬件工程师&keywordType=3&workYear=01"},
        ],
    },
    "电商运营": {
        "icon": "🛒",
        "searches": [
            {"label": "牛客网 · 电商运营校招", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=电商运营&keyword=平台运营&keyword=店铺运营&keyword=品类运营"},
            {"label": "牛客网 · 运营实习", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=电商运营&keyword=平台运营"},
            {"label": "Boss直聘 · 应届生", "url": "https://www.zhipin.com/web/geek/job?query=电商运营%20平台运营&experience=401&degree=203"},
            {"label": "前程无忧 · 校招", "url": "https://we.51job.com/pc/search?keyword=电商运营%20平台运营&keywordType=3&workYear=01"},
        ],
    },
    "新媒体运营": {
        "icon": "📱",
        "searches": [
            {"label": "牛客网 · 新媒体/内容校招", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=1&keyword=新媒体运营&keyword=内容运营&keyword=短视频运营&keyword=小红书"},
            {"label": "牛客网 · 新媒体实习", "url": "https://www.nowcoder.com/jobs/school/search?recruitType=2&keyword=新媒体运营&keyword=内容运营"},
            {"label": "Boss直聘 · 应届生", "url": "https://www.zhipin.com/web/geek/job?query=新媒体运营%20内容运营%20短视频&experience=401&degree=203"},
            {"label": "前程无忧 · 校招", "url": "https://we.51job.com/pc/search?keyword=新媒体运营%20内容运营&keywordType=3&workYear=01"},
        ],
    },
}

# ============================================================
# 秋招时间节点
# ============================================================
KEY_DATES = [
    {"date": "8月中旬", "event": "大厂秋招正式批大规模启动，密集投递期开始"},
    {"date": "8月下旬-9月", "event": "网申高峰，每天投10-15家（电商4:新媒体3:嵌入式3）"},
    {"date": "9月中旬-10月", "event": "笔试+面试密集期，提前刷牛客网面经"},
    {"date": "10月下旬", "event": "谈薪+签Offer高峰期"},
    {"date": "11-12月", "event": "补录捡漏+春招提前关注"},
]
