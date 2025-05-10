%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
int yylex(void);
int error_count = 0;
%}

%union {
    char *id;
    char *str;
    float num;
}

%token MUSIC_BASE INSTRUMENT TEMPO NOTE DURATION PAUSE REPEAT TIMES WHILE IF ELSE VAR PLAY_NOTE PLAY_SEQUENCE
%token EQ NEQ GT LT GTE LTE AND OR NOT
%token PLUS MINUS TIMES_OP DIV
%token LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET COMMA ASSIGN NEWLINE
%token <id> NOTE_NAME
%token <id> IDENTIFIER
%token <str> STRING
%token <num> NUMBER
%token ERROR

%%

PROGRAM:
    SETUP NEWLINE STATEMENTS
;

SETUP:
    MUSIC_BASE LBRACE instrument_or_tempo RBRACE NEWLINE
;

instrument_or_tempo:
    INSTRUMENT STRING
  | TEMPO NUMBER
  | INSTRUMENT STRING NEWLINE TEMPO NUMBER
  | TEMPO NUMBER NEWLINE INSTRUMENT STRING
  | INSTRUMENT STRING NEWLINE
  | TEMPO NUMBER NEWLINE
  | INSTRUMENT STRING NEWLINE TEMPO NUMBER NEWLINE
  | TEMPO NUMBER NEWLINE INSTRUMENT STRING NEWLINE
;

STATEMENTS:
    /* vazio */
  | STATEMENTS STATEMENT
;

STATEMENT:
    PLAY_NOTE NOTE_ITEM NEWLINE
  | PLAY_NOTE IDENTIFIER NEWLINE
  | PLAY_SEQUENCE SEQUENCE NEWLINE
  | PLAY_SEQUENCE IDENTIFIER NEWLINE
  | PAUSE DURATION NUMBER NEWLINE
  | PAUSE DURATION IDENTIFIER NEWLINE
  | VAR IDENTIFIER ASSIGN VAR_VALUE NEWLINE
  | REPEAT NUMBER TIMES WHILE BEXPRESSION NEWLINE BLOCK
  | REPEAT IDENTIFIER TIMES WHILE BEXPRESSION NEWLINE BLOCK
  | REPEAT NUMBER TIMES NEWLINE BLOCK
  | REPEAT IDENTIFIER TIMES NEWLINE BLOCK
  | IF BEXPRESSION NEWLINE BLOCK
  | IF BEXPRESSION NEWLINE BLOCK ELSE BLOCK
  | error NEWLINE { error_count++; /* Incrementa o contador de erros */ }
  | NEWLINE
;

VAR_VALUE:
    NOTE_ITEM
  | SEQUENCE
  | STRING
  | NUMBER
  | IDENTIFIER
;

NOTE_ITEM:
    NOTE NOTE_NAME DURATION NUMBER
  | NOTE IDENTIFIER DURATION NUMBER
  | NOTE NOTE_NAME DURATION IDENTIFIER
  | NOTE IDENTIFIER DURATION IDENTIFIER
;

SEQUENCE:
    LBRACKET NOTE_OR_ID_LIST RBRACKET
  | LBRACKET NOTE_OR_ID_LIST COMMA RBRACKET
;

NOTE_OR_ID_LIST:
    NOTE_OR_ID
  | NOTE_OR_ID_LIST COMMA NOTE_OR_ID
;

NOTE_OR_ID:
    NOTE_ITEM
  | IDENTIFIER
;

BLOCK:
    LBRACE NEWLINE STATEMENTS RBRACE
;

BEXPRESSION:
    BTERM
  | BEXPRESSION OR BTERM
;

BTERM:
    RELEXPRESSION
  | BTERM AND RELEXPRESSION
;

RELEXPRESSION:
    EXPRESSION
  | EXPRESSION EQ EXPRESSION
  | EXPRESSION NEQ EXPRESSION
  | EXPRESSION GT EXPRESSION
  | EXPRESSION LT EXPRESSION
  | EXPRESSION GTE EXPRESSION
  | EXPRESSION LTE EXPRESSION
;

EXPRESSION:
    TERM
  | EXPRESSION PLUS TERM
  | EXPRESSION MINUS TERM
;

TERM:
    FACTOR
  | TERM TIMES_OP FACTOR
  | TERM DIV FACTOR
;

FACTOR:
    NUMBER
  | STRING
  | IDENTIFIER
  | NOT FACTOR
  | LPAREN EXPRESSION RPAREN
;

%%

void yyerror(const char *s) {
    extern char *yytext;
    extern int line_num;
    fprintf(stderr, "ERRO SINTÁTICO na linha %d: %s (token atual: '%s')\n", 
            line_num, s, yytext);
}

int main() {
    /* O lexer já conta seus próprios erros */
    int result = yyparse();
    
    /* Reportar apenas erros sintáticos aqui */
    if (result == 0) {
        if (error_count == 0) {
            printf("Análise sintática bem-sucedida\n");
        } else {
            printf("Análise sintática concluída com %d erros\n", error_count);
        }
    } else {
        printf("Análise sintática falhou\n");
    }
    
    /* Opcional: chamar função do lexer para reportar erros léxicos */
    extern void print_lexical_status();
    print_lexical_status();
    
    /* Retornar status com base apenas nos erros sintáticos */
    return (result == 0 && error_count == 0) ? 0 : 1;
}