import socket, sys, re , pickle
filename = "GB3c1m.sav" # nome da IA salva
previsor = pickle.load(open(filename, 'rb'))
resposta = 0

def createServer(HOST, PORT):
    ''' Criar servidor '''

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('Socket created')
    except:
        print('Failed to create socket.')
        sys.exit()

    try:
        s.bind((HOST, PORT))
        print('Socket bind complete')
    except:
        print('Bind failed')
        sys.exit()

    return s

def runServer(s):
    ''' Manter servidor recebendo mensagens '''

    while True:

        try:
            d = s.recvfrom(1024)
            data = d[0].decode('utf-8')
            addr = d[1]
        except:
            continue
        data = re.findall("\d+\.*\d*", data)
        data = [float(i) for i in data]


        print("Dados recebidos: ", data)
        abrtCandle = data[0]
        for i in range(0,len(data)):
            data[i] = (data[i] - abrtCandle) * 2
            print(i)
        print(data)
        y_pred = previsor.predict([data])
        print(y_pred)
        y_pred = y_pred - data[-1]
        print(y_pred)
        if y_pred >= 0.1:
            resposta = "1"
        elif y_pred <= -0.1:
            resposta = "-1"
        else:
            resposta = "0"

        try:
            s.sendto(resposta.encode('utf-8'), addr)
        except:
            continue

    s.close()

if __name__ == "__main__":

    HOST = ''    # Host
    PORT = 8888  # Porta

    s = createServer(HOST, PORT)
    runServer(s)