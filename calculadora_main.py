import math
import time
import os

"""
Universidade Federal de Uberlândia - Campus Monte Carmelo
Faculdade de Computação - Sistemas de Informação
Matemática financeira - Prof(a) Mara Alves Soares
Phelipe Rodovalho Santos

CODIGO FONTE - CALCULADORA FINANCEIRA
"""


def cls():  # limpando o terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_ini():
    cls()
    print("\n__________________ Calculadora financeira __________________\n")
    print(''' Escolha o que deseja calcular
        [ 1 ] Juros Simples
        [ 2 ] Juros Compostos
        [ 3 ] Taxas e conversões
        [ 4 ] Calcular o Valor Presente Líquido - VPL
        [ 5 ] Amortização - Financiamento SAC
        [ 0 ] Sair
        ''')

    return int(input(' Digite a Opção: '))


def main():
    while (True):
        o = menu_ini()
        cls()
        print(o)

        if o == 1:  # Juros Simples
            print("_________________ Juros Simples _________________")
            print(''' Escolha o tipo de operaçao que deseja fazer
            [ 1 ] Calcular o Valor Futuro                    	VF = VP*(1+(i*n))
            [ 2 ] Calcular o Valor Presente                  	VP = VF/(1+(i*n))
            [ 3 ] Calcular o Tempo                           	n = ((VF/VP)-1)/i
            [ 4 ] Calcular a Taxa de juros                    	i = ((VF/VP)-1)/n
            [ 5 ] Calcular o Desconto Simples Racional          Dr = N - A               	
            [ 9 ] Voltar
            [ 0 ] Sair''')

            op = int(input(' Informe a Opção: '))
            cls()

            if op == 1:  # Calcular o Valor Futuro
                print("_________________ Calcular o Valor Futuro _________________")
                print('\n A formula utilizada para esta conta é  VF = VP*(1+(i*n)) \n')
                VP = float(input('Informe o valor presente (VP): '))
                n = float(input('Informe o tempo em dias (n): '))
                i = float(input('Informe a taxa (i): '))

                i = i / 100  # convertendo a taxa para valor em porcentagem
                n = n/30  # convertendo o tempo meses
                VF = VP * (1 + (i * n))

                print(' O resultado do valor fururo é: {:.2f}'.format(VF))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 2:  # Calcular o Valor Presente
                print("_________________ Calcular o Valor Presente _________________")
                print(
                    '\n A formula utilizada para esta conta é  VP = VF/(1+(i*n)) \n')
                vf = float(input(' Informe o valor Futuro (VF): '))
                n = float(input(' Informe o tempo em dias (n): '))
                i = float(input(' Informe a taxa (i): '))

                i = i / 100  # convertendo a taxa para valor em porcentagem
                n = n/30  # convertendo o tempo meses
                vp = vf/(1 + (i * n))
                print(' O resultado do valor Presente é: {:.2f}'.format(vp))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 3:  # Calcular o Tempo
                print("_________________ Calcular o Tempo _________________")
                print(
                    '\n A formula utilizada para esta conta é  n = ((VF/VP)-1)/i \n')
                VF = float(input(' Informe o valor Futuro (VF): '))
                VP = float(input(' Informe o valor Presente (VP): '))
                i = float(input(' Informe a taxa (i): '))

                i = i / 100  # convertendo a taxa para valor em porcentagem
                n = (((VF / VP) - 1) / i)
                print('O tempo utilizado foi: {:.2f}'.format(n))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 4:  # Calcular a Taxa de juros
                print("_________________ Calcular a Taxa de Juros _________________")
                print('\n A formula utilizada para esta conta é  i = ((VF/VP)-1)/n \n')
                vf = float(input(' Informe o valor Futuro (VF): '))
                vp = float(input(' Informe o valor Presente (VP): '))
                n = float(input(' Informe o tempo em dias (n): '))
                n = n/30  # convertendo o tempo meses

                i = ((vf/vp)-1)/n
                i = i*100
                print(' A taxa de juros utilizada foi:{:.2f}%'.format(i))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
                \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 5:  # Calcular o Desconto Simples Racional ou Por Dentro
                print(
                    "_________________ Calcular o Desconto Simples Raconal _________________")
                print(
                    '\n A formula utilizada para esta conta é  Dr = N - A \n')
                a = float(input(' Informe o valor Atual (A): '))
                n = float(input(' Informe o valor Nominal (N): '))

                dr = n - a
                print(' O desconto simples racional foi de:{:.2f}'.format(dr))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 9:  # Voltar
                main()

            elif op == 0:  # Sair
                sair()

        elif o == 2:  # Juros Compostos
            print("_________________ Juros Compostos _________________")
            print(''' Escolha o tipo de operaçao que deseja fazer
                [ 1 ] Calcular o valor Futuro                    	VF = VP*((1+i)^n)
                [ 2 ] Calcular o valor Presente                  	VP = VF/((1+i)^n)
                [ 3 ] Calcular o Tempo                           	n = Log(VF/VP) / Log(1+i)
                [ 4 ] Calcular a Taxa de Juros                   	i = [((VF/VP) ^ (1/n))-1]*100
                [ 9 ] Voltar
                [ 0 ] Sair''')

            op = int(input('\n Informe a Opção: '))
            cls()

            if op == 1:  # Calcular o valor Futuro
                print("_________________ Calcular o valor Futuro _________________")
                print(
                    '\n A formula utilizada para esta conta é  VF = VP*((1+i)^n) \n')
                vp = float(input(' Informe o valor Presente (VP): '))
                n = float(input(' Informe o tempo em dias (n): '))
                i = float(input(' Informe a taxa (i): '))

                i = i / 100  # convertendo a taxa para valor em porcentagem
                n = n/30  # convertendo o tempo meses
                vf = vp * (1 + i) ** n
                print(' O resultado do valor fururo é: {:.2f}'.format(vf))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
                    \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 2:  # Calcular o valor Presente
                print("_________________ Calcular o valor Presente _________________")
                print('\n A formula utilizada para esta conta é  VP = VF/((1+i)^n) \n')
                vf = float(input(' Informe o valor Futuro (VF): '))
                n = float(input(' Informe o tempo em dias (n): '))
                i = float(input(' Informe a taxa (i): '))

                i = i / 100  # convertendo a taxa para valor em porcentagem
                n = n/30  # convertendo o tempo meses
                vp = vf / ((1 + i) ** n)
                print(' O valor presente é: {:.4f}'.format(vp))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 3:  # Calcular o Tempo
                print("_________________ Calcular o Tempo _________________")
                print(
                    '\n A formula utilizada para esta conta é  n = Log(VF/VP) / Log(1+i) \n')
                vf = float(input(' Informe o valor Futuro (VF): '))
                vp = float(input(' Informe o valor Presente (VP): '))
                i = float(input(' Informe a taxa (i): '))

                i = i / 100  # convertendo a taxa para valor em porcentagem
                log1 = math.log(vf/vp)  # calculando Log(VF/VP)
                log2 = math.log(1+i)  # calculando Log(1+i)
                n = log1 / log2
                print(' O tempo utilizado foi de: {:.4f}'.format(n))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 4:  # Calcular a Taxa de Juros
                print("_________________ Calcular a Taxa de Juros _________________")
                print(
                    '\n A formula utilizada para esta conta é  i = [((VF/VP) ^ (1/n))-1]*100 \n')
                vf = float(input(' Informe o valor Futuro (VF): '))
                vp = float(input(' Informe o valor Presente (VP): '))
                n = float(input(' Informe o tempo em dias (n): '))
                n = n/30  # convertendo o tempo meses

                i = (((vf/vp) ** (1/n))-1)*100
                print(' A taxa utilizada foi de: {:.2f}%'.format(i))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 9:  # Voltar
                main()

            elif op == 0:  # Sair
                sair()

        elif o == 3:  # Taxas
            print("_________________ Taxas _________________")
            print(''' Escolha o tipo de operaçao que deseja fazer
                [ 1 ] Calcular Taxa efetiva                         i = ic/(1-ic*n)
                [ 2 ] Calcular Taxa desconto comercial              ic = i/(1+i*n)
                [ 3 ] Calcular Taxa anual               	        ia = ((1+ip)^n)-1
                [ 4 ] Periodo m-a                                   i = ((1+i)^n)-1
                [ 5 ] Periodo a-m                                   i = ((1+i)^1/n)-1
                [ 9 ] Voltar
                [ 0 ] Sair''')

            op = int(input('\n Informe a Opção: '))
            cls()

            if op == 1:  # Calcular Taxa efetiva
                print("_________________ Calcular Taxa efetiva  _________________")
                print(
                    '\n A formula utilizada para esta conta é i = ic/(1-ic*n) \n')
                ic = float(input(' Informe a Taxa comercial (ic): '))
                n = float(input(' Informe o tempo em dias (n): '))
                ic = ic/100  # transformando em taxa unitaria
                n = n/30  # transformando em meses
                i = (ic/(1-(ic*n)))*100
                print(' O resultado da taxa efetiva é: {:.4f}'.format(i))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 2:  # Calcular Taxa desconto comercial
                print(
                    "_________________ Calcular Taxa desconto comercial _________________")
                print(
                    '\n A formula utilizada para esta conta é ic = i/(1+i*n) \n')
                i = float(input(' Informe a taxa efetiva (i): '))
                n = float(input(' Informe o tempo em dias (n): '))
                i = i/100  # transformando em taxa unitaria
                n = n/30  # transformando em meses
                ic = (i/(1+i*n))*100
                print(
                    ' O resultado da taxa desconto comercial é: {:.2f}'.format(ic))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 3:  # Calcular Taxa anual
                print("_________________ Calcular Taxa anual _________________")
                print(
                    '\n A formula utilizada para esta conta é  ia = ((1+ip)^n)-1 \n')

                ip = float(input(' Informe a taxa (ip): '))
                n = float(input(' Informe o valor do Tempo (n): '))

                ip = ip/100
                ia = ((1+ip) ** n)-1
                ia = ia*100
                print(' O tempo utilizado foi:{:.4f}'.format(ia))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 4:  # Periodo m-a
                print("_________________ Calcular Periodo m-a _________________")
                print(
                    '\n A formula utilizada para esta conta é  i = ((1+i)^n)-1\n')
                i = float(input(' Informe o valor (i) '))
                n = float(input(' Informe o valor (n): '))

                i = ((1+i)**n)-1
                print(' O tempo utilizado foi:{:.2f}'.format(i))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 5:  # Periodo a-m
                print("_________________ Calcular Periodo a-m _________________")
                print(
                    '\n A formula utilizada para esta conta é  i = ((1+i)^1/n)-1 \n')
                i = float(input(' Informe o valor (i) '))
                n = float(input(' Informe o valor (n): '))
                i = i/100
                i = ((1+i)**(1/n))-1
                i = i*100
                print(' O tempo utilizado foi:{:.4f}'.format(i))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 9:  # Voltar
                main()

            elif op == 0:  # Sair
                sair()

        elif o == 4:  # Valor Presente Líquido - VPL
            print("_________________ Valor Presente Líquido - VPL _________________\n")
            print("Calcular o investimento inicial")
            print('\n A formula utilizada é FC = Somatório(FC / (1+k)^j) \n')
            n = int(
                input("Informe a quantidade de períodos que serão analisados (n): "))
            #j = int(input("Informe o número do período analisado (J): "))
            k = float(input("Informe o valor do custo de capital (K): "))
            k = k / 100  # convertendo a taxa para valor em porcentagem
            cls()
            inv = 0.0
            print("Somatório de períodos...")
            a = 1
            while(a != n+1):
                fc = float(
                    input("Informe o valor do fluxo de caixa no período (FC): "))
                aux = (1 + k)**a
                print("\naux k: ", aux, k)
                inv += fc/aux
                print("\naux = ", inv)
                print(f"Período {a}, Resultado: {inv}\n".format(n=n, inv=inv))
                a += 1
            not input('''Aperte enter para Continuar''')
            cls()

            print("Resultado do Investimento inicial = ", inv)
            fc = inv

            print(
                "\nCalcular o VPL, Fórmula (((FC) + (VR / (1 + k) ^ t)) - inv)")
            inv = int(
                input("Informe o valor do Inv: "))
            vr = float(input("Informe o valor residual do projeto (VR): "))

            t = int(input("Informe o tempo: "))

            k = float(input("Informe o valor do custo de capital (K): "))
            k = k/100

            print("O valor do investimento inicial já calculado é de: ", fc)

            not input('''Aperte enter para Continuar''')
            cls()
            vpl = 0.0
            a = 1
            print("Somatório de períodos...")
            # (((FC) + (VR / (1 + k) ^ t)) - inv)

            result = (((fc) + (vr / (1 + k)**t)) - inv)

            print("\nResultado VPL = ", result)

            not input('''Aperte enter para Continuar''')
            cls()

            print("Resultado do VPL = ", vpl)
            if vpl > 0:
                print("VPL aprovado!\n")
            else:
                print("VPL reprovado!\n")

            not input(
                '''\n Se necessario salve o valor antes de proseguir pois ele será apagado\n Aperte enter para Continuar''')
            cls()
            main()

        elif o == 5:  # Amortização - Financiamento SAC
            print("_________________ Amortização - Financiamento SAC _________________")
            print(''' Escolha o tipo de operaçao que deseja fazer
                [ 1 ] Calcular a Amortização                  Amort = PV/n
                [ 2 ] Calcular os Juros                       J = (PV/n) * ((n - t + 1)*i)
                [ 3 ] Calcular o PMT                          PMT = (PV/n) * (1 + (n - t + 1 )*i)
                [ 4 ] Calcular o Saldo Devedor                SD = PV - (Amort * t)
                [ 9 ] Voltar
                [ 0 ] Sair''')

            op = int(input('\n Informe a Opção: '))
            cls()

            if op == 1:  # Calcular a Amortização
                print("_________________ Calcular a Amortização _________________")
                print(
                    '\n A formula utilizada para este calculo é Amort = VP/n \n')
                vp = float(input(' Informe o valor Presente (VP): '))
                n = float(input(' Informe o tempo em dias (n): '))
                n = n/30
                amort = vp/n
                print(' O resultado da amortização é: {:.4f}'.format(amort))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
                    \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 2:  # Calcular os Juros
                print("_________________ Calcular os Juros _________________")
                print(
                    '\n A formula utilizada para este calculo é J = (VP/n) * ((n - t + 1)*i) \n')
                vp = float(input(' Informe o valor Presente (VP): '))
                n = float(input(' Informe o tempo em dias (n): '))
                t = float(input(' Informe o valor de (t): '))
                i = float(input(' Informe a taxa (i): '))
                t = t/30
                i = i/100  # transformando em taxa unitaria
                n = n/30  # transformando em meses

                j = ((vp/n) * ((n - t + 1)*i))
                print(' O resultado dos Juros é: {:.4f}'.format(j))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
                    \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 3:  # Calcular o PMT
                print("_________________ Calcular o PMT _________________")
                print(
                    '\n A formula utilizada para este calculo é PMT = (VP/n) * (1 + (n - t + 1 )*i) \n')
                vp = float(input(' Informe o valor Presente (VP): '))
                n = float(input(' Informe o tempo em dias (n): '))
                t = float(input(' Informe o valor de (t): '))
                i = float(input(' Informe a taxa (i): '))
                t = t/30
                i = i/100  # transformando em taxa unitaria
                n = n/30  # transformando em meses

                pmt = ((vp/n) * (1 + (n - t + 1)*i))
                print(' O resultado dos Juros é: {:.4f}'.format(pmt))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
                    \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 4:  # Calcular o Saldo Devedor
                print("_________________ Calcular o Saldo Devedor _________________")
                print(
                    '\n A formula utilizada para este calculo é SD = VP - (Amort * t ) \n')

                opp = str(
                    input("Deseja calcular o valor da amortização nesse momento? (s/n)"))
                if opp == 's' or opp == 'S':
                    amort = amortiza()
                else:
                    amort = float(input(' Informe o valor da Amortização: '))

                vp = float(input(' Informe o Valor Presente (VP): '))
                t = float(input(' Informe o valor de (t): '))
                t = t/30
                print("\n amort", amort * t)

                sd = vp - (amort * t)
                print(' O resultado do Saldo Devedor é: {:.4f}'.format(sd))
                not input('''\n Se necessario salve o valor antes de proseguir pois ele será apagado
                    \n Aperte enter para Continuar''')
                cls()
                main()

            elif op == 9:  # Voltar
                main()

            elif op == 0:  # Sair
                sair()

        elif o == 0:  # SAIR
            sair()


def amortiza():
    print("_________________ Calcular a Amortização _________________")
    print(
        '\n A formula utilizada para este calculo é Amort = VP/n \n')
    vp = float(input('Informe o valor Presente (VP): '))
    n = float(input('Informe o tempo em dias (n): '))
    n = n/30
    amort = vp/n
    print(' O resultado da amortização é: {:.4f}'.format(amort))
    not input('''\n Aperte enter para Continuar o calculo do Saldo''')
    return amort


def sair():
    print("__________________ Calculadora financeira __________________")
    print('\n Matemática financeira - Prof(a) Mara Alves Soares')
    print('\n Criado por Phelipe Rodovalho Santos - Copyright 2022')

    time.sleep(4)

    exit()


print(main())
