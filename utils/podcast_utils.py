import random
import numpy as np
import sqlite3
import pandas as pd
from typing import List, Dict, Optional, Sequence


def see_tables(database: str = "./data/database.sqlite") -> List:
    """
    See what tables are in a database

    Parameters:
    - database (str): The path to the SQLite database. Default is "database.sqlite".

    Returns:
    - List of tables (list)
    """
    see_tables_query = """
                       SELECT name 
                       FROM sqlite_master
                       WHERE type='table';
                       """

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        db_tables = cursor.execute(see_tables_query)
        list_of_tables = db_tables.fetchall()
        tables_in_db = ", ".join([str(i[0]) for i in list_of_tables])

    print(f'The tables in the current database are: "{tables_in_db}".')

    return list_of_tables


def query_to_df(query: str, database: str = "./data/database.sqlite") -> pd.DataFrame:
    """
    Read a table from the database and return a Pandas DataFrame

    Parameters:
    - query (str): The SQL query to execute.
    - database (str, optional): The path to the SQLite database. Default is "database.sqlite".

    Returns:
    pd.DataFrame: A Pandas DataFrame containing the query result.
    """
    with sqlite3.connect(database) as conn:
        return pd.read_sql_query(query, conn)


def extract_supercategory(category: str) -> str:
    """
    Extract the "supercategory" from a category name as structured as names divided by - and , characters

    Parameters:
    - category (str): category name or series of category names divided by - and ,

    Returns:
    -supercategory (str): string of the new "supercategory" name
    """
    if ',' in category:
        category = category.split(',')[0]
    return category.split('-')[0]


def grouping(supercategory: str, mapping: Optional[Dict[str, str]] = None) -> str:
    """
    Group supercategories according to specified mapping (or default mapping).

    Parameters:
    - supercategory (str): The supercategory to be grouped.
    - mapping (Optional[Dict[str, str]]): Mapping of supercategories to groups.
        If None, default mapping will be used.

    Returns:
    - str: The group to which the supercategory belongs.
    """
    if mapping is None:
        mapping = {'buddhism': 'spirituality',
                   'christianity': 'spirituality',
                   'hinduism': 'spirituality',
                   'islam': 'spirituality',
                   'judaism': 'spirituality',
                   'religion': 'spirituality',
                   'true': 'true-crime',
                   'society': 'society-culture',
                   'music': 'arts',
                   'tv': 'arts',
                   'news': 'news-government',
                   'government': 'news-government',
                   'technology': 'science-technology',
                   'science': 'science-technology'}
    if supercategory in mapping:
        return mapping[supercategory]
    else:
        return supercategory


def mean_diff_permutation(values: Sequence, n_obs_a: int, n_obs_b: int) -> float:
    """
    Calculate the mean difference for a single permutation of data from two groups of observations.

    Parameters:
    - values (Sequence): a Sequence such as a pandas series or list of values for all observations from
                         two independent groups.
    - n_obs_a (int): The number of observations in group A.
    - n_obs_b (int): The number of observations in group B.

    Returns:
    - float: The mean difference for a single permutation of the data from two groups of observations.
    """
    total_obs = n_obs_a + n_obs_b
    idx_a = set(random.sample(range(total_obs), n_obs_a))
    idx_b = set(range(total_obs)) - idx_a
    return values.iloc[list(idx_a)].mean() - values.iloc[list(idx_b)].mean()


def proportion_diff_permutation(labels: Sequence, n_obs_a: int, n_obs_b: int) -> float:
    """
    Calculate the proportion difference for a single permutation of data from two groups of observations.

    Parameters:
    - labels (Sequence): a Sequence such as a pandas series or list of category labels for all observations from
                         two independent groups.
    - n_obs_a (int): The number of observations in group A.
    - n_obs_b (int): The number of observations in group B.

    Returns:
    - float: The proportion difference for a single permutation of the data from two groups of observations.
    """
    total_obs = n_obs_a + n_obs_b
    idx_a = set(random.sample(range(total_obs), n_obs_a))
    idx_b = set(range(total_obs)) - idx_a
    group_a = labels.iloc[list(idx_a)]
    group_b = labels.iloc[list(idx_b)]
    proportion_a = group_a.value_counts().iloc[0]/group_a.value_counts().sum()
    proportion_b = group_b.value_counts().iloc[1]/group_b.value_counts().sum()
    
    return proportion_a - proportion_b

def bootstrap_confidence_interval_two_means(
        obs1: pd.Series,
        obs2: pd.Series,
        alpha: float = 0.05,
        n_bootstrap: int = 1000) -> tuple:
    """
    Calculate the bootstrap confidence interval for the difference between two means
    Parameters:
    - obs1 (pd.Series): dataset number 1
    - obs2 (pd.Series): dataset number 2
    - alpha (float): desired significance level
    - n_bootstrap (int): number of bootstrap samples
    
    Returns:
    - lower_bound (float): The lower bound of the confidence interval
    - upper_bound (float): The upper bound of the confidence
    """
    n_obs1, n_obs2 = len(obs1), len(obs2)

    bootstrap_means_diff = []
    for _ in range(n_bootstrap):
        bootstrap_sample1 = np.random.choice(obs1, size=n_obs1, replace=True)
        bootstrap_sample2 = np.random.choice(obs2, size=n_obs2, replace=True)

        mean1 = np.mean(bootstrap_sample1)
        mean2 = np.mean(bootstrap_sample2)

        means_diff = mean1 - mean2
        bootstrap_means_diff.append(means_diff)

    lower_bound = np.percentile(bootstrap_means_diff, 100 * alpha / 2)
    upper_bound = np.percentile(bootstrap_means_diff, 100 * (1 - alpha / 2))

    return lower_bound, upper_bound
