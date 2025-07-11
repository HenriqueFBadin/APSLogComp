%{
#include "music.tab.h"
#include <stdlib.h>
#include <string.h>
int line_num = 1;
int lex_error_count = 0;
%}

%%

"music_base"         { return MUSIC_BASE; }
"instrument"         { return INSTRUMENT; }
"tempo_base"         { return TEMPO; }
"note"               { return NOTE; }
"duration"           { return DURATION; }
"pause_duration"     { return PAUSE; }
"repeat"             { return REPEAT; }
"times"              { return TIMES; }
"while"              { return WHILE; }
"if"                 { return IF; }
"else"               { return ELSE; }
"var"                { return VAR; }
"play_note"          { return PLAY_NOTE; }
"play_sequence"      { return PLAY_SEQUENCE; }

"true"               { yylval.boolean = 1; return BOOL; }
"false"              { yylval.boolean = 0; return BOOL; }

"=="                 { return EQ; }
">"                  { return GT; }
"<"                  { return LT; }
"&&"                 { return AND; }
"||"                 { return OR; }
"or"                 { return OR; }
"and"                { return AND; }
"+"                  { return PLUS; }
"-"                  { return MINUS; }
"*"                  { return MULTIPLIER; }
"/"                  { return DIV; }
"!"                  { return NOT; }
"("                  { return LPAREN; }
")"                  { return RPAREN; }
"{"                  { return LBRACE; }
"}"                  { return RBRACE; }
"["                  { return LBRACKET; }
"]"                  { return RBRACKET; }
","                  { return COMMA; }
"="                  { return ASSIGN; }
\n                   { line_num++; return NEWLINE; }
"//"[^\n]*       { /* Ignore single-line comments */ }
[ \t]+               { /* Ignore whitespace */ }

[0-9]+(\.[0-9]+)?    { yylval.num = atof(yytext); return NUMBER; }

\"[^\"]*\"           { yylval.str = strdup(yytext); return STRING; }

[A-G][#b]?[0-9]+     { yylval.id = strdup(yytext); return NOTE_NAME; }

[a-zA-Z_][a-zA-Z0-9_]* {
    yylval.id = strdup(yytext); return IDENTIFIER;
}

.                    { 
                       fprintf(stderr, "ERRO LÉXICO: caractere inválido '%s' na linha %d\n", 
                               yytext, line_num); 
                       lex_error_count++;
                       return ERROR;
                     }

%%

int yywrap(void) {
    return 1;
}

void print_lexical_status() {
    if (lex_error_count == 0) {
        printf("Análise léxica bem-sucedida\n");
    } else {
        printf("Análise léxica concluída com %d erros\n", lex_error_count);
    }
}
