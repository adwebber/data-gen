"""
Functions called by runner.py file. If you want to call these functions other
than from command line, they are here. Complex logic shouldn't be called
here, only sets of other functions.
"""
import logging
from datetime import datetime

import pandas as pd
import numpy as np


_logger = logging.getLogger(__name__)


def generate_time_series():
    num_people = 1000
    probability_of_positive = 0.1

    start_date = datetime(2010, 1, 1).date()
    most_recent_date = datetime(2018, 1, 1).date()
    df_c = pd.DataFrame([start_date, most_recent_date], columns=['c_date'])
    df_c['c_date'] = pd.to_datetime(df_c['c_date'])
    df_c.set_index('c_date', inplace=True)
    df_c = df_c.asfreq('D')
    df_c['c_id'] = range(len(df_c))
    df_c['global'] = True

    num_positive = np.random.binomial(num_people, probability_of_positive)
    num_negative = num_people - num_positive
    df_people = pd.DataFrame(list(range(num_people)), columns=['person_id'])
    df_people['positive'] = False
    df_people.loc[df_people['person_id'] < num_positive, 'positive'] = True
    df_people['global'] = True


    df_cp = cross_join(df_c, df_people)
    df_cp = df_cp.groupby('person_id').apply(add_outcome_date)

    
    # from IPython import embed
    # embed()


def cross_join(df1, df2):
    df1['global'] = True
    df2['global'] = True

    df_cj = df1.merge(df2, on='global', how='inner')
    df_cj.drop('global', axis=1, inplace=True)

    return df_cj


def add_outcome_date(df):
    if df['positive'].sum() > 0:
        df.loc[
            df['c_id'].sample(1).index[0], 'initial_positive_outcome_day'
        ] = True

    return df
