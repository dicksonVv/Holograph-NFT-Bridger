import random

'''
	

     delay - your time (from and to) the break between wallets
     mode  -  0 -your networks (from and to which) ; 1 - search for nft by availability on the network and send it to your chosen network

     avax   /   bsc   /   polygon

     chain - from which network
     to - to which of the networks (selected randomly) - random.choice(['avax','polygon']) or to a specific network - just the network name 'avax'
    '''

delay = (10, 600)
mode = 1
chain = 'bsc'          #   avax   /   bsc   /   polygon
to = 'avax'     #random.choice(['ваша сеть','ваша сеть'])

info = {'avax':('https://snowtrace.io/tx/','https://rpc.ankr.com/avalanche'),
        'polygon':('https://polygonscan.com/tx/','https://polygon-rpc.com'),
        'bsc':('https://bscscan.com/tx/','https://bscrpc.com')}
