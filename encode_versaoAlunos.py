
#importe as bibliotecas
import suaBibSignal
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

def defineFreqs(numero):
    f1h = 1209
    f2h = 1336
    f3h = 1477
    f4h = 1633

    f1v = 697
    f2v = 770
    f3v = 852
    f4v = 941

    if numero == '1':
        f1 = f1v
        f2 = f1h

    elif numero == '2':
        f1 = f1v
        f2 = f2h
    
    elif numero == '3':
        f1 = f1v
        f2 = f3h

    elif numero == '4':
        f1 = f2v
        f2 = f1h

    elif numero == '5':
        f1 = f2v
        f2 = f2h
    
    elif numero == '6':
        f1 = f2v
        f2 = f3h

    elif numero == '7':
        f1 = f3v
        f2 = f1h

    elif numero == '8':
        f1 = f3v
        f2 = f2h

    elif numero == '9':
        f1 = f3v
        f2 = f3h

    elif numero == '0':
        f1 = f4v
        f2 = f2h

    elif numero == "#":
        f1 = f4v
        f2 = f3h

    elif numero == "*":
        f1 = f4v
        f2 = f1h

    elif numero == "A":
        f1 = f1v
        f2 = f4h

    elif numero == "B":
        f1 = f2v
        f2 = f4h

    elif numero == "C":
        f1 = f3v
        f2 = f4h

    elif numero == "D":
        f1 = f4v
        f2 = f4h
    
    return [f1, f2]


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

    lista_t = np.linspace(0, 1, 44100)
    taxa_amostragem = 44100
    sd.default.samplerate = taxa_amostragem
    numero = input("digite seu numero: ")
    freqs = defineFreqs(numero)
    print(f"Gerando Tom referente ao símbolo: {numero}")


    senoide1 = 1*np.sin(2*pi*freqs[0]*lista_t)
    print(senoide1)

    senoide2 = 1*np.sin(2*pi*freqs[1]*lista_t)
    sinal = senoide1+senoide2
    sinais = suaBibSignal.calcFFT(sinal, taxa_amostragem)

    print("Executando as senoides (emitindo o som)")
    sd.play(sinal)

    plt.figure(1)
    plt.xlabel("tempo")
    plt.ylabel("frequencias")
    plt.plot(lista_t, sinal)

    # plt.figure(2)
    # plt.xlabel("frequencia")
    # plt.ylabel("sinal emitido (transformada de fourier)")
    # plt.plot(senos, sinais)

    plt.show()
    sd.wait()
    signal_handler()

    # plotFFT(signal, fs)
    

if __name__ == "__main__":
    main()
