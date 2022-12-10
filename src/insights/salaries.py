from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data_job = read(path)
    get_max_salary = []
    for job in data_job:
        if job['max_salary'].isdigit():
            get_max_salary.append(int(job['max_salary']))
    return max(get_max_salary)

    raise NotImplementedError


def get_min_salary(path: str) -> int:
    data_job = read(path)
    get_min_salary = []
    for job in data_job:
        if job['min_salary'].isdigit():
            get_min_salary.append(int(job['min_salary']))
    return min(get_min_salary)

    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job does not have min_salary or max_salary")

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Job min_salary or max_salary is not a number")

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Job min_salary is greater than max_salary")

    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True

    else:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    salary_list = []
    try:
        for job in jobs:
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                salary_list.append(job)
    except ValueError:
        raise ValueError("Job does not have min_salary or max_salary")

    finally:
        return salary_list
