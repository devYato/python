def external_function():
    
    # Criando uma variavel 'external_var no escopo da funcao externa
    external_var = 'Eu sou uma variavel externa'
    
    # Definindo uma funcao interna que acessa essa variavel
    def internal_function():
        #usando a palavra-chave 'nonlocal' para indicar que queremos usar a variavel do escopo externo
        nonlocal external_var
        print(external_var)
        # Modificando a variavel externa
        external_var = 'Variavel externa modificada'
        print(external_var)
        
    internal_function()
    
external_function()

'''
No exemplo acima, a funcao internal_function acessa e modifica a variavel external_var da funcao externa externa_function.
A palavra-chave nonlocal permite que a funcao interna modifique a variavel do escopo externo, sem a necessidade de declará-la como global.

Se voce tentar modificar a variavel external_var sem usar nonlocal, o Python criara uma nova variavel local com o mesmo nome dentro da funcao interna, deixando a variavel externa inalterada.

'''