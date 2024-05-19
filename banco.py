saldo = 0
valor_total_sacado = 0
valor_total_depositado = 0
limite_saque_diario = 3
extrato = ''
while True:
    operacao = int(input('''
        Olá! Seja bem-vindo! Qual operação você deseja realizar?
        1 - Saque
        2 - Depósito
        3 - Extrato
        4 - Sair
        '''))

    if operacao == 1:
        valor_a_sacar = float(input('Qual o valor você deseja sacar? '))
        if valor_a_sacar > 500:
            print('Você não pode sacar valores iguais ou acima de R$500,00')
        elif limite_saque_diario > 0 and valor_a_sacar <= saldo:
            saldo -= valor_a_sacar
            valor_total_sacado += valor_a_sacar
            limite_saque_diario -= 1
            extrato += f'Saque de R${valor_a_sacar:.2f} \n'
            print('Operação de saque concluída com sucesso!')
        else:
            print('Operação de saque não concluída... Verifique o seu saldo ou o seu limite diário de saque.')

    if operacao == 2:
        valor_a_depositar = float(input('Qual o valor você deseja depositar? '))
        saldo += valor_a_depositar
        valor_total_depositado += valor_a_depositar
        extrato += f'Depósito de R${valor_a_depositar:.2f} \n'
        print(f'Valor R${valor_a_depositar} depositado com sucesso')

    if operacao == 3:
        if valor_total_sacado and valor_total_depositado == 0:
            print('Não foram realizadas movimentações')
        else:
            print(f'Saldo de R${saldo:.2f}')
        
    if operacao == 4:
        print('Volte sempre!')
        break;