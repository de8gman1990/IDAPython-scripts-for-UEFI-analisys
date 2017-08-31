# coding: cp866

from idaapi import *

def _make_comm():
    ea = cvar.inf.minEA 
    set_cmt(ea, 'Сигнатура\nРазмер таблицы (включая заголовок)\nРевизия таблицы\nЗначение контрольной суммы\nOEM идентификатор\nИдентификатор производителя\nOEM ревизия основной таблицы (DSDT)\nИдентификатор ASL компилятора\nРевизия компилятора ASL', 0)

    strid = get_struc_id('_ACPI_TABLE')
    size = get_struc_size(strid)
    ExtLinA(ea + size, 0, '\n')

def _make_struc():
   
    add_struc(-1,"_ACPI_TABLE",0)
    id = get_struc_id("_ACPI_TABLE")
    AddStrucMember(id, "Signature",	            0,	    0x50000400,	         0,	4)
    AddStrucMember(id, "Length",	            0X4,	0x20000400,	        -1,	4)
    AddStrucMember(id, "Revision",	            0X8,	0x000400,	        -1,	1)
    AddStrucMember(id, "Checksum",	            0X9,	0x000400,	        -1,	1)
    AddStrucMember(id, "OEMID",	                0XA,	0x50000400,	        -1,	6)
    AddStrucMember(id, "OEM_Table_ID",	        0X10,	0x50000400,	        -1,	8)
    AddStrucMember(id, "OEM_Revision",	        0X18,	0x20000400,	        -1,	4)
    AddStrucMember(id, "Creator_ID",	        0X1C,	0x50000400,	        -1,	4)
    AddStrucMember(id, "Creator_Revision",	    0X20,	0x20000400,	        -1,	4)

    ea = cvar.inf.minEA 
    strid = get_struc_id('_ACPI_TABLE')
    size = get_struc_size(strid)
    doStruct(0x00, size, strid)
    do_data_ex(cvar.inf.minEA + size, FF_BYTE, cvar.inf.maxEA - size, strid)

    
    

def _clear_all():
    do_unknown_range(cvar.inf.minEA, cvar.inf.maxEA - cvar.inf.minEA, DOUNK_EXPAND)    
    del_extra_cmt(cvar.inf.minEA, E_PREV)


def main():
    _clear_all()
    _make_struc()
    _make_comm()
    

main()
