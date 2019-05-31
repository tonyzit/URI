def impostos(porcentagem, salario):
    imposto= porcentagem*salario
    if imposto!=0:
        return imposto
    else:
        mensagem = "Isento"
        return mensagem

def main():
    imposto=0
    salario = float(input())
    if salario <= 2000.00:
        imposto = impostos(0, salario)
        print(imposto)
    else:
        salario = salario-2000
        if salario > 1000:
            salario = salario - 1000
            imposto = imposto + impostos(0.08, 1000)
            if salario > 1500:
                salario = salario - 1500
                imposto = imposto + impostos(0.18, 1500)
                if salario != 0:
                    imposto = imposto + impostos(0.28, salario)
            else:
                imposto = imposto + impostos(0.18, salario)
        else:
            imposto = imposto + impostos(0.08, salario)
        print("R$ {:.2f}".format(imposto))

main()