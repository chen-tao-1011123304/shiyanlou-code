"""
<p>给你一个字符串 a， 请你输出逆序之后的a。</p><p>例如：a=‘xydz’</p><p>则输出：zdyx</p>
"""
a = 'xydz'
b = ''
for i in a:
    b = i + b

print(b)





