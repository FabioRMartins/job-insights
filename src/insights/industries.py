from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data_job = read(path)
    industries = []
    for job in data_job:
        if job["industry"] != "":
            if job['industry'] not in industries:
                industries.append(job['industry'])
    return industries

    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_list = []
    for job in jobs:
        if job['industry'] == industry:
            industry_list.append(job)
    return industry_list

    raise NotImplementedError
