import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure
from dash import Dash, dcc, html
import plotly.graph_objects as go

# Gráfico de Histograma
def cria_graficos(df):
    figure: Figure = px.histogram(df, x='Nota', nbins=30, title='Distribuição de Notas')

# Gráfico de Dispersão
    figure1: Figure = px.scatter(df, x='N_Avaliações', y='Nota', color='Título', hover_data=['Qtd_Vendidos'])
    figure1.update_layout(
        title='Número de Avaliações vs Nota por Produto',
        xaxis_title='N_Avaliações',
        yaxis_title='Nota'
    )

# Gráfico de Mapa de Calor
    df_corr = df[['Desconto','Preço']].corr()
    figure2: Figure = px.imshow(df_corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Mapa de Calor de Correlação')

# Gráfico de Barra
    figure3: Figure = px.bar(df, x='Qtd_Vendidos', y='Marca', color='Marca', barmode='group', color_discrete_sequence=px.colors.qualitative.Plotly)
    figure3.update_layout(
        title='Quantidade de Produtos Vendidos por Marca',
        xaxis_title='Quantidade de Produtos Vendidos',
        yaxis_title='Marcas',
        plot_bgcolor='rgba(222, 255, 253, 1)',
        paper_bgcolor='rgba(186, 245, 241, 1)'
    )

# Gráfico de Pizza
    figure4: Figure = px.pie(df, names='Qtd_Vendidos', color='Qtd_Vendidos', color_discrete_sequence=px.colors.sequential.RdBu, title='Proporção de Vendas por Produto')

# Gráfico de Densidade
    x = df['Nota']
    y = df['Qtd_Vendidos']

    figure5 = go.Figure(go.Histogram2d(
        x=x,
        y=y,
        histnorm='probability',
        colorscale='Viridis'
    ))

    figure5.update_layout(
        title='Tabela de Densidade Entre Quantidades Vendidas e Nota',
        xaxis_title='Nota',
        yaxis_title='Quantidades Vendidas'
    )

# Gráfico de Regressão
    figure6: Figure = px.scatter(df, x='Nota', y='Preço', trendline_color_override='#278f65')
    figure6.update_layout(
        title='Quantidade de Notas por Preço',
        xaxis_title='Nota',
        yaxis_title='Preço'
    )

    return figure, figure1, figure2, figure3, figure4, figure5, figure6

# Cria Apps
def cria_apps():
    app = Dash(__name__)

    df = pd.read_csv('C:\\Users\\jtsar\\Downloads\\ecommerce_estatistica.csv')

    figure, figure1, figure2, figure3, figure4, figure5, figure6 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=figure.to_dict()),
        dcc.Graph(figure=figure1.to_dict()),
        dcc.Graph(figure=figure2.to_dict()),
        dcc.Graph(figure=figure3.to_dict()),
        dcc.Graph(figure=figure4.to_dict()),
        dcc.Graph(figure=figure5.to_dict()),
        dcc.Graph(figure=figure6.to_dict())
    ])
    return app

# Executa App
if __name__ == '__main__':
    app = cria_apps()
    app.run_server(debug=True, port=8050)