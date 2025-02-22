grammar Angeh;  
program: (breath_cycle | ai_directive)+;  
breath_cycle: 'Breathe' ID 'into' ID '{' (inhale | exhale)+ '}';  
inhale: 'Inhale' source '->' type ('with' filter)?;  
exhale: 'Exhale' action ('->' target)?;  
ai_directive: '@AI' ':' STRING;  
// ... Full grammar rules  
grammar Angeh;

program: (statement | ai_directive)+ EOF;

statement: 
    breath_cycle
    | domain_declaration
    | quantum_op
    | assignment
    ;

breath_cycle: 'Breathe' ID 'into' ID '{' (inhale exhale)+ '}';
inhale: 'Inhale' source '->' type ('with' filter=expression)?;
exhale: 'Exhale' action '->' target;

domain_declaration: 'In' domain_type=('quantum'|'web'|'iot') '{' code_block '}';
quantum_op: 'Entangle' qubit_list 'with' coherence_level;

ai_directive: '@AI' ':' command=STRING;
assignment: ID '=' expression;

type: 'Flow<' dtype=type '>' | 'Pulse<' etype=type '>' | 'Qubit';
source: ID | STRING;
action: ID | function_call;
target: ID | function_call;

function_call: ID '(' (expression (',' expression)*)? ')';
expression: 
    INT | FLOAT | STRING
    | ID
    | '(' expression ')'
    | expression op=('*'|'/') expression
    | expression op=('+'|'-') expression
    ;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;