####################################### importando bibliotecas #####################################

import pandas as pd

from IPython.display import display

####################################################################################################

###################################### lendo um excel ##############################################

vendas_df = pd.read_csv('tabela_vendas.csv', sep=';')

display(vendas_df)

##vendas_df.to_excel('C:/Users/thall/Desktop/exports/Tabela Vendas.xlsx',sheet_name='Tabela Vendas')

####################################################################################################