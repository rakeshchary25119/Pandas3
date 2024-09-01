import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    res = []
    for i in range(len(employees)):
        emp_id = employees['employee_id'][i]
        name = employees['name'][i]

        if emp_id % 2 != 0 and not name.startswith('M'):
            res.append([emp_id, employees['salary'][i]])
        else:
            res.append([emp_id, 0])
    
    df = pd.DataFrame(res, columns = ['employee_id', 'bonus']).sort_values(['employee_id'])
    return df