import re

class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme
    
    def __repr__(self):
        return f"{self.type} -> {self.lexeme}"

def lexer(input_str):
    # Regular expressions for different tokens
    identifier = re.compile(r'[a-zA-Z_]\w*')
    integer = re.compile(r'\d+')
    real = re.compile(r'\d+\.\d+')
    operators = re.compile(r'[=<>!+\-*/]')
    separators = re.compile(r'[();,]')
    keywords = {'while', 'if', 'else', 'int', 'float', 'double'}
    
    index = 0
    while index < len(input_str):
        # Skip whitespace
        if input_str[index].isspace():
            index += 1
            continue
        
        # Match keywords, identifiers, integers, real numbers, operators, and separators.
        m = identifier.match(input_str, index)
        if m:
            lexeme = m.group(0)
            if lexeme in keywords:
                yield Token('Keyword', lexeme)
            else:
                yield Token('Identifier', lexeme)
            index = m.end()
            continue
        
        #match with real numbers
        m = real.match(input_str, index)
        #checks if it is not none
        if m:
            #if match was found, yields a new token with type 'Real'
            # group is used to get the entire part that matches with the 'Real'
            yield Token('Real', m.group(0))
            #checks for the end
            index = m.end()
            continue
        
        #if match is found, yields a new token with 'Integer'
        m = integer.match(input_str, index)
        if m:
            yield Token('Integer', m.group(0))
            index = m.end()
            continue
        
        #if match found, yields token for 'Operator'
        m = operators.match(input_str, index)
        if m:
            yield Token('Operator', m.group(0))
            index = m.end()
            continue
        
        #if match is found, yield token for Separator
        m = separators.match(input_str, index)
        if m:
            yield Token('Separator', m.group(0))
            index = m.end()
            continue
        
        raise ValueError(f"Invalid character: {input_str[index]} at index {index}")



# Read input from file
with open("input_scode.txt", 'r') as file:
    input_str = file.read()

# Create and open the output file
with open("output.txt", 'w') as file:
    file.write("Token | Lexeme\n")
    # Iterate through tokens returned by lexer and write them to the output file
    for token in lexer(input_str):
        file.write(str(token) + '\n')
        print(token)
