import schedule
import time as tm
from datetime import time
from schedule import repeat, every

@repeat(every().second)
def tarefa():
    print("Se inscreve no canal, nao da mole!")

#schedule.every().hour.at(":03").do(tarefa)
#schedule.every().second.until(time(16, 15, 50)).do(tarefa)

while True:
    schedule.run_pending()
    tm.sleep(1)
