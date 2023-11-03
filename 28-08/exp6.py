import threading
import time

shared_resource = 0
lock = threading.Lock()

def increment_resource():
    global shared_resource
    for _ in range(5):
        with lock:
            shared_resource += 1
            print(f'Incremented shared resource: {shared_resource}')
        time.sleep(1)

def decrement_resource():
    global shared_resource
    for _ in range(5):
        with lock:
            shared_resource -= 1
            print(f'Decremented shared resource: {shared_resource}')
        time.sleep(1)


thread1 = threading.Thread(target=increment_resource)
thread2 = threading.Thread(target=decrement_resource)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Resource used properly')