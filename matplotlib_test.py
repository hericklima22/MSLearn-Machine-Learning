import pandas as pd

df_students = pd.read_csv('grades.csv', delimiter=',', header='infer')

#remove todas as linhas com dados faltantes
df_students = df_students.dropna(axis=0, how='any')

#calcula quem passou, assumindo que 60 é a nota para passar
passes = pd.Series(df_students['Grade'] >= 60)

#salva quem passou no dataframe do pandas
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print(df_students)