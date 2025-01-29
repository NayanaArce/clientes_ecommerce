import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:\\Users\\jtsar\\Downloads\\ecommerce_estatistica.csv')

# Histograma
print(df.head().to_string())
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Notas')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Dispersão
plt.scatter(df['N_Avaliações'], df['N_Avaliações'])
plt.title('Dispersão - Número de Avaliações e Número de Avaliações')
plt.xlabel('N_Avaliações')
plt.ylabel('N_Avaliações')
plt.show()

# Mapa de Calor
corr = df[['Desconto', 'Preço']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Preço e Desconto')
plt.show()

# Gráfico de barra
plt.figure(figsize=(10, 6))
df['Qtd_Vendidos'].value_counts().plot(kind='bar', color='#90ee70').width=(0,8)
plt.title('Quantidade de Vendas Por Marca')
plt.xlabel('Qtd_Vendidos')
plt.ylabel('Marca')
plt.xticks(rotation=0)
plt.show()

# Gráfico de Pizza
x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Proporção de Vendas Por Produto')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Qtd_Vendidos_Cod'], fill=True, color='#863e9c')
plt.title('Densidade de Vendas')
plt.xlabel('Qtd_Vendidos_Cod')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Nota', y='Preço', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color':'#34c289'})
plt.xlabel('Nota')
plt.ylabel('Preço')
plt.show()