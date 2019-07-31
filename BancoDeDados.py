import pandas
import datetime
class Dados:
    def __init__(self, nome_arquivo, num_candle):
        self.nome_arquivo = nome_arquivo
        self.num_candle = num_candle
        self.banco = pandas.DataFrame

    def setNome_Arquivo(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def setNum_candle(self, num_candle):
        self.num_candle = num_candle

    def getNome_Arquivo(self):
        return self.nome_arquivo

    def getNum_candle(self):
        return self.nome_arquivo

    def getBanco(self):
        return self.banco

    def elimin_dados(self):
        del self.banco['Hora']
        del self.banco['Ativo']
        del self.banco['Volume']
        del self.banco['Quantidade']

    def nomear_colunas(self):
        self.banco = pandas.read_csv(self.nome_arquivo, encoding="ISO-8859-1", delimiter=';')
        self.banco = self.banco.iloc[::-1]
        linha = self.banco.columns
        self.banco.columns = ['Ativo', 'Data', 'Hora', 'Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Volume','Quantidade']
        self.banco.loc[-1] = linha
        self.banco.index = self.banco.index + 1
        self.banco = self.banco.reset_index()
        del self.banco['index']
        self.banco = self.banco.sort_index()
        self.banco['Data'] = pandas.to_datetime(self.banco['Data'],dayfirst=True)
        self.str_to_num()
        print(self.banco)
        return self.banco

    def str_to_num(self):
        self.banco['Abertura'] = self.banco['Abertura'].apply(lambda x: x.replace(',', '.'))
        self.banco['Abertura'] = pandas.to_numeric(self.banco['Abertura'], downcast='float')
        self.banco['Maximo'] = self.banco['Maximo'].apply(lambda x: x.replace(',', '.'))
        self.banco['Maximo'] = pandas.to_numeric(self.banco['Maximo'], downcast='float')
        self.banco['Minimo'] = self.banco['Minimo'].apply(lambda x: x.replace(',', '.'))
        self.banco['Minimo'] = pandas.to_numeric(self.banco['Minimo'], downcast='float')
        self.banco['Fechamento'] = self.banco['Fechamento'].apply(lambda x: x.replace(',', '.'))
        self.banco['Fechamento'] = pandas.to_numeric(self.banco['Fechamento'], downcast='float')

    def normalizar(self):
        print(self.banco)
        linha = self.banco.shape[0]
        coluna = self.banco.shape[1]
        print(linha)
        print(coluna)
        for i in range(0,linha):
            abrtCandle = self.banco.iloc[i,0]
            print(i)
            for j in range(0,coluna):
                self.banco.iloc[i,j]= (self.banco.iloc[i,j] - abrtCandle) * 2
            diferenca = self.banco.iloc[i,-1] - self.banco.iloc[i,-5]
            if diferenca > 0 :
                self.banco.iloc[i,-1] = 1
            elif diferenca < 0:
                self.banco.iloc[i,-1] = -1
            else:
                self.banco.iloc[i, -1] = 0


    def setBanco(self):
        print(self.banco)
        backup = self.banco
        inicio = self.banco['Data'][0]
        fim = self.banco.iloc[-1]['Data']
        atual = inicio
        banco = 0
        while atual <= fim :
            dados = backup.loc[backup['Data'] == atual]
            if len(dados.index) > 0:
                for i in range(0, self.num_candle):
                    aux = dados[i:len(dados.index) - self.num_candle + i + 1]
                    aux = aux.reset_index(drop=True)
                    aux = aux.drop(aux.columns[[0]],axis=1)
                    if i == 0:
                        banco = aux
                    else:
                        banco = pandas.concat([banco, aux], axis=1)
                if atual == inicio:
                    self.banco = banco
                else:
                    self.banco = pandas.concat([self.banco,banco])
            atual = atual + datetime.timedelta(days=1)
        self.banco = self.banco.reset_index(drop=True)
        print(self.banco)


