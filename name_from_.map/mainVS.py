# coding: cp866

from idaapi import *
import os


#  ���᮪ ��� �࠭���� ����, ����� 㦥 �뫨 �ᯮ�짮����.
#  �㦥� ��� ⮣�, �⮡� �������� ����७�� ����.
_g_list = []




# �ਭ����� ��ப� ����� � ��ப� ����. �ਬ���� ��� � 㪠������� �����
def _make_name(in_name, in_addr):
    global _g_list
    # �஢��塞, ���� �� �� 㪠������� ����� ���
    is_name = get_name(0, int(in_addr,16))
    # �᫨ ����� ��� - ��室��
    if is_name == None:
        return
    # �᫨ �室��� ��� ᮤ�ন� ᨬ���� '?$' - ��室��
    if in_name[0] in '?$':
        return
    # �஢���� �ᯮ�짮������ �� ���. �᫨ ��� - �������� ��� � 
    # ᯨ᮪ �ᯮ�짮������ � ᮧ���� �� 㪠������� �����. �᫨ 
    # �ᯮ�짮������ - �������� � ����� �஡�� � �஢���� ������
    if in_name not in _g_list:
        _g_list.append(in_name)
        set_name(int(in_addr,16), in_name, SN_NOCHECK)
    else:
        in_name = in_name + '_'
        _make_name(in_name, in_addr)



# �ਭ����� ��ப�, 㤠��� �� �� ��砫� �� ᨬ���� �஡��� 
# � �����頥� ��ப� ��� �஡���� � ��砫�
def skip_space(in_str):
    lenth = len(in_str)
    out_str = ''
    #���뢠�� ��ࢮ� ᫮�� (ᨬ���� �� 1�� �஡���)
    for i in range(0, lenth):
        if in_str[i] != ' ':
            out_str = in_str[i:]
            break
    # �����頥� ��ப� ��� �஡���� � ��砫�
    return out_str



# �ਭ����� ��ப�, ���뢠�� �� ᨬ���� �� ��ࢮ�� �஡��� (����)
def get_addr(in_addr_str):
    lenth = len(in_addr_str)
    out_str = ''
    # ���뢥� ��ࢮ� ᫮�� (ᨬ���� �� 1�� �஡���)
    for i in range(0, lenth):
        if in_addr_str[i] in ' ':
            out_str = in_addr_str[0:i]
            break
    # �����頥� ��ப�, ᮤ�ঠ��� ⮫쪮 ����
    return out_str


   
# �ਭ����� ��ப�, ���뢠�� ᨬ���� �� ��ࢮ�� �஡��� (���)    
def _get_name(in_name_str):
    lenth = len(in_name_str)
    out_str = ''
    #���뢥� ��ࢮ� ᫮�� (ᨬ���� �� 1�� �஡���)
    for i in range(0, lenth):
        if in_name_str[i] in ' ':
            out_str = in_name_str[0:i]
            break
    # �����頥� ��ப� � ������
    return out_str
    
      


# �᭮���� �㭪��
def main():
	# ���� � '.map' 䠩��
    path_to_map = r'c:\Work\Temp\HardwareProfile.map'
    # ���뢠�� 䠩� �� �⥭��
    file = open(path_to_map)
 	# �����筮 �⠥� 䠩�
    for line in file.readlines():
    	# �᫨ � ��ப� ������� �����ப� '.obj' - ��ࠡ��뢠�� ��ப�
        if '.obj' in line:
         	# ����뢠�� ���� 21 ᨬ��� (�� ᮤ�ঠ� �������� ���ଠ樨)
            temp_name = line[21:]
            # ��������� �� ��ப� ���
            name = _get_name(temp_name)
            # 㤠�塞 �஡��� �� ��⠢襩�� ��� ��ப�
            temp_addr = skip_space(temp_name[len(name)+1:])
            # ��������� �� ��ப� ����
            addr = get_addr(temp_addr)
            # ��⠥��� �ਬ����� ��� � 㪠������� �����
            _make_name(name, addr)




# �窠 ���� �ਯ�
main()
