# coding: cp866

from idaapi import 	*
from idc import AddStrucMember

def build_struc(out_dict):
	add_struc(-1,'NVAR_HDR',0)
	nvar_hdr_id = get_struc_id('NVAR_HDR')
	nvar_hdr_size = get_struc_size(nvar_hdr_id)
	nvar_hdr_dict = {'id': nvar_hdr_id, 'size': nvar_hdr_size}
	AddStrucMember(nvar_hdr_id, "Signature",            0,      FF_ASCI | FF_DATA,   0, 4)
	AddStrucMember(nvar_hdr_id, "EntrySize",            0x4,    FF_WORD | FF_DATA,  -1, 2)
	AddStrucMember(nvar_hdr_id, "Reserved",             0x6,    FF_BYTE | FF_DATA,  -1, 3)
	AddStrucMember(nvar_hdr_id, "Attributes",           0x9,    FF_BYTE | FF_DATA,  -1, 1)
	AddStrucMember(nvar_hdr_id, "IndexInGUIDDataBase",  0xA,    FF_BYTE | FF_DATA,  -1, 1)
	out_dict['NVAR_HDR'] = nvar_hdr_dict

	add_struc(-1,'GUID',0)
	guid_id = get_struc_id('GUID')
	guid_size = get_struc_size(guid_id)
	guid_dict = {'id': guid_id, 'size': guid_size}
	AddStrucMember(guid_id,"Data1", 0,      0x20000400, -1, 4)
	AddStrucMember(guid_id,"Data2", 0X4,    0x10000400, -1, 2)
	AddStrucMember(guid_id,"Data3", 0X6,    0x10000400, -1, 2)
	AddStrucMember(guid_id,"Data4", 0X8,    0x000400,   -1, 8)
	out_dict['GUID'] = guid_dict