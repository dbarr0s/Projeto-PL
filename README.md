<p align="center">
  <img src="https://github.com/Duarte0903/IA_UMinho/blob/main/EEUMLOGO.png"/>
</p>

<h1 align="center">Projeto da UC de Processamento de Linguagens - 2023/2024</h1>
<h2 align="center">Compilador de Forth</h2>

## Introdução

Compilador da linguagem de programação Forth contruido com Python, que gera código para ser interpretado pela [máquina virtual](https://ewvm.epl.di.uminho.pt/) criada para a UC.

Foi construido um analisador léxico com [PLY-lex](https://ply.readthedocs.io/en/latest/ply.html#lex)

A gramática foi implementada com [PLY-Yacc](https://ply.readthedocs.io/en/latest/ply.html#yacc)

## Utilização 

1. Compilar o ficheiro de input
```
python main.py <path ficheiro>
```

2. Consultar os resultados na pasta output/
