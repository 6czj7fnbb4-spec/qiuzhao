"""
岗位筛选 + 三档分类逻辑
"""
import json
import os
from config import TRACKS, LOCATIONS, EXCLUDE_TERMS, COMPANIES_REACH, COMPANIES_SAFE

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "sent_jobs.json")


def load_sent_jobs():
    """加载已推送过的岗位记录"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_sent_jobs(record):
    """保存已推送记录"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)


def should_exclude(job):
    """检查是否应排除（学历/经验门槛不符）"""
    text = job.get("title", "") + job.get("company", "")
    for term in EXCLUDE_TERMS:
        if term in text:
            return True
    return False


def match_location(job):
    """检查工作地点是否匹配"""
    text = job.get("title", "") + job.get("company", "")
    for loc in LOCATIONS:
        if loc in text:
            return True
    # 如果没有明确地点信息，也保留（可能是全国招聘）
    return True


def match_track(job, track_name):
    """检查岗位是否匹配某条路线"""
    keywords = TRACKS[track_name]["keywords"]
    exclude_kws = TRACKS[track_name]["exclude"]
    text = job.get("title", "") + job.get("company", "")

    # 先看是否命中排除词
    for kw in exclude_kws:
        if kw in text:
            return False

    # 再看是否命中关键词
    for kw in keywords:
        if kw in text:
            return True
    return False


def classify_tier(job):
    """三档分类"""
    company = job.get("company", "")
    # 冲一冲
    for c in COMPANIES_REACH:
        if c in company:
            return "reach"
    # 稳拿到
    for c in COMPANIES_SAFE:
        if c in company:
            return "safe"
    # 其余
    return "chance"


def filter_and_classify(all_jobs):
    """
    对所有岗位进行筛选和三档分类
    返回: {
        "嵌入式/硬件工程师": {"reach": [...], "safe": [...], "chance": [...]},
        "电商运营": {...},
        "新媒体运营": {...}
    }
    """
    sent = load_sent_jobs()
    result = {}
    new_sent_ids = []

    for track_name in TRACKS:
        result[track_name] = {"reach": [], "safe": [], "chance": []}

    for job in all_jobs:
        # 去重：用 link 或 title+company 作为唯一标识
        job_id = job.get("link", "") or (job.get("title", "") + job.get("company", ""))
        if job_id and job_id in sent:
            continue

        # 排除不符合学历/经验的
        if should_exclude(job):
            continue

        # 地点过滤
        if not match_location(job):
            continue

        # 匹配路线 + 三档分类
        for track_name in TRACKS:
            if match_track(job, track_name):
                tier = classify_tier(job)
                result[track_name][tier].append(job)

        if job_id:
            new_sent_ids.append(job_id)

    # 记录已推送（避免每天重复）
    for jid in new_sent_ids:
        sent[jid] = True
    save_sent_jobs(sent)

    return result
