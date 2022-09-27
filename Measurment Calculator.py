weight_kg = input('Enter Weight Here (in KG): ')

weight_hg = int(weight_kg) * 10
weight_dag = int(weight_kg) * 100
weight_g = int(weight_kg) * 1000
weight_mg = int(weight_g) * 0.001

print('Hectograms: ' + str(weight_hg))
print('Decagrams: ' + str(weight_dag))
print('Grams: ' + str(weight_g))
print('Milligrams: ' + str(weight_mg))