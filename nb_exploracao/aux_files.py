"""
Para armazenar documentoes, funcoes, variveis, dicionarios auxiliares aos notebooks
"""
import pandas as pd


# dicionario que contem as informacoes das colunas
aux_info_colunas = {
    'customerID': 'Número de identificação único de cada cliente',
    'Churn': 'Se o cliente deixou ou não a empresa',
    'gender': 'Gênero (masculino e feminino)' ,
    'SeniorCitizen': 'Informação sobre um cliente ter ou não idade igual ou maior que 65 anos',
    'Partner':  'Se o cliente possui ou não um parceiro ou parceira',
    'Dependents': 'Se o cliente possui ou não dependentes',
    'tenure':  'Meses de contrato do cliente',
    'PhoneService': 'Assinatura de serviço telefônico' ,
    'MultipleLines': 'Assisnatura de mais de uma linha de telefone' ,
    'InternetService': 'Assinatura de um provedor internet' ,
    'OnlineSecurity': 'Assinatura adicional de segurança online' ,
    'OnlineBackup': 'Assinatura adicional de backup online' ,
    'DeviceProtection': 'Assinatura adicional de proteção no dispositivo' ,
    'TechSupport': 'Assinatura adicional de suporte técnico, menos tempo de espera',
    'StreamingTV': 'Assinatura de TV a cabo',
    'StreamingMovies': 'Assinatura de streaming de filmes' ,
    'Contract': 'Tipo de contrato',
    'PaperlessBilling': 'Se o cliente prefere receber online a fatura',
    'PaymentMethod': 'Forma de pagamento',
    'Charges_Monthly': 'Total de todos os serviços do cliente por mês',
    'Charges_Total': 'Total gasto pelo cliente'
    }

# funcao para check dataframe
def df_check(df):
    
    # criando dataframe para verificacao
    check = pd.DataFrame({'name': df.columns})

    # verificando quantos valores unicos existem em cada  (numero maximo possivel 7267)
    check['nunique'] = df.nunique().values

    # verificando quantidades de nulos
    check['isnull'] = df.isnull().sum().values

    # verificando espacos faltantes
    temp_series1 = df[df.select_dtypes('object').columns].apply(lambda x: x.str.strip().isin(['']).sum()) # colunas str
    temp_series2 = df.select_dtypes(['float', 'integer']).isnull().sum() # colunas numericos
    temp_series = pd.concat([temp_series1, temp_series2])
    temp_series.name = 'blank'
    check = check.merge(temp_series, how='left', left_on='name', right_index=True)

    # verificando data type
    check['dtypes'] = df.dtypes.values

    # vericando quais os valores unicos para colunas com 5 ou menos valores unicos
    check['unique'] = df.apply(lambda x: x.unique() if x.nunique() <= 5 else '-').values

    return check


# dicionario traducao coluna
dict_traducao_coluna = {
    'customerID': 'ID', 
    'Churn': 'Churn',
    'gender': 'Genero',
    'SeniorCitizen': 'Senior',
    'Partner': 'Parceiro',
    'Dependents': 'Dependentes',
    'tenure': 'Meses_de_contrato',
    'PhoneService': 'Servico_telefonico',
    'MultipleLines': 'Multiplas_linhas_telefonicas',
    'InternetService': 'Servico_de_internet',
    'OnlineSecurity': 'Seguranca_online',
    'OnlineBackup': 'Backup_online',
    'DeviceProtection': 'Protecao_no_dispositivo',
    'TechSupport': 'Suporte_tecnico',
    'StreamingTV': 'TV_a_cabo',
    'StreamingMovies': 'Streaming_de_filmes',
    'Contract': 'Tipo_de_contrato',
    'PaperlessBilling': 'Fatura_online',
    'PaymentMethod': 'Metodo_de_pagamento',
    'Charges_Monthly': 'Cobrancas_mensais',
    'Charges_Total': 'Cobrancas_total'}


# classificando colunas em (identificao, qualitativos e quantitativos)
def classvar(df):
    identificadora = ['customerID']
    quantitativas = ['tenure', 'Charges_Monthly', 'Charges_Total']
    qualitativas = df.drop(quantitativas + identificadora, axis=1).columns.tolist()
    return {
        'identificadora': identificadora,
        'quantitativas': quantitativas,
        'qualitativas': qualitativas
        }

categorical_maps = {
    'Churn' : {
        'No': 0,
        'Yes': 1,
    },
    'gender': {
        'Female': 0,
        'Male': 1
    },
    'SeniorCitizen': {
        'No': 0, # menos de 65
        'Yes': 1 # 65 ou mais
    },
    'Partner': {
        'Yes': 1,
        'No': 0
    },
    'Dependents': {
        'Yes': 1,
        'No': 0
    },
    'PhoneService': {
        'Yes': 1,
        'No': 0
    },
    'MultipleLines': {
        'Yes': 2,
        'No': 1,
        'No phone service' : 0
    },
    'InternetService': {
        'DSL': 1,
        'Fiber optic': 2,
        'No': 0
    },
    'OnlineSecurity': {
        'No': 1,
        'Yes': 2,
        'No internet service': 0
    },
    'OnlineBackup': {
        'Yes': 2,
        'No': 1, 
        'No internet service': 0
    },
    'DeviceProtection': {
        'Yes': 2,
        'No': 1, 
        'No internet service': 0
    },
    'TechSupport': {
        'Yes': 2,
        'No': 1, 
        'No internet service': 0
    },
    'StreamingTV': {
        'Yes': 2,
        'No': 1, 
        'No internet service': 0
    },
    'StreamingMovies': {
        'Yes': 2,
        'No': 1, 
        'No internet service': 0
    },
    'Contract': {
        'One year': 12,
        'Month-to-month': 1,
        'Two year': 24
    },
    'PaperlessBilling': {
        'Yes': 1,
        'No': 0
    },
    'PaymentMethod': {
        'Mailed check':0,
        'Electronic check':1,
        'Credit card (automatic)':2,
        'Bank transfer (automatic)':3
    }
}