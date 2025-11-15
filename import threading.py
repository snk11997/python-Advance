# import threading
# import time

# def print_numbers():
#     for i in range(10):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     for letter in 'abcdefghij':
#         print(letter)
#         time.sleep(1)

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


from multiprocessing import Process
import os

def worker():
    print(f'Worker: {os.getpid()}')

if __name__ == '__main__':
    processes = []
    for _ in range(5):
        p = Process(target=worker)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
