# Python - it's so readable, the code basically just writes itself ;-)

with open("C:\Users\erajmuk\Desktop\PY\test_CA.log") as infile:
  with open("C:\Users\erajmuk\Desktop\PY\out.log", 'w') as outfile:
    for line in infile:
      fields = line.split('\t')
      outfile.write(','.join(fields))
