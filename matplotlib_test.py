from click import pass_context
import pandas as pd

df_students = pd.read_csv('grades.csv', delimiter=',', header='infer')

#remove todas as linhas com dados faltantes
df_students = df_students.dropna(axis=0, how='any')

#calcula quem passou, assumindo que 60 é a nota para passar
passes = pd.Series(df_students['Grade'] >= 60)

#salva quem passou no dataframe do pandas
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

from matplotlib import pyplot as plt

# fig = plt.figure(figsize=(8, 3))

# #cria o gráfico de barra de nomes vs notas
# plt.bar(x=df_students.Name, height=df_students.Grade)

# plt.title("Notas dos estudantes")
# plt.xlabel("Estudante")
# plt.ylabel("Nota")
# plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# plt.xticks(rotation=90)

# plt.show()

#cria uma figura para 2 subplots (1 linha, 2 colunas)
fig, ax = plt.subplots(1, 2, figsize = (10,4))

#cria um plot em barra do nome vs nota no primeiro eixo
ax[0].bar(x=df_students.Name, height=df_students.Grade, color='orange')
ax[0].set_title("Notas")
ax[0].set_xticklabels(df_students.Name, rotation=90)


#cia um chart de torta dque passa o count no segundo eixo
pass_counts = df_students['Pass'].value_counts()
ax[1].pie(pass_counts, labels=pass_counts)
ax[1].set_title('Passando notas')
ax[1].legend(pass_counts.keys().tolist())


#adiciona um titulo para a figura
fig.suptitle('Dados dos estudantes')

fig.show()