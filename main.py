from binwfc import Pattern, Wave

pat = Pattern("0010-")

print(pat.check("00100"))
print(pat.check("0010"))

print(''.join([str(i) for i in Wave(15, [pat], "00010").collapse()]))
