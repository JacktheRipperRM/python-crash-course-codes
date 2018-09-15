# Python - it's so readable, the code basically just writes itself ;-)
#
with open('infile') as infile:
  with open('outfile', 'w') as outfile:
    for line in infile:
      fields = line.split('\t')
      outfile.write(','.join(fields))