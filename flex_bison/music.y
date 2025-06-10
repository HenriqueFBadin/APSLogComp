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
    int boolean;
}

%token MUSIC_BASE INSTRUMENT TEMPO NOTE DURATION PAUSE REPEAT TIMES WHILE IF ELSE VAR PLAY_NOTE PLAY_SEQUENCE
%token EQ GT LT AND OR NOT
%token PLUS MINUS MULTIPLIER DIV
%token LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET COMMA ASSIGN NEWLINE
%token <id> NOTE_NAME
%token <id> IDENTIFIER
%token <str> STRING
%token <num> NUMBER
%token <boolean> BOOL
%token ERROR

%%

PROGRAM:
      SETUP PROGRAM_SUFFIX
;

PROGRAM_SUFFIX:
      /* vazio */
    | PROGRAM_SUFFIX VARDEC NEWLINE
    | PROGRAM_SUFFIX BLOCK
    | PROGRAM_SUFFIX NEWLINE
;

SETUP:
      MUSIC_BASE LBRACE OPTIONAL_NEWLINES INSTRUMENT STRING NEWLINES TEMPO NUMBER OPTIONAL_NEWLINES RBRACE NEWLINE
    | MUSIC_BASE LBRACE OPTIONAL_NEWLINES TEMPO NUMBER NEWLINES INSTRUMENT STRING OPTIONAL_NEWLINES RBRACE NEWLINE
;

OPTIONAL_NEWLINES:
      /* vazio */
    | NEWLINES
;

NEWLINES:
      NEWLINE
    | NEWLINES NEWLINE
;

VARDEC:
      VAR IDENTIFIER TYPE VAR_INIT
;

VAR_INIT:
      /* vazio */
    | ASSIGN BEXPRESSION
;

TYPE:
      IDENTIFIER    /* tipos como int, double, bool */
    | NOTE          /* tipo especial "note" */
    | SEQUENCE      /* tipo especial "sequence" */
;

BLOCK:
      LBRACE NEWLINE STATEMENTS RBRACE
;

STATEMENTS:
      /* vazio */
    | STATEMENTS STATEMENT
;

STATEMENT:
      ASSIGNMENT NEWLINE
    | PLAYNOTE NEWLINE
    | PLAYSEQUENCE NEWLINE
    | PAUSE NUMBER NEWLINE
    | PAUSE IDENTIFIER NEWLINE
    | REPEAT EXPRESSION TIMES BLOCK
    | REPEAT EXPRESSION TIMES WHILE BEXPRESSION BLOCK
    | IF BEXPRESSION BLOCK
    | IF BEXPRESSION BLOCK ELSE BLOCK
    | VARDEC NEWLINE
    | NEWLINE
;

ASSIGNMENT:
      IDENTIFIER ASSIGN BEXPRESSION
;

PLAYNOTE:
      PLAY_NOTE NOTE_ITEM
    | PLAY_NOTE IDENTIFIER
;

PLAYSEQUENCE:
      PLAY_SEQUENCE SEQUENCE
    | PLAY_SEQUENCE IDENTIFIER
;

NOTE_ITEM:
      NOTE NOTE_NAME DURATION NUMBER
    | NOTE IDENTIFIER DURATION NUMBER
;

SEQUENCE:
      LBRACKET SEQITEM SEQITEM_LIST RBRACKET
;

SEQITEM_LIST:
      /* vazio */
    | COMMA SEQITEM SEQITEM_LIST
;

SEQITEM:
      NOTE_ITEM PAUSE NUMBER
    | IDENTIFIER PAUSE NUMBER
;

BEXPRESSION:
      BTERM
    | BEXPRESSION OR BTERM
    | LPAREN BEXPRESSION RPAREN
;

BTERM:
      RELEXPRESSION
    | BTERM AND RELEXPRESSION
    | LPAREN BTERM RPAREN
;

RELEXPRESSION:
      EXPRESSION
    | EXPRESSION EQ EXPRESSION
    | EXPRESSION GT EXPRESSION
    | EXPRESSION LT EXPRESSION
    | LPAREN RELEXPRESSION RPAREN
;

EXPRESSION:
      TERM
    | EXPRESSION PLUS TERM
    | EXPRESSION MINUS TERM
;

TERM:
      FACTOR
    | TERM MULTIPLIER FACTOR
    | TERM DIV FACTOR
;

FACTOR:
      NUMBER
    | BOOL
    | STRING
    | IDENTIFIER
    | NOTE_ITEM
    | SEQUENCE
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
    int result = yyparse();
    if (result == 0) {
        if (error_count == 0) {
            printf("Análise sintática bem-sucedida\n");
        } else {
            printf("Análise sintática concluída com %d erros\n", error_count);
        }
    } else {
        printf("Análise sintática falhou\n");
    }
    extern void print_lexical_status();
    print_lexical_status();
    return (result == 0 && error_count == 0) ? 0 : 1;
}
