import os
import time
import multiprocessing


def process_one():
    print("Запущен первый процесс")
    print("ID процесса:", os.getpid())
    time.sleep(2)
    print("Первый процесс закончил работу")


def process_two():
    print("Запущен второй процесс")
    print("ID процесса:", os.getpid())
    time.sleep(2)
    print("Второй процесс закончил работу")


def process_three():
    print("Запущен третий процесс")
    print("ID процесса:", os.getpid())
    time.sleep(2)
    print("Третий процесс закончил работу")


def process_four():
    print("Запущен четвертый процесс")
    print("ID процесса:", os.getpid())
    time.sleep(2)
    print("Четвертый процесс закончил работу")


if __name__ == "__main__":

    process1 = multiprocessing.Process(target=process_one)
    process2 = multiprocessing.Process(target=process_two)
    process3 = multiprocessing.Process(target=process_three)
    process4 = multiprocessing.Process(target=process_four)

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print("\nВсе процессы завершены.")
    print("ID первого процесса:", process1.pid)
    print("ID второго процесса:", process2.pid)
    print("ID третьего процесса:", process3.pid)
    print("ID четвертого процесса:", process4.pid)