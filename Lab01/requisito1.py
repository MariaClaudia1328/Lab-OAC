import re #bib para usar regex

# --o que não sei resolver ainda--
    # quando o label termina de ser montado 
    # no caso de constantes muito grandes

#Identificacao dos registradores pela máscara, retorna um inteiro correspondente ao registrador (usado na hora da montagem)
def number_reg(mask):
    if(mask == '$0' or mask == '$zero'):return 0
    if(mask == '$1' or mask == '$at'):return 1
    if(mask == '$2' or mask == '$v0'):return 2
    if(mask == '$3' or mask == '$v1'):return 3
    if(mask == '$4' or mask == '$a0'):return 4
    if(mask == '$5' or mask == '$a1'):return 5
    if(mask == '$6' or mask == '$a2'):return 6
    if(mask == '$7' or mask == '$a3'):return 7
    if(mask == '$8' or mask == '$t0'):return 8
    if(mask == '$9' or mask == '$t1'):return 9
    if(mask == '$10' or mask == '$t2'):return 10
    if(mask == '$11' or mask == '$t3'):return 11
    if(mask == '$12' or mask == '$t4'):return 12
    if(mask == '$13' or mask == '$t5'):return 13
    if(mask == '$14' or mask == '$t6'):return 14
    if(mask == '$15' or mask == '$t7'):return 15
    if(mask == '$16' or mask == '$s0'):return 16
    if(mask == '$17' or mask == '$s1'):return 17
    if(mask == '$18' or mask == '$s2'):return 18
    if(mask == '$19' or mask == '$s3'):return 19   
    if(mask == '$20' or mask == '$s4'):return 20
    if(mask == '$21' or mask == '$s5'):return 21
    if(mask == '$22' or mask == '$s6'):return 22
    if(mask == '$23' or mask == '$s7'):return 23
    if(mask == '$24' or mask == '$t8'):return 24
    if(mask == '$25' or mask == '$t9'):return 25
    if(mask == '$26' or mask == '$k0'):return 26
    if(mask == '$27' or mask == '$k1'):return 27
    if(mask == '$28' or mask == '$gp'):return 28
    if(mask == '$29' or mask == '$sp'):return 29
    if(mask == '$30' or mask == '$fp'):return 30
    if(mask == '$31' or mask == '$ra'):return 31           

# --primeira leitura--
    # ler linha a linha
    # cada linha eu acrescento 32 bits ao endereço 
    # se for encontrado um label (nome que termina com : ) seu endereço e nome é guardado num dicionario diferente (symbol table)

#Leitura do arquivo de entrada .asm
entrada = open('requisito2.asm','r')

#Confere se arquivo foi aberto e começa o processo
if entrada.mode == 'r':
    contents = entrada.readlines() # le linha a linha  
    address = 0 # endereço (int)
    reg = re.compile('\w+:') # regex que é utilizada para identificar os labels
    symbolTable = {} #dicionario da tabela de simbolos das labels
    for i in contents:
        address += 32 # cada instrução tem 32 bits
        matched = reg.match(i) # busca label em cada linha
        if matched: # se achou, pega a string, retira o : e adciona no dicionario com chave = address e valor = string
            label = matched.group()
            label = re.sub(':','',label)
            symbolTable[address] =  label

# Fechar arquivo          
entrada.close()

# ------ fim primeira parte -----------

# --segunda leitura--
    # ler linha a linha 
    # no caso de encontrar instrução com apenas registradores: armazenar num dicionario --> 'endereço': 'instrução em bits'
    # no caso de encontrar label: confere se o label existe e monta
        # no caso de label dentro da instrução --> procura se existe, seu endereço e monta 

#Leitura do arquivo de entrada .asm       
entrada = open('requisito2.asm','r')

# aqui começa a montar a linguagem de máquina
if entrada.mode == 'r':
    conteudo = entrada.readlines()
    print(conteudo)

# ------ fim segunda parte -----------

# Escrita no arquivo das saídas de .data e .text
saida01 = open('saida_data.mif','w')
saida02 = open('saida_text.mif','w')

# Definição e escrita do cabecalho do .mif
header = ['DEPTH = 16384;\n',
        'WIDTH = 32;\n',
        'ADDRESS_RADIX = HEX;\n',    
        'DATA_RADIX = HEX;\n',
        'CONTENT\n',
        'BEGIN\n']
saida01.writelines(header)
saida02.writelines(header)

#escrita no arquivo saida_data.mif

#escrita no arquivo saida_text.mif

#Finalização do arquivo
saida01.write('\nEND;')
saida02.write('\nEND;')

# Fechar arquivos
entrada.close()
saida01.close()
saida02.close()
