# coding: cp866

from idaapi import 	*
from idc import AddStrucMember

def build_struc(out_dict):
	# 1
	add_struc(-1,'PCIDATA',0)
	pcidata_id = get_struc_id('PCIDATA')
	pcidata_size = get_struc_size(pcidata_id)
	pcidata_dict = {'id': pcidata_id, 'size': pcidata_size}
	AddStrucMember(pcidata_id,"TblSignature", 	0,      FF_ASCI|FF_DATA, -1, 8)
	AddStrucMember(pcidata_id,"TblLength", 		0X8,    FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(pcidata_id,"TblChecksum", 	0XC,    FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(pcidata_id,"Reserved", 		0X10,   FF_BYTE|FF_DATA, -1, 3)
	AddStrucMember(pcidata_id,"PciGlobalFlags", 0X13,   FF_QWRD|FF_DATA, -1, 8)
	AddStrucMember(pcidata_id,"PciDevCount", 	0X1B,   FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(pcidata_id,"CspResCount", 	0X1F,   FF_DWRD|FF_DATA, -1, 4)
	out_dict['PCIDATA'] = pcidata_dict
	# 2
	add_struc(-1,'SIODATA',0)
	siodata_id = get_struc_id('SIODATA')
	siodata_size = get_struc_size(siodata_id)
	siodata_dict = {'id': siodata_id, 'size': siodata_size}
	AddStrucMember(siodata_id,"TblSignature", 	 0,      FF_ASCI|FF_DATA, -1, 8)
	AddStrucMember(siodata_id,"TblLength", 		 0X8,    FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(siodata_id,"TblChecksum", 	 0XC,    FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(siodata_id,"Reserved", 		 0X10,   FF_BYTE|FF_DATA, -1, 3)
	AddStrucMember(siodata_id,"GlobalSioFalsgs", 0X13,   FF_QWRD|FF_DATA, -1, 8)
	out_dict['SIODATA'] = siodata_dict
	# 3
	add_struc(-1,'APIDATA',0)
	apidata_id = get_struc_id('APIDATA')
	apidata_size = get_struc_size(apidata_id)
	apidata_dict = {'id': apidata_id, 'size': apidata_size}
	AddStrucMember(apidata_id,"TblSignature", 	 0,      FF_ASCI|FF_DATA, -1, 8)
	AddStrucMember(apidata_id,"TblLength", 		 0X8,    FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(apidata_id,"TblChecksum", 	 0XC,    FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(apidata_id,"Reserved", 		 0X10,   FF_BYTE|FF_DATA, -1, 3)
	AddStrucMember(apidata_id,"IoApicCount", 	 0X13,   FF_DWRD|FF_DATA, -1, 4)
	out_dict['APIDATA'] = apidata_dict