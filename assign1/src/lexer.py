import ply.lex as lex

keywords = [
'KEYWORD_alias','KEYWORD_and','KEYWORD_BEGIN','KEYWORD_begin','KEYWORD_break','KEYWORD_case','KEYWORD_class','KEYWORD_def','KEYWORD_defined?','KEYWORD_do',
'KEYWORD_else','KEYWORD_elsif','KEYWORD_END','KEYWORD_end','KEYWORD_ensure','KEYWORD_false','KEYWORD_for','KEYWORD_if','KEYWORD_in','KEYWORD_module','KEYWORD_next',
'KEYWORD_nil','KEYWORD_not','KEYWORD_or','KEYWORD_redo','KEYWORD_rescue','KEYWORD_retry','KEYWORD_return','KEYWORD_self','KEYWORD_super','KEYWORD_then',
'KEYWORD_true','KEYWORD_undef','KEYWORD_unless','KEYWORD_until','KEYWORD_when','KEYWORD_while','KEYWORD_yield','KEYWORD___ENCODING__','KEYWORD___END__','KEYWORD___FILE__','KEYWORD___LINE__'
]

operators = [
	# +,-,*,/,%,&,|,^ ,!,~,=
    'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD',
    'BITAND', 'BITOR', 'BITXOR', 'BITNOT', 'BITCOMP', 'EQUAL'
]

identifiers = [
    'IDENTIFIER'
]

tokens = keywords + operators + identifiers

#keywords

t_KEYWORD_alias = r'alias'
t_KEYWORD_and = r'and'
t_KEYWORD_BEGIN = r'BEGIN'
t_KEYWORD_begin = r'begin'
t_KEYWORD_break = r'break'
t_KEYWORD_case = r'case'

# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIV              = r'/'
t_MOD              = r'%'
t_BITAND           = r'&'
t_BITOR            = r'\|'
t_BITXOR           = r'\^'
t_BITCOMP          = r'~'
t_BITNOT           = r'!'
t_EQUAL            = r'='

reserved_map = { }
for r in keywords:
    reserved_map[ r[8:] ] = r

def t_IDENTIFIER(t):
    r'@?[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"IDENTIFIER")
    return t

#newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = 'alias + alj ='

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)


