import threading 
import time
def print_number():
    for i in range(5):
        print(f"Thread{threading.current_thread(). name}:{i}")
        time.sleep(1)

thread1=threading.Thread(target=print_number,name="thread 1")
thread2=threading.Thread(target=print_number,name="Thread 2")

thread1.start()
thread2.start()

# thread1.join()  # it will be excute ordered
# thread2.join()

print("All threads have finished")



