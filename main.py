print('Você está se sentindo mau? Ok... vamos ver se você está com febre!')
temp = float(input('Quanto está sua temperatura?'))

if temp >= 0.0 and temp <= 36.0:
  print('Hiportemia!')

elif temp >= 36.1 and temp <= 37.2:
  print('Saudável!')

elif temp >= 37.3 and temp <= 37.8:
  print('Febril!')

elif temp >= 37.9 and temp <= 38.9:
  print('Febre!')

elif temp >= 39 and temp <= 39.4:
  print('Febre alta!')

elif temp >= 39.1:
  print('Hipertermia!')


  



