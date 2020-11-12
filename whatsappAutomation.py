import numpy as np
import pandas as pd
from pandas import ExcelWriter
import rpa as r


numErroneosURL = []
numErroneos = []
cantidadEnviados=0
cantidadNoEnviados=0

r.init(visual_automation = True)
atmNumber ='a'
tempNum = 'a'
n =0
df = pd.read_excel('contactos.xlsx')
list = df['contactos'].tolist()

#list = [
#'https://api.whatsapp.com/send?phone=52133130980341&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
#'https://api.whatsapp.com/send?phone=5213313098034&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
#'https://api.whatsapp.com/send?phone=5213331385311&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
#'https://api.whatsapp.com/send?phone=52133130980341&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
#'https://api.whatsapp.com/send?phone=5213336771556&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
#'https://api.whatsapp.com/send?phone=5213318830312&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D'

#]
#for i in range(282):
for i in range(len(list)):

    print("Posicion: " + str(i))
    #print(list[i])
    r.url(list[i])
    reps=0
    err=False
    while tempNum==atmNumber:
        reps+=1
        if reps>5:
            break
    #    checkWhatsError = r.read('//*[@id="fallback_block"]/div/a')
    #    print('Error '+ checkWhatsError)
    #    if checkWhatsError == 'Descargar':
    #        print('Error found')
    #        err=True
    #        break
        tempNum = r.read('//*[@id="main_block"]/div[1]/h1/p/span')
        print(atmNumber +  " ==? " + tempNum)
        if n ==0:
            break
        r.wait(0.2)
    #if err:
    #    continue
    if reps >5:
        print('Atasco capturar este error')
        numErroneosURL.append(list[i])
        numErroneos.append(atmNumber)
        cantidadNoEnviados +=1
        continue
    atmNumber = tempNum
    r.click('//*[@id="action-button"]')
    r.wait(0.3)
    s = r.read(580, 350,850,400)
    print(s)
    if s == "Phone number shared via url is invalid.":
        print("Numero erroneo")
        numErroneosURL.append(list[i])
        numErroneos.append(atmNumber)
        cantidadNoEnviados +=1
        #r.hover(900, 450)
        #r.mouse('down')
        #r.mouse('up')
    else:
        print("numero correcto")
        cantidadEnviados+=1
        r.keyboard('[enter]')
        r.keyboard('[enter]')



    n=1
listNumCor=[]
listNumIncor =[]
listNumCor.append(cantidadEnviados)
listNumIncor.append(cantidadNoEnviados)

resultados = pd.DataFrame({"URL Fallidos":numErroneosURL,"Numeros Fallidos":numErroneos})
resultados2 =pd.DataFrame({"Numero Total de Fallas": listNumIncor,"Numero Total Enviados":listNumCor})
resultados2 = pd.concat([resultados2,resultados], ignore_index=True, axis=1)
writeron = pd.ExcelWriter('HojadeResultados.xlsx', engine='xlsxwriter')
with ExcelWriter('HojadeResultados.xlsx') as writer:
    #for n, df in enumerate(dfLists):
    resultados2.to_excel(writer,sheet_name='Resultados', index=False)
    writer.save()
r.close()
