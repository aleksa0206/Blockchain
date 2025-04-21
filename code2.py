from code1 import Blockchain, Block, Transaction 

its_coin = Blockchain()

its_coin.view()

its_coin.create_transaction(Transaction('adres1','adres2',75))
its_coin.create_transaction(Transaction('adres2','adres1',74))

print("Start minning...")
its_coin.mine_pending_transaction('Miner address')

its_coin.view()

balance = its_coin.get_balance_of_address('Miner address')
print('Balance of miners wallet: ', balance)

print('Do again minning , for winning reward...')

its_coin.mine_panding_transactions('minner_address')
balance = its_coin.get_balance_of_address('minner_address')
print("Balance of wallet after another minning: ", balance)

its_coin.view()