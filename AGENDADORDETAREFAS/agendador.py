import schedule
import time

def tarefa():
    print("Se inscreve no canal, nao da mole!")

schedule.every(5).seconds.do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)
