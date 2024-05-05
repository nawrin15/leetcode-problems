import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns =['student_id', 'age'], dtype = int)
    return df 
    
    
data=[
    [ 3           , 'Bob      ' , 'Operations           ' , 48675  ],
    [ 90          , 'Alice    ' , 'Sales                ' , 11096  ],
    [ 9           , 'Tatiana  ' , 'Engineering          ' , 33805  ],
    [ 60          , 'Annabelle' , 'InformationTechnology' , 37678  ],
    [ 49          , 'Jonathan ' , 'HumanResources       ' , 23793  ],
    [ 43          , 'Khaled   ' , 'Administration       ' , 40454  ],
]

def getFirst3Row(df: pd.DataFrame):
    return df.iloc[:3]


data1 = pd.DataFrame(data, columns =['employee_id', 'name', 'department', 'salary'])

print(getFirst3Row(data1))
