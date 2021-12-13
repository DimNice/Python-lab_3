import pickle
from tqdm import tqdm


def bubble_sort(s: list) -> list:
    with tqdm(s, desc="Процесс сортировки") as pbar:
        for i in range(len(s)):
            swap = False
            for j in range(len(s) - i - 1):
                if s[j]['age'] > s[j + 1]['age']:
                    s[j], s[j + 1] = s[j + 1], s[j]
                    swap = True
            if not swap:
                pbar.update(len(s) - i)
                break
            pbar.update(1)
    return s


def save_sort(data: list, path: str):
    """
          :param data: Список отсортированных объектов для сохранения.
          :param path: Путь для сохранения списка объектов.
          """
    with open(path, 'wb') as outfile:
        pickle.dump(data, outfile)


def load_sort(path: str) -> list:
    """
            :param path: Путь для загрузки списка объектов.
            :return: Возвращает список объектов, загруженных из pickle-файла.
    """
    with open(path, 'rb') as file:
        data = pickle.load(file)
    return data

