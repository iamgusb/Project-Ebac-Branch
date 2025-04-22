import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/Project-Ebac/gasolina.csv")
df.head()

with sns.axes_style('whitegrid'):

  goal = sns.lineplot(data=df, x="dia", y="venda")
  goal.set(title='Preço médio gasolina', xlabel='Dia', ylabel='Média de venda');

plt.savefig("gasolina.png")