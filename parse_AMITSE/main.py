# coding: cp866

from idaapi import *
import structures



dict_of_struct = {}




def make_struc():
    reload(structures)
    structures.build_struc(dict_of_struct)

    
    

def main():
    start_file = cvar.inf.minEA
    end_file = GetEntryOrdinal(0)
    methods_list = ('gEdit',          'gPopupEdit',   'gPopupString',
                  'gDate',          'gUefiAction',  'gPopupSel',
                  'gPopupPassword', 'gText',        'gNumeric',
                  'gTime',          'gSubMenu',     'gMenu',
                  'gLabel',         'gResetButton', 'gOrdListBox',
                  'gControl',       'gPopup',       'gHotKey',
                  'gObject',        'gMemo',        'gMsgBox',
                  'gAction',        'gApplication', 'gFrame',
                  'gListBox',       'gPage',        'gHotClick')

    make_struc()

    curr_addr = start_file
    while curr_addr < end_file:
        curr_name = Name(curr_addr)
        
        if curr_name in methods_list:
            doStruct(curr_addr, dict_of_struct[curr_name][0], dict_of_struct[curr_name][1])
            set_cmt(curr_addr, dict_of_struct[curr_name][2], 0)
            print curr_name

        curr_addr += 1


  
main()
