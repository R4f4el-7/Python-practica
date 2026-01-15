daw2 = {
  "estudiante1" : {
    "name" : "Emil",
    "nota" : 2
  },
  "estudiante2" : {
    "name" : "Tobias",
    "nota" : 8
  },
  "estudiante3" : {
    "name" : "Linus",
    "nota" : 4
  }
}
for x, obj in daw2.items():
  print(x)
  for clave, valor in obj.items():
    if(clave == "nota" and valor < 5):
      valor = 5
    print(clave + ':', valor)