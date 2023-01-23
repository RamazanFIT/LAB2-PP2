input_1 = int(input())

massive_bool = input_1*[True]
cnt = 2 



while(cnt < pow(input_1, 0.5)):
    if(massive_bool[cnt]):
        for i in range(pow(cnt, 2), input_1, cnt):
            massive_bool[i] = False;

    cnt += 1

for i in range(2, input_1):
    if(massive_bool[i]): 
        print(i, end=' ')

        
'''Решето Эратосфена'''

# print("HI")
# exit()
# print(pow(2, 2))