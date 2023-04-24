def do_fizzbuzz(num:int):
    print("hello")
    for i in range(1,1+num):
        if i%3==0:
            print('fizz')
        else:
            print(f'{i}')
if __name__=='__main__':
    do_fizzbuzz(16)
