
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from math import *
import time
import sys

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def main():

    print("Inicializando encoder")
    
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # Essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # Lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # O tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Construa com amplitude 1.
    # Some as senoides. A soma será o sinal a ser emitido.
    # Utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # Grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal

    frequencias = {'1': (697, 1209), 
                  '2': (697, 1336), 
                  '3': (697, 1477), 
                  '4': (770, 1209), 
                  '5': (770, 1336), 
                  '6': (770, 1477), 
                  '7': (852, 1209), 
                  '8': (852, 1336),
                  '9': (852, 1477), 
                  '0': (941, 1336)}

    num = input("Digite seu número: ")

    print(f'Gerando Tom referente ao símbolo: {num}')

    fs = 44100
    tempo = 5

    t = np.linspace(0, tempo, fs*tempo, endpoint=False)
    
    s1 = np.sin(2*np.pi*frequencias[num[0]][0]*t)
    s2 = np.sin(2*np.pi*frequencias[num[0]][1]*t)

    s = s1 + s2

    sd.play(s, fs)
    sd.wait()

    plt.plot(t[:1000], s[:1000])
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.show()

    signalMeu().plotFFT(s, fs)

if __name__ == "__main__":
    main()
