"""
<p>给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照<strong><span style="color:#ff0000;">字典序升序排列</span></strong>(注意key可能是字符串）。</p><p>例如：a={1:1,2:2,3:3}, 则输出：1,2,3</p>
"""
c = ','
a ={2:1, 1:2, 3:3}
b = []

for i in a.keys():
    z = str(i)
    b.append(z)
b.sort()
d= c.join(b)
print(d)







