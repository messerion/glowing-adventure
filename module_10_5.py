import time
from multiprocessing import Pool

def read_info(name):
    """Считывает информацию из файла."""
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f"Линейное выполнение заняло: {time.time() - start_time:.6f} секунд")

    
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f"Многопроцессное выполнение заняло: {time.time() - start_time:.6f} секунд")