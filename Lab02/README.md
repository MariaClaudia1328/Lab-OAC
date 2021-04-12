# Laboratório 02 de OAC

## Objetivo

- Montar os módulos principais da unidade operativa (Datapath), que compõem a arquitetura MIPS Uniciclo
- Esses módulos devem processar um conjunto de instruções de 32 bits pré-compiladas no formato .mif

## Metodologia

### Requisito 01: Implementação da Unidade Operativa Uniciclo MIPS

- Fazer modificações necessárias na Unidade Operativa da imagem de forma que o processamento do Uniciclo completo ocorra
- Apresentar unidade de controle, com sinais de controle em cada módulo e registradores
- Módulos a serem desenvolvidos:
    - ULA
    - Muxes
    - Memória de instruções (requisito 2)
    - Memória de dados (requisito 2)
    - Banco de registradores 
    - Extensão de sinal
    - Deslocamento de 2 à esquerda 
    - Unidade para multiplicação 
    - Unidade para instrução jump
    - Unidade de controle

### Requisito 02: Bloco de Memória de Dados e Instruções

- Criar os blocos de memória de dados e instruções seguindo a organização do tipo Havard
- Utilizar recursos do Quartus:
    - memory megafunctions, codigos em verilog ou uVHDL
- Utilizar para o desenvolvimento e teste os arquivos UnicicloInst.mif e UnicicloData.mif, assim como o Uniciclo.asm
- Sugestão para o uso dos endereços: usar o endereçamento do MARS
- Esses módulos devem ser desenvolvidos de forma a suportar respectivos tamanhos e codificações necessários para que os dados sejam processados pelos módulos subsequentes
- A metodologia deve ser feita de forma sincronizada com os demais módulos da unidade operativa

### Requisito 03: Suporte a Tipos de Instruções

- O funcionamento dos módulos deve ser feito com o Waveform Editor do Quartus com as entradas do campo opcode, funct. 
- A operação da ULA deve ser completa
- Lista das instruções que devem ser suportadas

### Requisito 04: Análise de Desempenho das Unidades Desenvolvidas

- Usar o Waveform para mostrar o que está sendo processado de cada instrução em cada módulo
- Medir tempo de execução, identificar gargalos, etc.

## Observações

- Se utilizar um modo para construir como blocos nativos do quartus, verilog, a consistencia deve ser mantida pra evitar problemas --> Se usou verilog em um, ele deve ser usado em todos

## Infos
