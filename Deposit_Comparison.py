per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму, которую вы хотите положить: '))
deposit_tkb = money * per_cent['ТКБ'] / 100
deposit_skb = money * per_cent['СКБ'] / 100
deposit_vtb = money * per_cent['ВТБ'] / 100
deposit_sber = money * per_cent['СБЕР'] / 100
deposit = (deposit_tkb, deposit_skb, deposit_vtb, deposit_sber)
print(deposit)
print(f'Максимальная сумма, которую вы можете заработать — {max(deposit)}')
