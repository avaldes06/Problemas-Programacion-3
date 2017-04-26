class numeros:
    numero = 0

    def __init__(self,num):
        self.numero = num


    def parImpar(self):
        if (self.numero % 2) == 0:
           #Pares
            return 0
        else:
            #Impares
            return 1



