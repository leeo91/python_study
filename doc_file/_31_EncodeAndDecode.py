s = '伟大的中国梦'
scode_gbk = s.encode('gbk')
print(scode_gbk)
scode_utf8 = s.encode('utf-8')
print(scode_utf8)

s2 = '耶๑'
# errors -> ignore/strict/replace
scode = s2.encode('gbk', errors='replace')
print(scode)

print(bytes.decode(scode_gbk, 'gbk'))
print(bytes.decode(scode_utf8, 'utf-8'))
print(bytes.decode(scode, 'gbk', errors='ignore'))
