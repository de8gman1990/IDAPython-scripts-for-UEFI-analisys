# coding: cp866

from idaapi import 	*
from idc import AddStrucMember

def build_struc(out_dict):
	# 1
	add_struc(-1,'_ACPI_TABLE',0)
	acpi_table_id = get_struc_id('_ACPI_TABLE')
	acpi_table_size = get_struc_size(acpi_table_id)
	acpi_table_dict = {'id': acpi_table_id, 'size': acpi_table_size}
	AddStrucMember(acpi_table_id, "HeaderVersion",     	0,	    FF_DWRD|FF_DATA,  0, 4)
	AddStrucMember(acpi_table_id, "UpdateRevision",		0X4,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "Date",              	0X8,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "ProcessorId",	    0XC,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "Checksum",	        0X10,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "LoaderRevision",		0X14,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "ProcessorFlags",		0X18,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "DataSize",	        0X1C,	FF_DWRD|FF_DATA, -1, 4)
	AddStrucMember(acpi_table_id, "TotalSize",	        0X20,	FF_DWRD|FF_DATA, -1, 4)
	out_dict['_ACPI_TABLE'] = acpi_table_dict
    # 2
