#Projeto 3 Sistemas Operacionais - 04G
#João Victor Ferreira Pimenta - 42005876
#Claudia Fiorentino Andrade - 42005302
#Victor Prado Chaves - 32070772
#Thiago Henrique Quadrado EStacio - 42012740

import threading, time, logging

def cabeca():
  global prodcab, semaforo, cabe
  cabe = True
  cont = 0
  while cont < 10:
    if cabe == True:
      t = "cab", cont
      #semaforo.acquire()
      prodcab.append(t)
      logging.info("Fabricando Cabeca %d", cont)
      semaforo.release()
      time.sleep(2)
      cabe = False
      cont += 1
  logging.info("Cabecas Fabricadas.")
    
def corpo():
  global producorp, semaforo, cor
  cont = 0
  cor = True
  while cont < 10:
    if cor == True:
      #semaforo.acquire()
      t = "corp", cont
      prodcorp.append(t)
      logging.info("Fabricando corpo %d", cont)
      #semaforo.release()
      time.sleep(4)
      cor = False
      cont += 1
  logging.info("Corpos Fabricados.")

def montagem():
  global montador, semaforo
  i = 0
  while i < 10:  
    #if prodcab[-1] == prodcorp[-1]:
    semaforo.acquire()
    montador.append(prodcab[-1] + prodcorp[-1])
    logging.info("Fabrica Robo %d", i)
    logging.info(montador[i])
    semaforo.release()
    time.sleep(3)
    i += 1
  logging.info("Robos Fabricados.")

format = "%(asctime)s-%(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H;%M:%S")
montador = []
prodcab = []
prodcorp = []
semaforo = threading.Lock()
cor = True
t1 = threading.Thread(target=cabeca)
t2 = threading.Thread(target=corpo)
t3 = threading.Thread(target=montagem)
t1.start()
t2.start()
t3.start()