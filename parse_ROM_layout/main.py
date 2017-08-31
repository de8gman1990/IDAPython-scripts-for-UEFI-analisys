# -*- coding: cp866 -*-

from idaapi import *


def _apply_struc():
    _section_size = cvar.inf.maxEA - cvar.inf.minEA
    strid_HEADER = get_struc_id('AMI_ROM_LAYOUT_HEADER')
    size_HEADER = get_struc_size(strid_HEADER)
    strid_AREA = get_struc_id('AMI_ROM_AREA')
    size_AREA = get_struc_size(strid_AREA)
    _num_member = (_section_size - size_HEADER)/ size_AREA
    
    doStruct(0x00, size_HEADER, strid_HEADER)
    ea = cvar.inf.minEA + size_HEADER 
    for i in range(0,_num_member):
        ExtLinA(ea, 0, '')
        doStruct(ea, size_AREA, strid_AREA)
        ea += size_AREA    


def _create_struc():
    add_struc(-1,"AMI_ROM_LAYOUT_HEADER",0)
    id = get_struc_id("AMI_ROM_LAYOUT_HEADER")
    AddStrucMember(id, "Signature",	        0,	FF_ASCI | FF_DATA,	 0,	4)
    AddStrucMember(id, "Version",	        0x4,	FF_DWRD | FF_DATA,	-1,	4)
    AddStrucMember(id, "DescriptorSize",	0x8,	FF_DWRD | FF_DATA,	-1,	4)
    AddStrucMember(id, "NumberOfDescriptors",	0xC,	FF_DWRD | FF_DATA,	-1,	4)
    
    add_struc(-1,"GUID",0)
    id = get_struc_id("GUID")
    AddStrucMember(id,"Data1",	0,	FF_DWRD | FF_DATA,	-1,	4)
    AddStrucMember(id,"Data2",	0X4,	FF_WORD | FF_DATA,	-1,	2)
    AddStrucMember(id,"Data3",	0X6,	FF_WORD | FF_DATA,	-1,	2)
    AddStrucMember(id,"Data4",	0X8,	FF_DATA,	        -1,	8)

    add_struc(-1,"AMI_ROM_AREA",0)
    id = get_struc_id("AMI_ROM_AREA")
    AddStrucMember(id,"Guid",	    0,      FF_STRU | FF_DATA,	GetStrucIdByName("GUID"),	16)
    AddStrucMember(id,"Address",    0X10,    FF_QWRD | FF_DATA,	-1,	                        8)
    AddStrucMember(id,"Offset",	    0X18,    FF_DWRD | FF_DATA,	-1,	                        4)
    AddStrucMember(id,"Size",	    0X1C,    FF_DWRD | FF_DATA,	-1,	                        4)
    AddStrucMember(id,"Type",	    0X20,    FF_DWRD | FF_DATA,	-1,	                        4)
    AddStrucMember(id,"Attributes", 0X24,    FF_DWRD | FF_DATA,	-1,	                        4)

    add_struc(-1,"ROM_AREA",0)
    id = get_struc_id("ROM_AREA")
    AddStrucMember(id,"Address",    0X00,    FF_QWRD | FF_DATA, -1,                         8)
    AddStrucMember(id,"Offset",     0X08,    FF_DWRD | FF_DATA, -1,                         4)
    AddStrucMember(id,"Size",       0X0C,    FF_DWRD | FF_DATA, -1,                         4)
    AddStrucMember(id,"Type",       0X10,    FF_DWRD | FF_DATA, -1,                         4)
    AddStrucMember(id,"Attributes", 0X14,    FF_DWRD | FF_DATA, -1,                         4)
    

    
def _clear_file():
    do_unknown_range(cvar.inf.minEA, cvar.inf.maxEA - cvar.inf.minEA, DOUNK_EXPAND)    
    del_extra_cmt(cvar.inf.minEA, E_PREV)


def main():
    _clear_file()
    _create_struc()
    _apply_struc()

# первый коммент на русском   
main()
