from client import Client
import time
from threading import Thread

c1 = Client("hasnae")

c2 = Client("khalid")

c1.send_message("hello !")
time.sleep(1)
c2.send_message("Hello!")
time.sleep(1)
c1.send_message("What's up ?")
time.sleep(1)
c2.send_message("Noting much")
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()

def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False
                break

Thread(target=update_messages).start()
