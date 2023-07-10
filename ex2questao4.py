valor_da_compra = float(input("Valor da compra: "))

valor_do_frete = float(input("Valor do frete: "))

cadastro_cliente = input("O cliente é cadastrado? “s” (sim) ou “n” (não) ")
if cadastro_cliente == "s" or valor_da_compra + valor_do_frete >= 100:
     print("Você tem direito a desconto.")
else:
     print("Cadastre-se para receber o cupom de desconto.")