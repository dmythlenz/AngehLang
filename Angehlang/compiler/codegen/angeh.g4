grammar Angeh;

program: (statement | function_def | class_def)*;

statement
    : variable_decl
    | assignment
    | function_call
    | if_statement
    | for_loop
    | while_loop
    | try_catch
    ;

variable_decl: type ID ('=' expression)? ';';

type
    : 'int'
    | 'float'
    | 'string'
    | 'bool'
    | 'List' '<' type '>'
    | 'Map' '<' type ',' type '>'
    ;

function_def
    : 'fn' ID '(' param_list? ')' '->' type? block
    ;

class_def
    : 'class' ID ('extends' ID)? '{' class_member* '}'
    ;

// ... rest of practical grammar rules