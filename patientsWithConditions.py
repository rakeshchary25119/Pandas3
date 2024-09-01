import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    res = []
    for i in range(len(patients)):
        p_id = patients['patient_id'][i]
        p_name = patients['patient_name'][i]
        conditions = patients['conditions'][i]
        for i in conditions.split(' '):
            if i.startswith('DIAB1'):
                res.append([p_id, p_name, conditions])
    print(*res)
    return pd.DataFrame(res, columns = ['patient_id', 'patient_name', 'conditions'])