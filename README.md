# calculadora_financeira
Repositório referente a implementação de uma calculadora financeira em python

Foi implementado:

Juros simples
    * Valor Futuro                      VF = VP*(1+(i*n))
    * Valor Presente                    VP = VF/(1+(i*n))
    * Tempo                              n = ((VF/VP)-1)/i
    * Taxa de Juros     	             i = ((VF/VP)-1)/n
    * Desconto Simples Racional          Dr = N - A    

Juros 
    * Valor Futuro                    	VF = VP*((1+i)^n)
    * Valor Presente                  	VP = VF/((1+i)^n)
    * Tempo                           	n = Log(VF/VP) / Log(1+i)
    * Taxa de Juros                   	i = [((VF/VP) ^ (1/n))-1]*100

Taxas e Periodos
    * Taxa efetiva                      i = ic/(1-ic*n)
    * Taxa desconto comercial           ic = i/(1+i*n)
    * Taxa anual               	        ia = ((1+ip)^n)-1
    * Periodo m-a                       i = ((1+i)^n)-1
    * Periodo a-m                       i = ((1+i)^1/n)-1

Ainda será implementado:
    * Amortização
    * VPL
     