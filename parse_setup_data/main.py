# coding: cp866

from idaapi import *
import structures 




def make_SetupIFRDataList(ea):
    pass

def make_SetupPackagePageIdList(ea):
    ExtLinA(ea, 0, '  ')
    set_name(ea, '_SetupPackagePageIdList', 0)
    MakeDword(ea)
    count = get_long(ea)

    index = 0
    for i in range(ea+4, 4*count+ea+4, 4):
        index += 1
        MakeDword(i)
        set_cmt(i, 'offset _SetupPackagePageIdList_%s' % (index-1), 0)
        
        j = get_long(i)
        ExtLinA(ea+j, 0, ' ')
        MakeStruct(ea + j, 'GUID')
        set_name(ea+j, '_SetupPackagePageIdList_%s' % (index-1), 0)
        

def make_SetupPackageGUIDList(ea):
    ExtLinA(ea, 0, '  ')
    set_name(ea, '_SetupPackageGUIDList', 0)
    MakeDword(ea)
    count = get_long(ea)

    index = 0
    for i in range(ea+4, 4*count+ea+4, 4):
        index += 1
        MakeDword(i)
        set_cmt(i, 'offset _SetupPackageGUIDList_%s' % (index-1), 0)

        j = get_long(i)
        ExtLinA(ea+j, 0, ' ')
        MakeStruct(ea + j, 'GUID')
        set_name(ea+j, '_SetupPackageGUIDList_%s' % (index-1), 0)
        make_ascii_string(ea+j+get_struc_size(get_struc_id('GUID')), 0, ASCSTR_UNICODE)


def make_SetupPackageHpkData(ea):
    ExtLinA(ea, 0, '  ')
    set_name(ea, '_SetupPackageHpkData', 0)
    MakeStruct(ea, '_HPK_INFO')


def make_SetupPackageVariableList(ea):
    ExtLinA(ea, 0, '  ')
    set_name(ea, '_SetupPackageVariableList', 0)
    MakeDword(ea)
    count = get_long(ea)

    index = 0
    for i in range(ea+4, 4*count+ea+4, 4):
        index += 1
        MakeDword(i)
        set_cmt(i, 'offset _SetupPackageVariableList_%s' % (index-1), 0)
        
        j = get_long(i)
        ExtLinA(ea+j, 0, ' ')
        MakeStruct(ea + j, 'GUID')
        set_name(ea+j, '_SetupVariableInfo_%s' % (index-1), 0)
        set_name(ea+j, '_SetupGUIDInfo_%s' % (index-1), 0)
        make_ascii_string(ea+j+get_struc_size(get_struc_id('GUID')), 0, ASCSTR_UNICODE)
        
        k = get_long(i+4)
        if k < 4*count+ea+4:
            MakeArray(ea + j + get_struc_size(get_struc_id('GUID')) + get_max_ascii_length(ea + j + get_struc_size(get_struc_id('GUID')), -1), k - j)


def make_SetupControlInfo_N_N(ea):
    set_name(ea, '_SetupControlInfo_N_N', 0)


def make_SetupPackagePageList(ea, ea_CONTROL_INFO):
    ExtLinA(ea, 0, '  ')
    set_name(ea, '_SetupPackagePageList', 0)
    MakeDword(ea)
    count = get_long(ea)
    
    index = 0
    for i in range(ea+4, 4*count+ea+4, 4):
        index += 1
        MakeDword(i)
        set_cmt(i, 'offset _SetupPageInfo_%s' % (index-1), 0)

        j = get_long(i)
        ExtLinA(j, 0, ' ')
        MakeStruct(j, '_PAGE_INFO')
        set_name(j, '_SetupPageInfo_%s' % (index-1), 0)
        m = Dword(j + get_struc_size(get_struc_id("_PAGE_INFO")))
        for n in range(j+get_struc_size(get_struc_id("_PAGE_INFO")), 4*m+j+0x20, 4):
            MakeDword(n)
            offsetVariables = Dword(n)
            MakeStruct(offsetVariables + ea_CONTROL_INFO, '_CONTROL_INFO')
        ExtLinB(j+get_struc_size(get_struc_id("_PAGE_INFO"))+4*m, 0, '_SetupPageInfo_End')
        ExtLinB(j+get_struc_size(get_struc_id("_PAGE_INFO"))+4*m, 1, '')
            

def make_SetupPackageScreen(ea):
    ExtLinA(ea, 0, '  ')
    strid = get_struc_id('_SCREEN_INFO')
    size = get_struc_size(strid)
    doStruct(ea, size, strid)
    set_name(ea, '_SetupPackageScreen', 0)
    

def parse_main_struc(out_dict):
    strid = get_struc_id('_SETUP_PKG')
    size = get_struc_size(strid)
    doStruct(0x00, size, strid)
    set_name(0, 'PackageSignature', 0)
    out_dict['ea_SetupPackageScreen'] = get_long(0x28)
    out_dict['ea_SetupPackagePageList'] = get_long(0x2C)
    out_dict['ea_SetupControlInfo_N_N'] = get_long(0x30)
    out_dict['ea_SetupPackageVariableList'] = get_long(0x34)
    out_dict['ea_SetupPackageHpkData'] = get_long(0x38)
    out_dict['ea_SetupPackageGUIDList'] = get_long(0x3C)
    out_dict['ea_SetupPackagePageIdList'] = get_long(0x40)
    out_dict['ea_SetupIFRDataList'] = get_long(0x44)    

  
def _clear_all():
    do_unknown_range(cvar.inf.minEA, cvar.inf.maxEA - cvar.inf.minEA, DOUNK_EXPAND) 
    del_extra_cmt(cvar.inf.minEA, E_PREV)


   
def main():
    reload(structures)
    _clear_all()

    dict_of_struc = {}
    structures.build_struc(dict_of_struc)
    # print dict_of_struc

    dict_of_ea = {}
    parse_main_struc(dict_of_ea)
    # print dict_of_ea

    make_SetupPackageScreen(dict_of_ea['ea_SetupPackageScreen'])
    make_SetupPackagePageList(dict_of_ea['ea_SetupPackagePageList'], dict_of_ea['ea_SetupControlInfo_N_N'])
    make_SetupControlInfo_N_N(dict_of_ea['ea_SetupControlInfo_N_N'])
    make_SetupPackageVariableList(dict_of_ea['ea_SetupPackageVariableList'])
    make_SetupPackageHpkData(dict_of_ea['ea_SetupPackageHpkData'])
    make_SetupPackageGUIDList(dict_of_ea['ea_SetupPackageGUIDList'])
    make_SetupPackagePageIdList(dict_of_ea['ea_SetupPackagePageIdList'])
    make_SetupIFRDataList(dict_of_ea['ea_SetupIFRDataList'])
    
main()
