/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_MUSIC_TAB_H_INCLUDED
# define YY_YY_MUSIC_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    MUSIC_BASE = 258,              /* MUSIC_BASE  */
    INSTRUMENT = 259,              /* INSTRUMENT  */
    TEMPO = 260,                   /* TEMPO  */
    NOTE = 261,                    /* NOTE  */
    DURATION = 262,                /* DURATION  */
    PAUSE = 263,                   /* PAUSE  */
    REPEAT = 264,                  /* REPEAT  */
    TIMES = 265,                   /* TIMES  */
    WHILE = 266,                   /* WHILE  */
    IF = 267,                      /* IF  */
    ELSE = 268,                    /* ELSE  */
    VAR = 269,                     /* VAR  */
    PLAY_NOTE = 270,               /* PLAY_NOTE  */
    PLAY_SEQUENCE = 271,           /* PLAY_SEQUENCE  */
    EQ = 272,                      /* EQ  */
    GT = 273,                      /* GT  */
    LT = 274,                      /* LT  */
    AND = 275,                     /* AND  */
    OR = 276,                      /* OR  */
    NOT = 277,                     /* NOT  */
    PLUS = 278,                    /* PLUS  */
    MINUS = 279,                   /* MINUS  */
    MULTIPLIER = 280,              /* MULTIPLIER  */
    DIV = 281,                     /* DIV  */
    LPAREN = 282,                  /* LPAREN  */
    RPAREN = 283,                  /* RPAREN  */
    LBRACE = 284,                  /* LBRACE  */
    RBRACE = 285,                  /* RBRACE  */
    LBRACKET = 286,                /* LBRACKET  */
    RBRACKET = 287,                /* RBRACKET  */
    COMMA = 288,                   /* COMMA  */
    ASSIGN = 289,                  /* ASSIGN  */
    NEWLINE = 290,                 /* NEWLINE  */
    NOTE_NAME = 291,               /* NOTE_NAME  */
    IDENTIFIER = 292,              /* IDENTIFIER  */
    STRING = 293,                  /* STRING  */
    NUMBER = 294,                  /* NUMBER  */
    BOOL = 295,                    /* BOOL  */
    ERROR = 296                    /* ERROR  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 11 "music.y"

    char *id;
    char *str;
    float num;
    int boolean;

#line 112 "music.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_MUSIC_TAB_H_INCLUDED  */
