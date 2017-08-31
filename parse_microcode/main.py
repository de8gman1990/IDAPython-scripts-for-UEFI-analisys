# coding: cp866

from idaapi import *
import structures



dict_of_struct = {}




def make_comm(comm_addr):
    ExtLinA(comm_addr, 0, '')
    set_cmt(comm_addr, 'Версия заголовка\n'
                'Ревизия обновления\n'
                'Дата\n'
                'Идентификатор процессора\n'
                'Контрольная сумма\n'
                'Ревизия загрузчика\n'
                'Флаги процессора\n'
                'Размер данных\n'
                'Общий размер', 
            0)
    ExtLinB(comm_addr, 0, 'Данные микрокода')




def apply_struc(struc_addr, struc_param, index):
    doStruct(struc_addr, struc_param['size'], struc_param['id'])
    make_comm(struc_addr)
    MakeName(struc_addr, 'Microcode_%s' % index)





def make_struc():   
    reload(structures)
    structures.build_struc(dict_of_struct)

    
    

def clear_all():
    do_unknown_range(cvar.inf.minEA, cvar.inf.maxEA - cvar.inf.minEA, DOUNK_EXPAND)    
    for i in range(10):
        del_extra_cmt(cvar.inf.minEA, E_PREV+i)




def main():
    start_file = cvar.inf.minEA 
    end_file = cvar.inf.maxEA

    clear_all()
    make_struc()

    num_microcode = 0
    microcode_sign = '0x5444504dL'
    curr_addr = start_file
    while curr_addr < end_file:

        if hex(Dword(curr_addr)) != microcode_sign:
            num_microcode += 1
            apply_struc(curr_addr, dict_of_struct['_ACPI_TABLE'], num_microcode)
            next_addr = curr_addr + Dword(curr_addr + 0x20)
            curr_addr = next_addr
            
        else:
            ExtLinA(comm_addr, 0, '')
            MakeStr(curr_addr, curr_addr + 4)
            break




main()