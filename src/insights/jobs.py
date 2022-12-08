from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        data_job = csv.DictReader(file)
        job_list = []
        for job in data_job:
            job_list.append(job)
        return job_list

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data_job = read(path)
    job_types = []
    for job in data_job:
        if job['job_type'] not in job_types:
            job_types.append(job['job_type'])
    return job_types
    
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
