import pandas as pd

df_students = pd.read_csv('grades.csv', delimiter=',', header='infer')

#remove todas as linhas com dados faltantes
df_students = df_students.dropna(axis=0, how='any')

#calcula quem passou, assumindo que 60 é a nota para passar
# passes = pd.Series(df_students['Grade'] >= 60)

# #salva quem passou no dataframe do pandas
# df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

from matplotlib import pyplot as plt
plt.rcParams['interactive'] == True

# fig = plt.figure(figsize=(8, 3))

# #cria o gráfico de barra de nomes vs notas
# plt.bar(x=df_students.Name, height=df_students.Grade)

# plt.title("Notas dos estudantes")
# plt.xlabel("Estudante")
# plt.ylabel("Nota")
# plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# plt.xticks(rotation=90)

# plt.show()

# #cria uma figura para 2 subplots (1 linha, 2 colunas)
# fig, ax = plt.subplots(1, 2, figsize = (10,4))

# #cria um plot em barra do nome vs nota no primeiro eixo
# ax[0].bar(x=df_students.Name, height=df_students.Grade, color='orange')
# ax[0].set_title("Notas")
# ax[0].set_xticklabels(df_students.Name, rotation=90)


# #cia um chart de torta dque passa o count no segundo eixo
# pass_counts = df_students['Pass'].value_counts()
# ax[1].pie(pass_counts, labels=pass_counts)
# ax[1].set_title('Passando notas')
# ax[1].legend(pass_counts.keys().tolist())


# #adiciona um titulo para a figura
# fig.suptitle('Dados dos estudantes')

# fig.show()


# var_data = df_students['Grade']

# fig = plt.figure(figsize=(10,4))

# # plota o histograma
# plt.hist(var_data)

# #adiciona titulo e labels
# plt.title('Distribuicao de dados')
# plt.xlabel('Valor')
# plt.ylabel('Frequencia')


#pega a variavel para examinar
# var = df_students['Grade']
# print(var)

# min_val = var.min()
# max_val = var.max()
# mean_val = var.mean()
# med_val = var.median()
# mod_val = var.mode()[0]

# print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
#                                                                                         mean_val,
#                                                                                         med_val,
#                                                                                         mod_val,
#                                                                                         max_val))

# fig = plt.figure(figsize=(10, 4))

# #cria o histograma
# plt.hist(var)

# #desenha as linhas das estatísticas
# plt.axvline(x=min_val, color='gray', linestyle='dashed', linewidth = 2)
# plt.axvline(x=max_val, color='cyan', linestyle='dashed', linewidth = 2)
# plt.axvline(x=mean_val, color='red', linestyle='dashed', linewidth = 2)
# plt.axvline(x=med_val, color='yellow', linestyle='dashed', linewidth = 2)
# plt.axvline(x=mod_val, color='gray', linestyle='dashed', linewidth = 2)


# plt.title("Distribuicao de dados")
# plt.xlabel('Valor')
# plt.ylabel('Frequencia')

# fig.show()

# var = df_students['Grade']

# fig = plt.figure(figsize=(10,4))

# plt.boxplot(var)
# plt.title('Distribuicao de dados')

# fig.show()


def show_distribution(var_data):
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.max()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                            mean_val,
                                                                                            med_val,
                                                                                            mod_val,
                                                                                            max_val))

    fig, ax = plt.subplots(2, 1, figsize=(10,4))

    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequencia')

    ax[0].axvline(x=min_val, color='gray', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=max_val, color='cyan', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=mean_val, color='red', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=med_val, color='yellow', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=mod_val, color='gray', linestyle='dashed', linewidth = 2)

    ax[1].boxplot(var_data, vert=False)
    ax[1].set_label('Valor')

    fig.suptitle('Distribuicao de dados')

    plt.show()


def show_density(var_data):
    fig = plt.figure(figsize=(10,4))

    var_data.plot.density()

    plt.title('Densidade de dados')

    plt.axvline(x=var_data.mean(), color='cyan', linestyle = 'dashed', linewidth = 2)
    plt.axvline(x=var_data.median(), color='red', linestyle = 'dashed', linewidth = 2)
    plt.axvline(x=var_data.mode()[0], color='yellow', linestyle = 'dashed', linewidth = 2)

    plt.show()

col = df_students['Grade']

# show_distribution(col)
show_density(col)