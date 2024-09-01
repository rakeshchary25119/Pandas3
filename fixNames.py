import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    res = []
    for i in range(len(users)):
        name = users['name'][i][0].upper() + users['name'][i][1:].lower()
        emp_id = users['user_id'][i]
        res.append([emp_id, name])

    return pd.DataFrame(res, columns=['user_id', 'name']).sort_values(['user_id'])