def main():
    #escribe tu código abajo de esta línea
    b = int(input())
    lista = []
    i = 0
    if b>0 :
        while i<b :
            valor = input()
            lista.append(valor)
            i = i+1
        print(lista)
        noduplicados = []
        for i in lista :
            if i not in noduplicados:
                noduplicados.append(i)
        print(noduplicados)
    else:
        print('Error')

if __name__=='__main__':
    main()
