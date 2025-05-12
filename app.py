
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated data for importations
data = {
    'Mês': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06'] * 3,
    'NCM': ['8541.43.00'] * 6 + ['8504.40.40'] * 6 + ['8504.40.90'] * 6,
    'País de Origem': ['China', 'Alemanha', 'EUA', 'China', 'Alemanha', 'EUA'] * 3,
    'Município': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'São Paulo', 'Rio de Janeiro', 'Curitiba'] * 3,
    'Razão Social': ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Empresa E', 'Empresa F'] * 3,
    'CNPJ': ['00.000.000/0001-01', '00.000.000/0001-02', '00.000.000/0001-03', '00.000.000/0001-04', '00.000.000/0001-05', '00.000.000/0001-06'] * 3,
    'Valor FOB (USD)': [100000, 150000, 200000, 120000, 160000, 210000] * 3,
    'Potência (Wp)': [300, 320, 310, 300, 320, 310] * 3,
    'Tensão (V)': [24, 48, 36, 24, 48, 36] * 3,
    'Modelo': ['Modelo X', 'Modelo Y', 'Modelo Z', 'Modelo X', 'Modelo Y', 'Modelo Z'] * 3,
    'Fabricante': ['Fabricante A', 'Fabricante B', 'Fabricante C', 'Fabricante D', 'Fabricante E', 'Fabricante F'] * 3
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Análise de Importações de Módulos Fotovoltaicos e Inversores')

# Sidebar filters
st.sidebar.header('Filtros')
selected_ncm = st.sidebar.multiselect('Selecione o NCM', options=df['NCM'].unique(), default=df['NCM'].unique())
selected_months = st.sidebar.date_input('Selecione o período', [pd.to_datetime('2023-01-01'), pd.to_datetime('2023-06-30')])

# Convert selected_months to datetime64
selected_months = [pd.to_datetime(date) for date in selected_months]

# Filter data based on selections
filtered_df = df[df['NCM'].isin(selected_ncm)]
filtered_df = filtered_df[(pd.to_datetime(filtered_df['Mês']) >= selected_months[0]) & (pd.to_datetime(filtered_df['Mês']) <= selected_months[1])]

# Display filtered data
st.subheader('Dados Filtrados')
st.dataframe(filtered_df)

# Plotting
st.subheader('Gráficos de Importações')

# Bar plot for Valor FOB by NCM
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x='NCM', y='Valor FOB (USD)', hue='País de Origem', ax=ax)
ax.set_title('Valor FOB por NCM e País de Origem')
st.pyplot(fig)

# Export to Excel
st.subheader('Exportar Dados')
if st.button('Exportar para Excel'):
    filtered_df.to_excel('importacoes_fotovoltaicos.xlsx', index=False)
    st.success('Dados exportados para importacoes_fotovoltaicos.xlsx')
