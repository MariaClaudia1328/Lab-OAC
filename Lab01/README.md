# Lab01-OAC
Laboratório 01 da disciplina Organização e Arquitetura de Computadores

## Objetivo

- Gerar um código objeto montado em hexadecimal, em arquivo de texto ASCII, no formato MIF, a partir de uma listagem de instruções pré-definidas em Assembly MIPS

## Metodologia

1. Ler o arquivo .asm e imprimir o que foi lido em outro arquivo, para familiarizar-se com o formato do arquivo .asm 
2. Ler o arquivo .asm, alocando as instruções na memória 
3. Imprimir o que foi lido e o mapa da memória utilizada para verificação 
4. Traduzir o que foi armazenado na memória para hexadecimal
5. Depois de traduzir, ou assim que traduzir, inserir o resultado no .mif 

## Considerações

1. É preciso conhecer a estrutura do arquivo .mif
2. A próxima seção pode dar uma ideia do que deve ser feito no laboratório. Vou inserir o trecho em inglês do livro em uma imagem, no arquivo etc do repositório
3. Talvez, antes de traduzir para hexadecimal, a tradução deve ser feita em binário 

### Como o arquivo .asm (em assembly) pode ser lido [Fonte:Computer Organization and Design 4ed, Patterson and Henessy]

    Primeiro, o assembler lê cada linha do arquivo assembly e a quebra de acordo com seus componentes, essas partes são chamadas de 'lexemes', que são words, números e caracteres de pontuação. Por exemplo, a linha:
`ble $t0, 100, loop` 

    possui 6 partes, o opcode ble, o rs $t0, uma virgula, a constante 100, uma virgula e o símbolo loop. Se a linha começa com um label, o assembler guarda o nome e o endereço que a label ocupa em uma 'tabela de símbolos'. Depois, o assembler calcula quantas 'words' de memória a instrução irá ocupar. Monitorando quanto espaço de memória uma insrtução ocupa, o assembler saberá quando a próxima irá aparecer. Para calcular o tamanho da instrução, basta seguir o padrão MIPS. 

    Após esse processo, o assembler usa o conteúdo da 'tabela de símbolos', durante uma segunda leitura pelo arquivo, para produzir, de fato, linguagem de máquina. Novamente, o assembler examina cada linha do arquivo. Se a linha possui uma instrução, o assembler combina a representação binária de seu opcode e operandos em uma expressão legal (processo parecido ao do capitulo 2, seção 2.5). Intruções e words que fazem referencia a um símbolo externo, em outro arquivo, não podem ser montados, pois seus símbolos não estão na tabela de simbolos. Entretanto, o assembler não reclama de referencias não resolvidas, pois esse problema é resolvido posteriormente. 