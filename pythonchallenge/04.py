"""
<p>给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。</p><p>例如：a=‘xyzwd’</p><p>则输出:xzd</p>
"""
a = 'xyzwd'
c = ''
for i, j in enumerate(a):
    # 判断是不是奇数
    b = bool((i+1) % 2 == 1)
    if b:
        c += j

print(c)










