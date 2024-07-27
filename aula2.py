# \r\n -> CRLF, no mac é somente o \n que existe como opção de quebra de linha -> LF 

print(12,34, sep=',', end='\r\n')
print(56,78, sep=",", end='\n')
print(9,10, sep=",", end='\n')

