# coding: cp866

from idaapi import *
import structures 

dict_of_struc = {}

def make_ins_cmt(addres, position, content):
    num_line = 0
    start_line = 0
    end_line = 0

    for i in range(len(content)):
        if content[i] == '\n':
            end_line = i
            if position == 'Before':
                ExtLinA(addres, num_line, content[start_line:end_line])
            elif position == 'After':
                ExtLinB(addres, num_line, content[start_line:end_line])

            start_line = end_line + 1
            num_line += 1

        elif i == len(content) - 1:
            if position == 'Before':
                ExtLinA(addres, num_line, content[start_line:])
            elif position == 'After':
                ExtLinB(addres, num_line, content[start_line:])



def make_array(struc_addr, ascii_dict):
    if 'Defaults' not in ascii_dict['content']:
        array_end = struc_addr + Word(struc_addr + 4)
        array_size = array_end - ascii_dict['end']
        MakeArray(ascii_dict['end'], array_size)
        ExtLinB(ascii_dict['end'], 0, '\n')

    elif 'Defaults' in ascii_dict['content']:
        ExtLinB(struc_addr + 0x16, 0, '\n')
        guid_tail = struc_addr + Word(struc_addr + 0x4)
        print hex(guid_tail)
        make_ins_cmt(guid_tail - 16, 'After', '\n\n\n\n')

        for i in range(160):
            guid_head = guid_tail - 16

            if hex(Dword(guid_head)) != '0xffffffffL':
                make_struc(guid_head, dict_of_struc['GUID'])
                make_ins_cmt(guid_head, 'Before', '\nГуид с индексом %s' % i)
            else:
                make_ins_cmt(guid_tail, 'Before', '\nСписок гуидов переменных\n\nГуид с индексом %s' % i)
                break

            guid_tail = guid_head



def make_ascii_string(struc_head, ascii_dict):
    nvar_hdr_id = get_struc_id("NVAR_HDR")
    nvar_hdr_size = get_struc_size(nvar_hdr_id)
    ascii_start = struc_head + nvar_hdr_size
    ascii_end = None
    
    for i in range(ascii_start, ascii_start + 50):
        if hex(Byte(i)) > '0x80' or hex(Byte(i)) < '0x30':
            ascii_end = i
            break
    if ascii_end != None:
        MakeStr(ascii_start, ascii_end)
    
    ascii_dict['content'] = GetString(ascii_start)
    ascii_dict['end'] = ascii_end
    


def make_const_comm(comm_addr):
    set_cmt(comm_addr,  'Сигнатура\n'
                        'Размер записи\n'
                        'Зарезервировано\n'
                        'Атрибуты\n'
                        'Индекс в списке GUID\'ов переменных', 
                        1)



def make_struc(struc_addr, struc_param):
    doStruct(struc_addr, struc_param['size'], struc_param['id'])
    if struc_param['id'] == get_struc_id('NVAR_HDR'):
        make_const_comm(struc_addr)
        ascii_dict = {}
        make_ascii_string(struc_addr, ascii_dict)
        make_array(struc_addr, ascii_dict)
        


def clear_file(in_start, in_end):
    do_unknown_range(in_start, in_end - in_start, DOUNK_EXPAND) 
    for num_line in range(0,30):
        del_extra_cmt(in_start, E_PREV + num_line)



# ======================================================================
def main():
    reload(structures)
    
    structures.build_struc(dict_of_struc)

    start_file = cvar.inf.minEA 
    end_file = cvar.inf.maxEA 
    clear_file(start_file, end_file)
    
    SIGN_NVAR = '0x5241564eL'
    curr_addr = start_file

    while curr_addr < end_file:
        if hex(Dword(curr_addr)) == SIGN_NVAR:
            make_struc(curr_addr, dict_of_struc['NVAR_HDR'])

        curr_addr += 1

    make_ins_cmt(end_file - 16, 'Before', '\nGUID текущего файла')
    make_struc(end_file - 16, dict_of_struc['GUID'])



main()
