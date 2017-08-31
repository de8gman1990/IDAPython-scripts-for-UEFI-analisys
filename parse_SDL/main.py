# coding: cp866

from idaapi import *
import structures 

dict_of_struc = {}




def make_array(struc_addr, struc_size):
	array_start = struc_addr + struc_size
	array_end = struc_addr + Dword(struc_addr + 0x8)
	array_size = array_end - array_start
	MakeArray(array_start, array_size)


    

def make_const_comm(comm_addr):
    set_cmt(comm_addr,  '\n'
                        '\n'
                        '\n'
                        '\n'
                        '', 
                        1)




def make_struc(struc_addr, struc_param):
    doStruct(struc_addr, struc_param['size'], struc_param['id'])
    # make_const_comm(struc_addr)
    make_array(struc_addr, struc_param['size'])
        



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

    string_list = ('$PCIDATA', '$SIODATA', '$APIDATA')
    
    SIGN_DATA = '0x24'
    curr_addr = start_file
    while curr_addr < end_file:
    	string = GetString(curr_addr, 8, ASCSTR_C)
        if string in string_list:
            make_struc(curr_addr, dict_of_struc[ string[1:] ])
            curr_addr = curr_addr + Dword(curr_addr + 0x8)
        else:
        	curr_addr += 1
        



main()
