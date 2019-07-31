import pickle
import pandas
import BancoDeDados as bd
entrada = {}
negoci = 0
filename = "GB3c1m.sav" # nome da IA salva
numCandle = 3
candleFilename = "Banco de Dados/DOLFUT_1min-06-10-2016-a-09-02-2018.csv" # Nome do arquivo em que se encontra os candles
candles = bd.Dados(candleFilename,1)
candles.nomear_colunas()
previsor = pickle.load(open(filename, 'rb'))
dias = 5
#teste = [[0,2,-2,2,3,4,-1,1]]
#y_pred = previsor.predict(teste)
#print(y_pred)
inicio = negoci['Data'][0]
atual = inicio
#Começa no primeiro dia e vai até a quantidade de dias predeterminada
for i in range(0, dias):
    auxNegoci = negoci.loc[negoci['Data'] == atual]
    auxCandle = candles.getBanco().loc[candles.getBanco()['Data'] == atual]
    for j in auxCandle:
        for k in auxNegoci:
            if j.Hora < k.Hora:
                if entrada.len()== (numCandle - 1) * 4:
                    entrada = entrada[5:]
                entrada = entrada.append(j.abertura, j.min, j.max, j.fechamento)



