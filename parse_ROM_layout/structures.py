# coding: cp866

from idaapi import 	*
from idc import AddStrucMember

def build_struc(out_dict):
	add_struc(-1,'GUID',0)
	guid_id = get_struc_id('GUID')
	guid_size = get_struc_size(guid_id)
	guid_dict = {'id': guid_id, 'size': guid_size}
	AddStrucMember(guid_id,"Data1", 0,      FF_DATA|FF_DWRD, -1, 4)
	AddStrucMember(guid_id,"Data2", 0X4,    FF_DATA|FF_WORD, -1, 2)
	AddStrucMember(guid_id,"Data3", 0X6,    FF_DATA|FF_WORD, -1, 2)
	AddStrucMember(guid_id,"Data4", 0X8,    FF_DATA|FF_BYTE, -1, 8)
	out_dict['GUID'] = guid_dict
