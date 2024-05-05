import pandas as pd

def createDataframe(student_data) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns =['student_id', 'age'], dtype = int)
    return df 
    
    
data_1=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

print(createDataframe(data_1))