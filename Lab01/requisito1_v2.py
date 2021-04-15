import re  # bib para usar regex
import numpy as np

j_dict = {
    "j": "000010",
    "jal": "000011",
    "jr": "000000",
    "jalr": "000000",
}
r_dict = {
    "add": "000000",
    "addu": "000000",
    "sub": "000000",
    "subu": "000000",
    "and": "000000",
    "or": "000000",
    "xor": "000000",
    "nor": "000000",
    "sll": "000000",
    "srl": "000000",
    "sra": "000000",
    "sllv": "000000",
    "srlv": "000000",
    "srav": "000000",
    "slt": "000000",
    "sltu": "000000",
    "clo": "011100",
    "clz": "011100",
    "mult": "000000",
    "div": "000000",
    "mfhi": "000000",
    "mflo": "000000",
    "msubu": "011100",
    "madd": "011100",
    "mul": "011100",
    "movn": "000000",
    "teq": "000000",
}
i_dict = {
    "addi": "001000",
    "addiu": "001001",
    "andi": "001100",
    "ori": "001101",
    "xori": "001110",
    "slti": "001010",
    "sltiu": "001011",
    "lb": "100000",
    "lbu": "100100",
    "lh": "100001",
    "lhu": "100101",
    "lw": "100011",
    "lui": "001111",
    "sb": "101000",
    "sh": "101001",
    "sw": "101011",
    "beq": "000100",
    "bne": "000101",
    "bltz": "000001",
    "bgez": "000001",
    "bltzal": "000001",
    "bgezal": "000001",
    "blez": "000110",
    "bgtz": "000111",
}
m_dict = {}

funct_dict = {
    "add": "100000",
    "addu": "100001",
    "sub": "100010",
    "subu": "100011",
    "and": "100100",
    "or": "100101",
    "xor": "100110",
    "nor": "100111",
    "sll": "000000",
    "srl": "000010",
    "sra": "000011",
    "sllv": "000100",
    "srlv": "000110",
    "srav": "000111",
    "slt": "101010",
    "sltu": "101011",
    "clo": "100001",
    "clz": "100000",
    "mult": "011000",
    "msubu": "000101",
    "div": "011010",
    "mfhi": "010000",
    "mflo": "010010",
    "madd": "000000",
    "mul": "000010",
    "movn": "001011",
    "teq": "110100",
}


def is_number(num):
    """Tests to see if arg is number. """
    try:
        # Try to convert the input.
        float(num)
        # If successful, returns true.
        return True
    except:
        # Silently ignores any exception.
        pass

    # If this point was reached, the input is not a number and the function
    # will return False.
    return False



def number_reg(mask):
    if mask == "$0" or mask == "$zero":
        return 0
    if mask == "$1" or mask == "$at":
        return 1
    if mask == "$2" or mask == "$v0":
        return 2
    if mask == "$3" or mask == "$v1":
        return 3
    if mask == "$4" or mask == "$a0":
        return 4
    if mask == "$5" or mask == "$a1":
        return 5
    if mask == "$6" or mask == "$a2":
        return 6
    if mask == "$7" or mask == "$a3":
        return 7
    if mask == "$8" or mask == "$t0":
        return 8
    if mask == "$9" or mask == "$t1":
        return 9
    if mask == "$10" or mask == "$t2":
        return 10
    if mask == "$11" or mask == "$t3":
        return 11
    if mask == "$12" or mask == "$t4":
        return 12
    if mask == "$13" or mask == "$t5":
        return 13
    if mask == "$14" or mask == "$t6":
        return 14
    if mask == "$15" or mask == "$t7":
        return 15
    if mask == "$16" or mask == "$s0":
        return 16
    if mask == "$17" or mask == "$s1":
        return 17
    if mask == "$18" or mask == "$s2":
        return 18
    if mask == "$19" or mask == "$s3":
        return 19
    if mask == "$20" or mask == "$s4":
        return 20
    if mask == "$21" or mask == "$s5":
        return 21
    if mask == "$22" or mask == "$s6":
        return 22
    if mask == "$23" or mask == "$s7":
        return 23
    if mask == "$24" or mask == "$t8":
        return 24
    if mask == "$25" or mask == "$t9":
        return 25
    if mask == "$26" or mask == "$k0":
        return 26
    if mask == "$27" or mask == "$k1":
        return 27
    if mask == "$28" or mask == "$gp":
        return 28
    if mask == "$29" or mask == "$sp":
        return 29
    if mask == "$30" or mask == "$fp":
        return 30
    if mask == "$31" or mask == "$ra":
        return 31

import sys
# Leitura do arquivo de entrada .asm
if(len(sys.argv) == 1):
    print("Favor inserir o arquivo a ser aberto como argumento.")
    sys.exit(1)

entrada = open(sys.argv[1], "r")

# Confere se arquivo foi aberto e começa o processo
if entrada.mode == "r":
    contents = entrada.readlines()  # le linha a linha
    address_text = 0  # endereço (int)
    address_data = 0  # endereço (int)
    reg = re.compile("\w+:", flags=re.M)  
    segD = re.compile(".data", flags=re.M)
    segT = re.compile(".text", flags=re.M)
    labelDict = {} 
    instructionsDict = {}
    seg_Data = True
    for i in contents:
        i = i.replace("\n", "")
        print(i) 
        matched = reg.match(i)

        if (matched):  
            
            label = matched.group()
            label = re.sub(":", "", label)
            
            if()
            labelDict[label] = address
        else: 
            instructionsDict[address] = i
        
        

print(labelDict)

#leitura do .data
entrada2 = open(sys.argv[1],'r')

saida_data = []
if(entrada2.mode == 'r'):
    conteudo = entrada2.readlines()
    add = 0
    for i in conteudo:
        if( i == '.text\n'):
            break
        else:
            sl = i.rstrip('\n').lstrip().split(' ')
            for item in sl[1:]:
                if(('.word' in sl) and item != '.word'):
                    item = item.split(',')
                    for c in item:
                    	if(c!=''):
                    		saida_data.append(c)
                if(('.byte' in sl) and item != '.byte'):
                    item = item.split(',')
                    for c in item:
                        for d in c:
                            if(d!="'"):
                                saida_data.append(ord(d))
                
addres_data = []
index = 0
for add in saida_data:
    addres_data.append(np.base_repr(index,base=16).rjust(8,'0'))
    saida_data[index] = np.base_repr(int(add), base = 16).rjust(8,'0')
    index += 1

saidaData = open("saida_data.mif",'w')
header = ['DEPTH = 16384;\n',
         'WIDTH = 32;\n',
         'ADDRESS_RADIX = HEX;\n',
         'DATA_RADIX = HEX;\n',
         'CONTENT\n',
         'BEGIN\n\n']

saidaData.writelines(header)

#escrever em .data
for value,add in zip(saida_data,addres_data):
    s = add + ' : ' + value + '\n'
    saidaData.writelines(s)

saidaData.writelines('\nEND')
saidaData.close() 

list_isntructions = []
address2 = 0

for instruc in instructionsDict.values():
    if(instruc.find('#')!=-1):
        instruc = instruc[0:instruc.find('#')]
    address2 += 1
    infos = {"address": address2, "instruction": instruc}
    if ((".data" not in instruc) and (".text" not in instruc)) and instruc != "":
        reg = re.compile('\w+ ')
        mat = reg.match(instruc)

        if(mat):
            l = mat.group()
            if(l == 'li '):
                sl1 = instruc.split(',')[0].strip().split(' ')[1]
                sl2 = instruc.split(',')[1].strip()
                
                if('x' in sl2):
                    sl2 = np.base_repr(int(sl2, 16), base=16).rjust(8,'0')
                else:
                    sl2 = sl2.rjust(8, '0')     

                infos["instruction"] = "lui " + sl1 + "," + '0x' +  sl2[0:4]
                list_isntructions.append(infos)
                
                infos = infos.copy()
                address2 += 1
                infos["address"] = address2
                infos["instruction"] = "ori " + sl1 + "," + sl1 + "," + '0x' + sl2[4:8]
                

        list_isntructions.append(infos)


# Verificando o type da instruções:
list_isntructions_types = []
for info in list_isntructions:
    typee = ""

    address = info["address"]
    instruction = info["instruction"]

    splitt = instruction.split()

    if splitt[0] in r_dict:
        typee = "R-TYPE"
    elif splitt[0] in i_dict:
        typee = "I-TYPE"
    elif splitt[0] in j_dict:
        typee = "J-TYPE"
    else:
        typee = "UNDEFINED TYPE"

    infos = {"address": address, "instruction": instruction, "type": typee}

    list_isntructions_types.append(infos)

def format_r(iten):
    iten_instruc = iten["instruction"]
    remove_comma = iten_instruc.replace(",", " ")
    spli = remove_comma.split()
    op_name = spli[0]
    if len(spli) == 4:
        op = r_dict[op_name]
        rs = spli[2]
        rt = spli[3]
        rd = spli[1]

        if spli[0] == "sll" or spli[0] == "srl" or spli[0] == "sra":
            shamt = spli[3]
        else:
            shamt = "00000"

        funct = funct_dict[op_name]

        iten["op"] = op
        iten["rs"] = rs
        iten["rt"] = rt
        iten["rd"] = rd
        iten["shamt"] = shamt
        iten["funct"] = funct

    elif len(spli) == 3:
        if (
            op_name == "mult"
            or op_name == "div"
            or op_name == "madd"
            or op_name == "msubu"
            or op_name == "teq"
        ):
            op = r_dict[op_name]
            rs = spli[1]
            rt = spli[2]
            rd_shamt = "0000000000"
            funct = funct_dict[op_name]

            iten["op"] = op
            iten["rs"] = rs
            iten["rt"] = rt
            iten["rd_shamt"] = rd_shamt
            iten["funct"] = funct
        elif op_name == "clo":
            op = r_dict[op_name]
            rs = spli[2]
            rt = "00000"
            rd = spli[1]
            shamt = "00000"
            funct = funct_dict[op_name]

            iten["op"] = op
            iten["rs"] = rs
            iten["rt"] = rt
            iten["rd"] = rd
            iten["shamt"] = shamt
            iten["funct"] = funct
        else:
            iten["undef_form"] = "formatar esse iten"
    else:
        if op_name == "mfhi" or op_name == "mflo":
            op = r_dict[op_name]
            rs_rt = "0000000000"
            rd = spli[1]
            shamt = "00000"
            funct = funct_dict[op_name]
            iten["op"] = op
            iten["rs_rt"] = rs_rt
            iten["rd"] = rd
            iten["shamt"] = shamt
            iten["funct"] = funct
        else:
            iten["undef_form"] = "formatar esse iten"


def format_i(iten):
    iten_instruc = iten["instruction"]
    remove_comma = iten_instruc.replace(",", " ")
    spli = remove_comma.split()

    if len(spli) == 4:
        if is_number(spli[3]):
            op_name = spli[0]

            op = i_dict[op_name]
            rs = spli[2]
            rt = spli[1]
            imm = spli[3]

            iten["op"] = op
            iten["rs"] = rs
            iten["rt"] = rt
            iten["imm"] = imm

        else:  # len=4 porém último índice não é número
            if spli[3][0] == "$":
                op_name = spli[0]

                op = i_dict[op_name]
                rs = spli[2]
                rt = spli[1]
                imm = spli[3]

                iten["op"] = op
                iten["rs"] = rs
                iten["rt"] = rt
                iten["imm"] = imm
            else:
                op_name = spli[0]

                op = i_dict[op_name]
                rs = spli[2]
                rt = spli[1]
                imm = spli[3]

                iten["op"] = op
                iten["rs"] = rs
                iten["rt"] = rt
                iten["imm"] = imm

    else:
        if "(" in spli[2]:
            ctt = re.findall("\(.*?\)", spli[2])
            ctt_ = ctt[0].replace("(", "").replace(")", "")

            ctt2 = re.sub(r"\([^)]*\)", "", spli[2])

            op_name = spli[0]

            op = i_dict[op_name]
            rs = ctt_
            rt = spli[1]
            imm = ctt2

            iten["op"] = op
            iten["rs"] = rs
            iten["rt"] = rt
            iten["imm"] = imm
        else:
            op_name = spli[0]
            op = i_dict[op_name]
            rs = 0
            rt = spli[1]
            imm = spli[2]

            iten["op"] = op
            iten["rs"] = rs
            iten["rt"] = rt
            iten["imm"] = imm


def format_j(iten):
    iten_instruc = iten["instruction"]
    remove_comma = iten_instruc.replace(",", " ")
    spli = remove_comma.split()

    op_name = spli[0]
    op = j_dict[op_name]
    _address_ = spli[1]

    iten["op"] = op
    iten["_address_"] = _address_


# Recuperando valores do formato!
for iten in list_isntructions_types:
    # R-TYPE
    if iten["type"] == "R-TYPE":
        format_r(iten)

    # I-TYPE
    elif iten["type"] == "I-TYPE":
        format_i(iten)

    # J-TYPE
    elif iten["type"] == "J-TYPE":
        format_j(iten)

    else:  ##Type não identificado !
        pass


# converte de hexadecimal para binario
def hexa_bin(hexa, num_of_bits):
    scale = 16 
    return bin(int(hexa, scale))[2:].zfill(num_of_bits)


for i in list_isntructions_types:
    print(i)
    for j in i:
        if(j == 'rs'):
            num = number_reg(i[j])
            if(num):
                i[j] = np.binary_repr(num,5)
            else:
                i[j] = np.binary_repr(0,5)
        if(j == 'rd'):
            num = number_reg(i[j])
            if(num):
                i[j] = np.binary_repr(num,5)
            else:
                i[j] = np.binary_repr(0,5)
        if(j == 'rt'):
            num = number_reg(i[j])
            if(num):
                i[j] = np.binary_repr(num,5)
            else:
                i[j] = np.binary_repr(0,5)
        if(j == 'imm'):
            if(i[j][0] == '$'):
                num = number_reg(i[j])
                if(num):
                    i[j] = np.binary_repr(num,16)
                else:
                    i[j] = np.binary_repr(0,16)
            elif(i[j] in labelDict):
                i[j] = np.binary_repr(labelDict[i[j]],16)

            elif(len(i[j]) > 1 and i[j][0] == '0' and i[j][1] == 'x'):

                i[j] = hexa_bin(i[j],16)

            else:
                i[j] = np.binary_repr(int(i[j]),16)


        if(j == 'shamt'):
            if(i['type'] == 'R-TYPE'):
                if(i[j] != '00000'):
                    i[j] = np.binary_repr(int(i[j]),5)

        if(j == '_address_'):
            if(i['op'] == '000011'):
                if(i[j][0] == '$'):
                    num = number_reg(i[j])
                    if(num):
                        i[j] = np.binary_repr(num,26)
                    else:
                        i[j] = np.binary_repr(0,26)
                elif(i[j] in labelDict):
                    i[j] = np.binary_repr(labelDict[i[j]],26)
                elif(i[j][0] == '0' and i[j][1] == 'x'):
                    i[j] = hexa_bin(i[j],26)
            elif('jr ' in i['instruction']):
                if(i[j][0] == '$'):
                    num = number_reg(i[j])
                    if(num):
                        i[j] = np.binary_repr(num,5)
                    else:
                        i[j] = np.binary_repr(0,5)
                elif(i[j] in labelDict):
                    i[j] = np.binary_repr(labelDict[i[j]],5)
                elif(i[j][0] == '0' and i[j][1] == 'x'):
                    i[j] = hexa_bin(i[j],5)
                i[j] = i[j] + '000000000000000001000'
            elif('jalr' in i['instruction']):
                num = number_reg(i[j])
                if(num):
                    i[j] = np.binary_repr(num,5)
                else:
                    i[j] = np.binary_repr(0,5)

                if(i['instruction'].find(',') != -1):
                    s = i['instruction'].split(',')[-1].strip()
                    num2 = number_reg(s)
                    i[j] = i[j] + '00000' + np.binary_repr(num2,5) + '00000001001'
                else:
                    i[j] = i[j] + '000001111100000001001'

            else:
                num = number_reg(i[j])
                if(num):
                    i[j] = np.binary_repr(num,15)
                else:
                    i[j] = np.binary_repr(0,15)
                

for i in list_isntructions_types:
    for j in i:
        if(j == 'address'):
            i[j] = np.base_repr(int(i[j]),base=16).rjust(8,'0')

#juntar a instrução
saida = []
for i in list_isntructions_types:
    aux = 0
    s =''
    for k,v in i.items():
        aux+=1
        if(aux >= 4):
            s = s + v
    saida.append(s)    

#transformar instrução em hexadecimal 
for i in range(0,len(saida)):
    if(saida[i]):
        saida[i] = np.base_repr(int(saida[i], 2),base=16).rjust(8,'0')
    

address_ = []
for i in list_isntructions_types:
    if(i['address']):
        address_.append(i['address'])

# mandar endereço e instrução para mif no formato -->    address : instrução
saida_text = open("saida_text.mif", "w")
s = ''
header = ['DEPTH = 16384;\n',
         'WIDTH = 32;\n',
         'ADDRESS_RADIX = HEX;\n',
         'DATA_RADIX = HEX;\n',
         'CONTENT\n',
         'BEGIN\n\n']

saida_text.writelines(header)
for i,j in zip(address_,saida):
    s = i + ' : ' + j + '\n'
    saida_text.writelines(s)

saida_text.writelines('\nEND')
saida_text.close()

# Fechar arquivo
entrada.close()
entrada2.close()
