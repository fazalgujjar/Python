number = int(input('Please enter a number to factor!'))
if number < 0:
  print('Please enter positive integer')
else:
  f = 1
  for i in range( 1, number+1):
    f = f*i
  print(f'Fectorial of {number} is {f}')
