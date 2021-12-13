import argparse
from package.validator import Validator, ReadFile
from package.sorter import save_sort, load_sort, bubble_sort
from tqdm import tqdm

parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='87.txt', type=str)
parser.add_argument('-output_sort', dest="file_output_sort", default='87_output_sort.bin', type=str)
parser.add_argument('-output', dest="file_output", default='87_output.txt', type=str)
args = parser.parse_args()
file = ReadFile(args.file_input)
checkers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_valid_records = 0
valid_for_sort = []
with tqdm(file.data, desc='Прогресс валидации', colour="#FAF0E6") as progressbar:
    for elem in file.data:
        check_element = Validator(elem['email'], elem['height'], elem['inn'], elem['passport_series'], elem['age'],
                                  elem['occupation'], elem['political_views'], elem['worldview'], elem['address'])
        valid_values = check_element.check_all()
        if valid_values == 9:
            valid_for_sort.append(elem)
            number_of_valid_records += 1
        else:
            checkers[valid_values] += 1
        progressbar.update(1)
number_of_invalid_records = checkers[0] + checkers[1] + checkers[2] + checkers[3] + checkers[4] + checkers[5] + \
                            checkers[6] + checkers[
                                7] + checkers[8]
print("Число правильных записей:", number_of_valid_records, )
print("Число неправильных записей:", number_of_invalid_records)
print("Ошибки в почте:", checkers[0])
print("Ошибки в росте:", checkers[1])
print("Ошибки в ИНН:", checkers[2])
print("Ошибки в серии паспорта:", checkers[3])
print("Ошибки в возрасте:", checkers[4])
print("Ошибки в работе:", checkers[5])
print("Ошибки в адресе:", checkers[6])
print("Ошибки в политических взглядах:", checkers[7])
print("Ошибки в взглядах на мир:", checkers[8])
print("Начинается процесс сортировки.")
valid_for_sort = bubble_sort(valid_for_sort)
print("Сортировка завершена.")
print("Начинается процесс записи в pickle-файл.")
save_sort(valid_for_sort, args.file_output_sort)
print("Процесс записи завершен.")
print("Процесс загрузки объектов из pickle-файла.")
sort_data = load_sort(args.file_output_sort)
print("Загрузка объектов завершена.")
print("Процесс записи загруженных объектов в файл формата txt.")
output = open(args.file_output, 'w')
for elem in sort_data:
    output.write("email: " + elem['email'] + "\n" + "height:" + str(elem['height']) + "\n" +
                 "inn: " + elem['inn'] + "\n" + "passport_series:" + str(elem['passport_series']) + "\n" +
                 "age: " + str(elem['age']) + "\n" + "occupation: " + elem['occupation']
                 + "\n" + "political_views: " + elem['political_views']
                 + "\n" + "worldview: " + elem['worldview'] +
                 "\n" + "address: " + elem['address'] + "\n" + "__________________________________________\n")
output.close()
print("Процесс записи завершен.")
