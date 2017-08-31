# coding: cp866

from idaapi import *
import os


#  Список для хранения имен, которые уже были использованы.
#  Нужен для того, чтобы избежать повторения имен.
_g_list = []




# принимает строку имени и строку адреса. приминяет имя к указанному адресу
def _make_name(in_name, in_addr):
    global _g_list
    # проверяем, есть ли по указанному адресу имя
    is_name = get_name(0, int(in_addr,16))
    # если имени нет - выходим
    if is_name == None:
        return
    # если входное имя содержит символы '?$' - выходим
    if in_name[0] in '?$':
        return
    # проверяет использовалось ли имя. если нет - добавляет его в 
    # список использованных и создает по указанному адресу. если 
    # использовалось - добавляет в конец пробел и проверяет заново
    if in_name not in _g_list:
        _g_list.append(in_name)
        set_name(int(in_addr,16), in_name, SN_NOCHECK)
    else:
        in_name = in_name + '_'
        _make_name(in_name, in_addr)



# принимает строку, удаляет из ее начала все символы пробела 
# и возвращает строку без пробелов в начале
def skip_space(in_str):
    lenth = len(in_str)
    out_str = ''
    #считывает первое слово (символы до 1го пробела)
    for i in range(0, lenth):
        if in_str[i] != ' ':
            out_str = in_str[i:]
            break
    # возвращает строку без пробелов в начале
    return out_str



# принимает строку, считывает все символы до первого пробела (адрес)
def get_addr(in_addr_str):
    lenth = len(in_addr_str)
    out_str = ''
    # считывет первое слово (символы до 1го пробела)
    for i in range(0, lenth):
        if in_addr_str[i] in ' ':
            out_str = in_addr_str[0:i]
            break
    # возвращает строку, содержащую только адрес
    return out_str


   
# принимает строку, считывает символы до первого пробела (имя)    
def _get_name(in_name_str):
    lenth = len(in_name_str)
    out_str = ''
    #считывет первое слово (символы до 1го пробела)
    for i in range(0, lenth):
        if in_name_str[i] in ' ':
            out_str = in_name_str[0:i]
            break
    # возвращает строку с именем
    return out_str
    
      


# основная функция
def main():
	# путь к '.map' файлу
    path_to_map = r'c:\Work\Temp\HardwareProfile.map'
    # открываем файл на чтение
    file = open(path_to_map)
 	# построчно читаем файл
    for line in file.readlines():
    	# если в строке найдена подстрока '.obj' - обрабатываем строку
        if '.obj' in line:
         	# отбрасываем первые 21 символ (не содержат полезной информации)
            temp_name = line[21:]
            # извлекаем из строки имя
            name = _get_name(temp_name)
            # удаляем пробелы из оставшейся части строки
            temp_addr = skip_space(temp_name[len(name)+1:])
            # извлекаем из строки адрес
            addr = get_addr(temp_addr)
            # пытаемся применить имя к указанному адресу
            _make_name(name, addr)




# точка старта скрипта
main()
