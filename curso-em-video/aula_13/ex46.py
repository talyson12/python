from time import sleep
print('-=' * 20)
print('{:^40}'.format('Festival de fogos de artifício'))
print('-=' * 20)
sleep(1)
print('Começando!')
sleep(1)
for c in range(10, -1, -1):
    print(c, end=' > ')
    sleep(1)
print('FIM.')