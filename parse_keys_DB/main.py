# coding: cp866

from idaapi import *



def _make_struc():
   	# 1
    add_struc(-1,"_TIME",0)
    id = get_struc_id("_TIME")
    AddStrucMember(id, "Year",	        0,		FF_WORD | FF_DATA,	 0,	2)
    AddStrucMember(id, "Month",	        0X2,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Day",	        0X3,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Hour",	        0X4,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Minute",		0X5,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Second",		0X6,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Pad1",	        0X7,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Nanosecond",	0X8,	FF_DWRD | FF_DATA,	-1,	4)
    AddStrucMember(id, "TimeZone",		0XC,	FF_WORD | FF_DATA,	-1,	2)
    AddStrucMember(id, "Daylight",		0XE,	FF_BYTE | FF_DATA,	-1,	1)
    AddStrucMember(id, "Pad2",	        0XF,	FF_BYTE | FF_DATA,	-1,	1)



    
def _clear_all():
    do_unknown_range(cvar.inf.minEA, cvar.inf.maxEA - cvar.inf.minEA, DOUNK_EXPAND)    
    del_extra_cmt(cvar.inf.minEA, E_PREV)




def main():
    _clear_all()
    _make_struc()
   



main()
