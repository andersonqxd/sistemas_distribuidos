class interface:
    def menu():
        print("=" * 30)
        print(f"|{'OPERAÇÕES':^30}") #centraliza o conteudo do parametro na tela com ^
        print("=" * 30)
        print("|\t> add\n|\t> sub\n|\t> div\n|\t> mult")
        print("=" * 30)
        operacoes = ["add", "sub", "div", "mult"]
        ope = input("Escolha uma operação: ")
        expre = ""
        if ope == "add":
            expre = operacoes[0]
        elif ope == "sub":
            expre = operacoes[1]
        elif ope == "div":
            expre = operacoes[2]
        elif ope == "mult":
            expre = operacoes[3]

            
        num1 = str(input("Primeiro valor: "))
        num2 = str(input("Segundo valor: "))


        expre = expre + " " + num1 + " " + num2
        return expre
        