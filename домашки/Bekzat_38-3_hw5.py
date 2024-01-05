
data = ('O!', 'Megacom', '0705', 'Beeline', '0550', '0770', 'Katel', '0510', 'Fonex', '0543')
designations = []
codes = []

for operators in data:
    if operators.isnumeric():
        codes.append(operators)
    else:
        designations.append(operators)

operators = dict()
index = 0
print(designations, codes)
while index < len(codes):
    operators[designations[index]] = {codes[index],}
    index += 1

del operators['Katel']
del operators['Fonex']
operators['O!'].update(['0705', '0735'])
operators['Megacom'].update(['0550', '0510', '0543'])
operators['Beeline'].update(['0222', '0220'])
for designations, codes in operators.items():
    print(f'{designations} - {codes}')