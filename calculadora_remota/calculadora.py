class calculadora:
    
    def calc( operando, value1, value2):
        match operando:
            case "add" :
                result =  str(value1 + value2)
                return result
            case "sub" :
                result = str(value1 - value2 )
                return result
            case "mult" :
                result = str(value1 * value2) 
                return result
            case "div" :
                    if (value2 != 0):
                        result  = str(float(value1) / float(value2))
                        return result
                    else:
                        resutl =   "Não aceito divisao por zero"
                        return result