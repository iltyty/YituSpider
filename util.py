import os
import numpy as np
import pandas as pd

from child import Child

from pandas import DataFrame

COLUMNS = [
    '姓名',
    '检查号',
    '性别',
    '病人号',
    '年龄',
    '检查日期',
    'TW3 RUS 骨龄',
    'TW3 C 骨龄',
    '中华 05 骨龄',
    '图谱骨龄',
]


def init_res_excel(filename: str) -> DataFrame:
    if os.path.exists(filename):
        return pd.read_excel(filename)

    return DataFrame(columns=COLUMNS)


def save_to_excel(res: list[Child], filename='res.xlsx'):
    df = init_res_excel(filename)
    
    for c in res:
        row = [
            c.name,
            c.exam_id,
            c.gender,
            c.child_id,
            c.age,
            c.date,
            c.rus_bone,
            c.c_bone,
            c.zh_bone,
            c.img_bone
        ]

        df.loc[df.index.size] = row

    df.index = np.arange(1, len(df) + 1)
    df.to_excel(filename, index=False)