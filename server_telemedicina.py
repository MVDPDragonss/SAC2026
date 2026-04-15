import socket
import struct
import time





try:


    #Connessione con il client paziente
    ip_address='0.0.0.0'
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_address, 12345))
    server.listen(1)
    print("In attesa...")

    conn, addr = server.accept()
    print("Connessione da", addr)








    # Ricevi esattamente 20 byte
    data = b''
    while len(data) < 20:
        packet = conn.recv(20 - len(data))
        if not packet:
            break
        data += packet





    # Disimpacchettiamo
    unpacker = struct.Struct('!IfIII')
    frequenza_cardiaca, temperatura, press_sistole, press_diastole, atti_respiratori = unpacker.unpack(data)

    print("Frequenza cardiaca ricevuta:", frequenza_cardiaca)
    print("Temperatura corporea ricevuta:", temperatura)
    print("Sistole ricevuta:", press_sistole, " - Diastole ricevuta:", press_diastole)
    print("Atti respiratori ricevuti:", atti_respiratori)






    # Controlli sui parametri ricevuti dal client




    # Controlli relativi alla frequenza cardiaca

    # Controllo relativo al battito cardiaco************************************************************************

    if frequenza_cardiaca < 60:# Frequenza cardiaca bassa
        val_freq="Bradicardia"                                   # Valutazione della frequenza cardiaca

    elif frequenza_cardiaca > 100:# Frequenza cardiaca alta
        val_freq="Tachicardia"                                   # Valutazione della frequenza cardiaca

    else:# Frequenza cardiaca regolare
        val_freq="Frequenza cardiaca regolare"                   # Valutazione della frequenza cardiaca




    # Controllo relativo alla temperatura corporea******************************************************************

    if temperatura > 39:                                         # Valutazione della temperatura corporea
        val_temp="Febbre molto alta"

    elif temperatura > 37.5:                                     # Valutazione della temperatura corporea
        val_temp="Febbre moderata"

    else:                                                        # Valutazione della temperatura corporea
        val_temp="Temperatura corporea regolare"            





    # Controllo relativo alla pressione sanguigna*******************************************************************

    # Controllo la sistole


    if press_sistole > 140:
        val_press="Pressione sanguigna alta"                     # Valutazione della pressione sanguigna

    elif press_sistole < 90:
        val_press="Pressione sanguigna bassa"                    # Valutazione della pressione sanguigna

    else:
        val_press="Pressione sanguigna regolare"                 # Valutazione della pressione sanguigna





    # Controllo relativo agli atti respiratori**********************************************************************

    if atti_respiratori < 12:
        val_resp="Bradipnea"                                     # Valutazione degli atti respiratori

    elif atti_respiratori > 20:
        val_resp="Tachipnea"                                     # Valutazione degli atti respiratori

    else:
        val_resp="Atti respiratori regolari"                     # Valutazione degli atti respiratori




    # Stampa delle valutazioni relative ai dati ricevuti dal paziente***********************************************

    print("\n\nValutazione frequenza cardiaca: ",val_freq)

    print("Valutazione temperatura corporea: ",val_temp)

    print("Valutazione pressione sanguigna: ",val_press)

    print("Valutazione atti respiratori: ",val_resp)




    # Invio delle valutazioni al client paziente


    conn.sendall(f"Valutazione frequenza cardiaca: {val_freq} \nValutazione temperatura corporea: {val_temp} \nValutazione pressione sanguigna: {val_press} \nValutazione atti respiratori: {val_resp}".encode('utf-8'))








    time.sleep(300)
    conn.close()

except socket.error as e:
    print(f"Errore nella connessione al server: {e}")
    time.sleep(300)
    exit(1)    