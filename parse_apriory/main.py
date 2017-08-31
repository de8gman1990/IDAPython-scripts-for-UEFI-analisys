# coding: cp866

from idaapi import *
import structures



dict_of_struct = {}




def apply_struc(struc_addr, struc_param):
    doStruct(struc_addr, struc_param['size'], struc_param['id'])
    



def make_struc():
    reload(structures)
    structures.build_struc(dict_of_struct)




def clear_all():
    do_unknown_range(cvar.inf.minEA, cvar.inf.maxEA - cvar.inf.minEA, DOUNK_EXPAND)    
    for i in range(10):
    	del_extra_cmt(cvar.inf.minEA, E_PREV + i)
   



def main():
    start_file = cvar.inf.minEA 
    end_file = cvar.inf.maxEA

    clear_all()
    make_struc()

    curr_addr = start_file
    while curr_addr < end_file:
        apply_struc(curr_addr, dict_of_struct['GUID'])
        curr_addr += dict_of_struct['GUID']['size']
    



main()
