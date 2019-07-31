import BancoDeDados as bd



banco = bd.Dados('Banco de Dados/DOLFUT_15min--27-03-2018-a-04-06-2019.csv',5)
banco.setNome_Arquivo('Banco de Dados/DOLFUT_15min--27-03-2018-a-04-06-2019.csv')
banco.setNum_candle(5)
banco.nomear_colunas()
banco.elimin_dados()
banco.setBanco()
banco.normalizar()
banco.getBanco().to_csv('Class5c15m.csv')
