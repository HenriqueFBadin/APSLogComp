# APSLogComp

```ebnf
PROGRAM = SETUP, { STATEMENT } ;


SETUP = "music_base", "{", ( INSTRUMENT | TEMPO ), "}" ;


STATEMENT = ( λ 
	    | PLAYNOTE
	    | PLAYSEQUENCE
	    | PAUSE 
            | "repeat", ( NUMBER | IDENTIFIER ), "times", [ "while", BEXPRESSION ] "\n", BLOCK 
	    | "if", BEXPRESSION, "\n", BLOCK, ["else", BLOCK] 
	    | "var", IDENTIFIER, "=", ( NOTE | SEQUENCE | STRING | NUMBER ) ), "\n" ;


NOTE = "note", ( NOTE_NAME | IDENTIFIER ), "duration", ( NUMBER | IDENTIFIER ) ;
PAUSE = "pause", "duration", ( NUMBER | IDENTIFIER ) ;
INSTRUMENT = "instrument", ( STRING | IDENTIFIER ) ;
TEMPO = "tempo_base", ( NUMBER | IDENTIFIER ) ;
SEQUENCE = "[", ( NOTE | IDENTIFIER ), { ",", ( NOTE | IDENTIFIER ) }, "]" ;


PLAYNOTE = "play_note", ( NOTE | IDENTIFIER ) ; 
PLAYSEQUENCE = "play_sequence", ( SEQUENCE | IDENTIFIER ) ;


BLOCK = "{", "\n", { STATEMENT }, "}" ;
BEXPRESSION  = BTERM, { ( "||", "or" ) , BTERM } ; 
BTERM = RELEXPRESSION, { ( "&&" | "and" ), RELEXPRESSION } ;
RELEXPRESSION = EXPRESSION, { ( "==" | "!=" | ">" | "<" | ">=" | "<=" ), EXPRESSION } ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = ( ( "+" | "-" | ( "!" | "not" ) ), FACTOR
         | IDENTIFIER
         | NUMBER
         | STRING                              
         | "(", EXPRESSION, ")" ) ;


NOTE_NAME = ( LETTER, [ ACCIDENTAL ], [ DIGIT, { DIGIT } ] ) ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
STRING = '"', { CHARACTER }, '"' ;
CHARACTER = ( LETTER | DIGIT ) ;
NUMBER = DIGIT, { DIGIT }, [ ".", DIGIT, { DIGIT } ] ;
LETTER = ( A | ... | G ) ;
ACCIDENTAL = ( "#" | "b" ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```

## Descrição do que foi feito para a **Entrega Parcial 1**

Para essa entrega foi desenvolvida uma EBNF, que está presente no arquivo EBNF_APS.txt, para uma linguagem de criação de música.

A linguagem desenvolvida permite a criação de sequências musicais programáveis de forma simples e estruturada.

O programa é dividido em duas partes principais:

- **music_base**: configuração inicial do instrumento e do tempo base (bpm).
- **statements**: comandos musicais como tocar notas, pausas, repetições, condicionais e declarações de variáveis.

Os principais recursos da linguagem incluem:

1. **Notas individuais**: tocam uma nota específica com uma duração configurável.
2. **Sequências de notas**: agrupam várias notas e tocam todas em sequência.
3. **Pausas**: inserem períodos de silênço entre as notas.
4. **Repetições**: repetem blocos de notas um número determinado de vezes, com opção de condição (while) para loops dinâmicos.
5. **Condicionais (if/else)**: permitem executar diferentes trechos musicais com base em expressões lógicas.
6. **Variáveis**: armazenam números, notas ou sequências, permitindo reuso e composição dinâmica.
7. **Operadores aritméticos e booleanos**: possibilitam expressões dentro de `if` e `repeat while`.

Mais detalhes de como devem ser as suas utilizações podem ser encontrados na EBNF.

### Exemplo simples de código que eu pensei quando estava no processo criativo da linguagem

```plaintext
music_base {
    instrument "piano"
    tempo_base 120
}

var melodia = [ note C duration 1, note E duration 1, note G duration 1 ]

play_sequence melodia

var ritmo = 3

repeat 3 times
{
    play_note note F duration 0.5
    play_note note D duration 0.5
    pause duration 0.25
    play_note note C duration 0.5

    if ritmo == 1
    {
        play_note note F duration 1
        play_note note D duration 1
        play_note note C duration 1
    }
    else
    {
        ritmo = ritmo - 1
        play_sequence [ note A duration 0.5, note G duration 0.5 ]
    }
}
```

