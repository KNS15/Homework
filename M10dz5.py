import multiprocessing
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while data := f.readline():
            all_data.append(data)
            data = f.readline()


if __name__ == '__main__':
    all_files = [f'./file {number}.txt' for number in range(1, 5)]

    MULTIPROCCESSING = True

    if not MULTIPROCCESSING:
        start = datetime.now()
        for file in all_files:
            read_info(file)
        end = datetime.now()
        print(f'{end - start} (линейный)') #0:00:02.964694 (линейный)
    else:
        start = datetime.now()
        with multiprocessing.Pool() as pool:
            pool.map(read_info, all_files)
        end = datetime.now()
        print(f'{end - start} (многопроцессорный)') #0:00:01.099998 (многопроцессорный)


