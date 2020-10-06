import numpy as np
import pandas as pd
from pandas import ExcelWriter
import rpa as r
list = [
'https://api.whatsapp.com/send?phone=52133130980341&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
'https://api.whatsapp.com/send?phone=5213313098034&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
'https://api.whatsapp.com/send?phone=5213331385311&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
'https://api.whatsapp.com/send?phone=52133130980341&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
'https://api.whatsapp.com/send?phone=5213336771556&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D',
'https://api.whatsapp.com/send?phone=5213318830312&text=%C2%A1Hola!%20%F0%9F%91%8B%F0%9F%91%8B%20frutas%20y%20verdura%20para%20cuidar%20el%20sistema%20inmune%20de%20tu%20familia%3A%20%20%20%20%20%0A%F0%9F%8D%8AMandarina%20%2424.3%2Fkg%20a%20%2420.0%2Fkg%0A%F0%9F%A5%ACApio%20%2437%2Fkg%20a%20%2426%2Fkg%0A%F0%9F%8D%97Pollo%20%2494%2Fkg%20a%20%2475%2Fkg%0A%F0%9F%A5%ACEsp%C3%A1rragos%20%24101%2Fkg%20a%20%2484%2Fkg%0A%F0%9F%8D%8D%F0%9F%8D%8D%F0%9F%8D%8D'

]
r.init(visual_automation = True)
atmNumber ='a'
tempNum = 'a'
n =0
for i in list:

    r.url(i)
    while tempNum==atmNumber:
        tempNum = r.read('//*[@id="main_block"]/div[1]/h1/p/span')
        print(atmNumber +  " ==? " + tempNum)
        if n ==0:
            break
        r.wait(0.2)
    atmNumber = tempNum
    r.click('//*[@id="action-button"]')
    r.wait(0.3)
    s = r.read(580, 350,850,400)

    if s == "Phone number shared via url is invalid.":
        print("Numero erroneo")
        #r.hover(900, 450)
        #r.mouse('down')
        #r.mouse('up')
    else:
        print("numero correcto")
        r.keyboard('[enter]')
        r.keyboard('[enter]')



    n=1
r.close()
