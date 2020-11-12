import pandas as pd
df = pd.read_excel('contactos.xlsx')
list = df['contactos'].tolist()
print('[')
for row in range(10):

    print('\'' + list[row]+ '\',')
print(']')
