print('Seja bem vindo a loja de Victor Ramalho Dias')

valorDoPedido = float(input("Valor do Pedido: R$"))
quantidadeParcelas  = int(input("Quantidade de Parcelas: "))

if quantidadeParcelas < 1:
    print("Erro na quantidade de parcelas!")
elif quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas < 6:
    juros = 0.04
elif quantidadeParcelas < 9:
    juros = 0.08
elif quantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32
if quantidadeParcelas >= 1:
    valorDaParcela = valorDoPedido * (1 + juros)/quantidadeParcelas
    valorTotalParcelado = valorDaParcela * quantidadeParcelas
    print(f'O valor dividido em {quantidadeParcelas} parcela(s) é de R${valorDaParcela:.2f}\nE o valor total é de R${valorTotalParcelado}')
