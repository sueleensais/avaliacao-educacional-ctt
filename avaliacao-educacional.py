#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# carregando os dados
df = pd.read_csv("dados-simulados.csv")
print(df.head())


# In[3]:


# calculando as dificuldade das questões
dificuldade = df.mean()
print(dificuldade)

# valor próximo a 1.0: questão fácil
# valor próximo a 0.0: questão difícil


# In[4]:


# calculando a discriminação das questões entre alunos de diferentes níveis de desempenho

# pontuação total de cada aluno
df["total"] = df.sum(axis=1)

# ordenando os alunos por total de pontos
df_sorted = df.sort_values("total")

# definindo os grupos inferior e superior
n = int(len(df) * 0.27)
grupo_inferior = df_sorted.iloc[:n]
grupo_superior = df_sorted.iloc[-n:]

# calculando a discriminação de cada questão
discriminacao = grupo_superior.mean() - grupo_inferior.mean()
print(discriminacao)

# valores positivos: discriminação boa
# valores próximos de 0: discriminação fraca
# valores negativos: indica problema (os alunos fracos acertaram mais do que os alunos fortes)


# In[5]:


# juntando resultados: dificuldade e discriminação
resultado = pd.DataFrame({
    "Dificuldade": dificuldade,
    "Discriminação": discriminacao
})

# removendo a linha "total"
resultado = resultado.drop("total", errors="ignore")
print(resultado)

# interpretação:
# Coluna dificuldade: demonstra se a questão é fácil (valor alto) ou difícil (valor baixo)
# Coluna discriminação: demonstra se a questão diferencia bem os alunos (valor positivo e alto)
# Questões com alta dificuldade e baixa discriminação podem ser muito fáceis e pouco úteis. 
# Questões com baixa dificuldade e boa discriminação são boas para avaliações.
# Questões com discriminação negativas devem ser revisadas.


# In[6]:


# criando gráfico
ax = resultado.plot(kind="bar", figsize=(10,6))
plt.title("Dificuldade e Discriminação das Questões")
plt.xlabel("Questões")
plt.ylabel("Valores")
plt.axhline(0, color = "black", linewidth = 0.8)
plt.legend(loc = "best")
plt.show()


# In[7]:


# criando coluna de interpretação das questões

# criando função
# regras de interpretação: Boa: discriminação > 0.30 | Fraca: 0 < discriminação <= 0.30 | Revisar: discriminação <= 0
def interpretar_item(row):
    if row["Discriminação"] > 0.3:
        return "Boa"
    elif row["Discriminação"] > 0:
        return "Fraca"
    else:
        return "Revisar"

# aplicando função no dataframe
resultado["Interpretação"] = resultado.apply(interpretar_item, axis=1)

# visualizando tabela final
print(resultado)


# In[ ]:




