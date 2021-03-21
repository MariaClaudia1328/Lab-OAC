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


# --o que não sei resolver ainda--
# quando o label termina de ser montado
# no caso de constantes muito grandes

# Identificacao dos registradores pela máscara, retorna um inteiro correspondente ao registrador (usado na hora da montagem)
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


# --primeira leitura -------------------
# ler linha a linha
# cada linha eu acrescento 32 bits ao endereço
# se for encontrado um label (nome que termina com : ) seu endereço e nome é guardado num dicionario diferente (symbol table)

# Leitura do arquivo de entrada .asm
entrada = open("requisito2.asm", "r")
# print("entrada!!!",entrada)

# Confere se arquivo foi aberto e começa o processo
if entrada.mode == "r":
    contents = entrada.readlines()  # le linha a linha
    # print("contents!!!", contents)
    address = 0  # endereço (int)
    reg = re.compile(
        "\w+:", flags=re.M
    )  # regex que é utilizada para identificar os labels
    labelDict = {}  # dicionario da tabela de simbolos das labels
    instructionsDict = {}
    for i in contents:
        i = i.replace("\n", "")
        address += 1  # cada instrução tem 32 bits
        matched = reg.match(i)  # busca label em cada linha
        if (
            matched
        ):  # se achou, pega a string, retira o : e adciona no dicionario com chave = address e valor = string
            label = matched.group()
            label = re.sub(":", "", label)
            labelDict[address] = label
        else:  # caso contrário, adiciono essa linha de instrução em outro dicionario
            instructionsDict[address] = i

    # print(labelDict)


# print(instructionsDict)
# print("------------------------------------------------------------")

list_isntructions = []
address2 = 0

for instruc in instructionsDict.values():
    address2 += 1
    infos = {"address": address2, "instruction": instruc}
    if ((".data" not in instruc) and (".text" not in instruc)) and instruc != "":
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


# print(list_isntructions_types)


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
        # print(iten)

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


# Formato ou Tipo não encontrado
#for iten in list_isntructions_types:
#    print(iten)
    # if iten["type"] == "UNDEFINED TYPE":
    #     print(iten)
    # if "undef_form" in iten.keys():
    #     print(iten)

# passar os valores dos campos para binario 
# na funcao da np.binary_repr eu passo como argumento o numero em decimal e o tanto de bits. Se o decimal for sinalizado,ele é passado para complemento de 2
for i in list_isntructions_types:
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
                    i[j] = np.binary_repr(num,5)
                else:
                    i[j] = np.binary_repr(0,5)
            else:
                num = number_reg(i[j])
                if(num):
                    i[j] = np.binary_repr(num,5)
                else:
                    i[j] = np.binary_repr(0,5)
        if(j == '_address_'):
            num = number_reg(i[j])
            if(num):
                i[j] = np.binary_repr(num,5)
            else:
                i[j] = np.binary_repr(0,5)
        #pesquisar na tabela de Label

# passar o endereço para hexadecimal 
# na função np.base_repr eu passo o numero, a base e o tamanho que eu quero
for i in list_isntructions_types:
    for j in i:
        if(j == 'address'):
            i[j] = np.base_repr(int(i[j]),base=16, padding=8)

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


#for k in saida:
#    print(k)

#transformar instrução em hexadecimal 
for i in saida:
    if(i):
        i = np.base_repr(int(i),base=16)

address_ = []
for i in list_isntructions_types:
    if(i['address']):
        address_.append(i['address'])

# mandar endereço e instrução para mif no formato -->    address : instrução
saida_text = open("saida_text.mif", "w")
header = ['DEPTH = 16384;\n',
         'WIDTH = 32;\n',
         'ADDRESS_RADIX = HEX;\n',
         'DATA_RADIX = HEX;\n',
         'CONTENT\n',
         'BEGIN\n\n']
saida_text.writelines(header)
s = ''
for i,j in zip(address_,saida):
    s = i + ' : ' + j + '\n'
    saida_text.writelines(s)

saida_text.writelines('\nEND')

#for iten in list_isntructions_types:
#   print(iten)

# Fechar arquivo
saida_text.close()
entrada.close()
# #--fim primeira parte -----------------


# # --segunda leitura--
#     # ler linha a linha
#     # no caso de encontrar instrução com apenas registradores: armazenar num dicionario --> 'endereço': 'instrução em bits'
#     # no caso de encontrar label: confere se o label existe e monta
#         # no caso de label dentro da instrução --> procura se existe, seu endereço e monta

# #Leitura do arquivo de entrada .asm
# # entrada = open('requisito2.asm','r')

# # aqui começa a montar a linguagem de máquina
# if entrada.mode == 'r':
#     conteudo = entrada.readlines()
#     # print(conteudo)
# # ------ fim segunda parte -----------


# # Escrita no arquivo das saídas de .data e .text
# saida01 = open('saida_data.mif','w')
# saida02 = open('saida_text.mif','w')
# # print(saida01)

# # Definição e escrita do cabecalho do .mif
# header = ['DEPTH = 16384;\n',
#         'WIDTH = 32;\n',
#         'ADDRESS_RADIX = HEX;\n',
#         'DATA_RADIX = HEX;\n',
#         'CONTENT\n',
#         'BEGIN\n']
# saida01.writelines(header)
# saida02.writelines(header)

# #escrita no arquivo saida_data.mif

# #escrita no arquivo saida_text.mif

# #Finalização do arquivo
# saida01.write('\nEND;')
# saida02.write('\nEND;')

# # Fechar arquivos
# entrada.close()
# saida01.close()
# saida02.close()