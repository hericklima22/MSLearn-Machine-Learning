data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]

from array import array
from random import Random, randint
# from this import d
import numpy as np

grades = np.array(data)

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

students_age = []

for i in range(22):
    students_age.append(randint(18 ,50))

student_data = np.array([study_hours, grades, students_age])

import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1],
                            'Age':student_data[2]})


df_students.loc[5] # retorna o dado do index 5
df_students.loc[0:5] # retorna o dado em um range
df_students.iloc[0:5] #retorna os dados das 5 primeiras linhas

# print(students_age)
# print(df_students.iloc[4,[0,3]]) #retorna o valor das colunas do index [~, ~]
# print(df_students.loc[1,'Name']) #retorna o valor da coluna especifica na lista especificada [linha, 'nome_coluna']
# print(df_students.loc[df_students['Age'] <= 30]) #pode retornar as linahs que satisfazem a condição determinada
# print(df_students.query('Name=="Dan"')) # é a mesma coisa do de cima1
# print(df_students[df_students.Name == 'Aisha']) #pode especvificar o nome da coluna como um valor de index



########### carregando um DataFrame de um arquivo ############

# wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv
df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
print(df_students.head())