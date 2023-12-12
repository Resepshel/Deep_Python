# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def href(str_href):
    *_, file = str_href.split('/')
    file_href = str_href[:len(str_href) - len(file)]
    file_name, ext = file.split('.')
    return file_href, file_name, ext


string_href = 'C:/User/My_PC/media/video/film.md'
result = href(string_href)
print(f'Путь до файла: {result[0]}\nНазвание файла: {result[1]}\nРасширение файла: {result[2]}')


