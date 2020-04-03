def test(number):
    # 在函数内部再定义一个函数， 而且这个函数用到了外边函数的变量，那么将这个函数以及用到的变量成为闭包
    def test_in(number_in):
        print('in test_in 函数， number_in is {0}'.format(number_in))

        return number_in+number

    # 其实这里返回的就是闭包的结果
    return test_in


# 给test函数赋值， 这个20就是给参数number
ret = test(20)

print(ret)

# 注意这个100其实给参数number_in
print(ret(100))

# 注意这个200其实是给参数number_in
print(ret(200))



