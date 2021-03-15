# Laboratório 01 da disciplina Organização e Arquitetura de Computadores

## Objetivo

Criar um código objeto motando em Hexadecimal a partir de um arquivo texto .asm em ASCII. Escrever um relatório sobre o que foi feito.

## Metodologia para montar o código objeto

1. Ler cada linha do arquivo .asm
2. Quebrar a linha de acordo com seus componentes
    * se linha começa com label ( no formato Label:), o nome e o endereço devem ser armazenados numa tabela
    * calculo de quantas 'words' de memória a instrução irá ocupar para saber quando a próxima irá aparecer --> **O MIPS tem o padrão de 32 bits**
3. Ler novamente o arquivo .asm
4. Examinar novamente cada linha do arquivo para montar a linguagem de máquina
    * Se encontra uma instrução: pego endereço e calculo o valor de seus campos em binário, depois converto para hexadecimal
    * Se encontra uma label, consulta a tabela para ver se contém o label e montar o que estiver dentro da label
5. Imprimir o que foi montado em **hexadecimal** para .data em um arquivo e para .text em outro, seguindo o padrão .mif

## Considerações

1. É preciso conhecer a estrutura do arquivo .mif
2. A próxima seção pode dar uma ideia do que deve ser feito no laboratório. Vou inserir o trecho em inglês do livro em uma imagem, no arquivo *etc* do repositório
3. Antes de traduzir para hexadecimal, a montagem deve ser feita em binário
4. O arquivo de entrada contém:
    * Instruções dadas no requisito2
    * registradores inteiros da CPU MIPS assim como suas máscaras
    * entradas no campo imediato com números inteiros ou decimais, ambos inteiros e sinalizados
5. Uma dúvida que fica é se constantes muito grandes serão usadas e se isso é um problema
6. Apenas uma tabela para os labels será usada pois é o mesmo arquivo

## Outros
### Como o arquivo .asm (em assembly) pode ser lido [Fonte:Computer Organization and Design 4ed, Patterson and Henessy]

    Primeiro, o assembler lê cada linha do arquivo assembly e a quebra de acordo com seus componentes, essas partes são chamadas de 'lexemes', que são words, números e caracteres de pontuação. Por exemplo, a linha:
`ble $t0, 100, loop` 

    possui 6 partes, o opcode ble, o rs $t0, uma virgula, a constante 100, uma virgula e o símbolo loop. Se a linha começa com um label, o assembler guarda o nome e o endereço que a label ocupa em uma 'tabela de símbolos'. Depois, o assembler calcula quantas 'words' de memória a instrução irá ocupar. Monitorando quanto espaço de memória uma insrtução ocupa, o assembler saberá quando a próxima irá aparecer. Para calcular o tamanho da instrução, basta seguir o padrão MIPS. 

    Após esse processo, o assembler usa o conteúdo da 'tabela de símbolos', durante uma segunda leitura pelo arquivo, para produzir, de fato, linguagem de máquina. Novamente, o assembler examina cada linha do arquivo. Se a linha possui uma instrução, o assembler combina a representação binária de seu opcode e operandos em uma expressão legal (processo parecido ao do capitulo 2, seção 2.5). Intruções e words que fazem referencia a um símbolo externo, em outro arquivo, não podem ser montados, pois seus símbolos não estão na tabela de simbolos. Entretanto, o assembler não reclama de referencias não resolvidas, pois esse problema é resolvido posteriormente. 

### Links importantes
* Sobre arquivo .mif : [Inicialização de memória com arquivos .MIF e .HEX](https://wiki.sj.ifsc.edu.br/wiki/index.php/Inicializa%C3%A7%C3%A3o_de_mem%C3%B3ria_com_arquivos_.MIF_e_.HEX)
