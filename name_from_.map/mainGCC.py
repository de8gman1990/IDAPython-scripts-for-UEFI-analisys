# coding: cp866


from idaapi import *
import os



_g_list = []



# принимает строку имени и строку адреса. приминяет имя к указанному адресу
def _make_name(in_name, in_addr):
    

    global _g_list

    if in_name[-1:] == '\n':
        in_name = in_name[:-1]

    print ''
    print in_name
    print in_addr

    # # проверяем, есть ли по указанному адресу имя
    # is_name = get_name(0, int(in_addr,16))
    # # если имени нет - выходим
    # if is_name == None:
    #     return
    # # если входное имя содержит символы '?$' - выходим
    # if in_name[0] in '?$':
    #     return
    # проверяет использовалось ли имя. если нет - добавляет его в 
    # список использованных и создает по указанному адресу. если 
    # использовалось - добавляет в конец пробел и проверяет заново
    if in_name not in _g_list:
        _g_list.append(in_name)
        set_name(int(in_addr,16), in_name, SN_NOCHECK)
    else:
        in_name = in_name + '_'
        _make_name(in_name, in_addr)




def skip_dot(in_str):
    lenth = len(in_str)
    out_str = ''

    for i in range(0, lenth):
        if in_str[i] == '.':
            out_str = in_str[i+1:]
            break

    return out_str




def make_name(_addr, _str):

    _str = skip_dot(_str[2:])

    if len(_str) < 50:
        _make_name(_str, _addr)




def main():
    _path_to_map = r'c:\Work\Temp\HardwareProfile.map'

    file = open(_path_to_map)
    addr = 0
    prev_str = ''

    for line in file.readlines():

        if prev_str != '':
            if '0x0000000000' in line[16:28]:
                if line[16:34] != '0x0000000000000000':
                    addr = line[16:34]
                    if prev_str[:2] == ' .':
                        make_name(addr, prev_str)

        prev_str = line


    
main()