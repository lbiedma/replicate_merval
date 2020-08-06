import requests
import pandas as pd
import numpy as np
from io import StringIO

### Lista de acciones argentinas ###
stocks_list = [
    'AGRO', 'ALUA', 'APBR', 'AUSO', 'BBAR', 'BHIP',
    'BMA', 'BOLT', 'BPAT', 'BRIO', 'BYMA', 'CARC',
    'CAPU', 'CELU', 'CEPU', 'CGPA2', 'COME', 'CRES',
    'CTIO', 'CVH', 'DGCU2', 'EDN', 'GCLA', 'GGAL', 'HAVA',
    'INDU', 'IRSA', 'LEDE', 'LOMA', 'LONG', 'METR', 'MIRG',
    'MOLA', 'MOLI', 'MORI', 'OEST', 'PAMP',
    'PATY', 'PGR', 'SAMI', 'SUPV', 'TECO2', 'TGLT', 'TGNO4',
    'TGSU2', 'TRAN', 'TS', 'TXAR', 'VALO', 'YPFD',
    ### Agregamos el índice de acciones argentinas: Merval
    'MERVAL',
]

### Obtengamos los datos y los guardemos por si las moscas...
for stock in stocks_list:
    url = 'http://www.ravabursatil.com/v2/empresas/precioshistoricos.php?e={}&csv=1'.format(stock)
    req = requests.get(url, allow_redirects=True)
    df = pd.read_csv(StringIO(req.content.decode("utf-8")))
    name = './stocks/{}.csv'.format(stock)
    df.to_csv(name)
