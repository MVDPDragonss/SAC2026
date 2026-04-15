import socket
import struct
import time
import random
import math

# Dati da inviare**************************************************************
#frequenza_cardiaca = 75
#temperatura = 37.0
#press_sistole = 120
#press_diastole = 80
#atti_respiratori = 14
#******************************************************************************



#Generazione dei dati fisiologici simulati*************************************



#Generazione della temperatura corporea


















try:

    # Creiamo il socket
    ip_address='10.13.21.3'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 12345))

    print("Rilevamento della temperatura corporea in corso...")

    cont = random.random()
    # Dati da inviare
    if cont < 0.7:
        temperatura = random.uniform(36, 37.5)
    elif 0.7 < cont < 0.9:
        temperatura = random.uniform(37.6, 42) 
    else:
        temperatura= random.uniform(32, 35.9) 

    time.sleep(1)





    #Generazione della frequenza cardiaca

    print("Rilevamento della frequenza cardiaca in corso...")

    cont = random.random()

    if cont < 0.7:
        frequenza_cardiaca = int(random.uniform(60, 100))
    elif 0.7 < cont < 0.9:
        frequenza_cardiaca = int(random.uniform(101, 150))
    else:
        frequenza_cardiaca = int(random.uniform(30, 59))

    time.sleep(1)




    #Generazione della pressione sanguigna

    print("Rilevamento della pressione sanguigna in corso...")

    cont = random.random()

    if cont < 0.7:
        press_sistole = int(random.uniform(100, 140))
    elif 0.7 < cont < 0.9:
        press_sistole = int(random.uniform(141, 180))
    else:
        press_sistole = int(random.uniform(25, 99))

    press_diastole = press_sistole - 35

    time.sleep(1)





    #Generazione degli atti respiratori

    print("Rilevamento degli atti respiratori in corso...")

    cont = random.random()

    if cont < 0.7:
        atti_respiratori = int(random.uniform(12, 18))
    elif 0.7 < cont < 0.9:
        atti_respiratori = int(random.uniform(19, 25))
    else:
        atti_respiratori = int(random.uniform(6, 11))

    

    print("Frequenza cardiaca ricevuta:", frequenza_cardiaca)
    print("Temperatura corporea ricevuta:", temperatura)
    print("Sistole ricevuta:", press_sistole, " - Diastole ricevuta:", press_diastole)
    print("Atti respiratori ricevuti:", atti_respiratori)

    
    # Prepariamo il pack
    packer = struct.Struct('!IfIII')
    packed_data = packer.pack(frequenza_cardiaca, temperatura, press_sistole, press_diastole, atti_respiratori)

    # Inviamo i dati
    s.sendall(packed_data)



    # Stampa dati



    print("Dati inviati al server.")



    #Ricezione delle valutazioni dei dati analizzati

    # Ricezione delle valutazioni dei dati analizzati
    data = s.recv(1024)  # Ricevi i dati dal server

    # Decodifica e stampa il risultato
    print("\n\nRISULTATI OTTENUTI:\n\n")
    print(data.decode('utf-8'))


    time.sleep(300)
    s.close()

except socket.error as e:
    print(f"Errore nella connessione al server: {e}")
    time.sleep(300)
    exit(1)    