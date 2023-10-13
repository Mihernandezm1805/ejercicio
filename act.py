sw=1
c=0
p=0
cc=0
precioC=0
precioP=0
precioCC=0

while(sw==1):
  print(" TIENDA DE ROPA ")
  print("1.- Camisetas ")
  print("2.- Pantalón ")
  print("3.- chaquetas ")
  print("4- finalizar compra ")
  print("5.- salir")
  op=int(input(" elija su opcion:\n"))
  if op==1:
    c=c+1
    precioC=c*2500
    print(f" Camisetas {c}\nPRECIO: ${precioC}")
  elif op==2:
    p=p+1
    precioP=p*5000
    print(f" Pantalón {p}\nPRECIO: ${precioP}")
  elif op==3:
    cc=cc+1
    precioCC=cc*8000
    print(f" Chaquetas {cc}\nPRECIO: ${precioCC}")
  elif op==4:
    if c==0 and p==0 and cc==0:
      print(" seleccione al menos 1 producto ")
    else:
      nombre=input(" ingrese su nombre ")
      print(" ======= Factura Tienda de Ropa =======")
      print(" prendas: ")
      if c!=0:
        print(f" Camisetas: {c}\nPRECIO: ${precioC}")
        print("-------------")
      if p!=0:
        print(f" Pantalón {p}\nPRECIO: ${precioP}")
        print("-------------")
      if cc!=0:
        print(f" Chaquetas: {cc}\nPRECIO: ${precioCC}")
        print("-------------")
      print(f"total ${precioC+precioP+precioCC}")
      print("-------------")
      print(f"¡Gracias {nombre} por su compra!")
      print("-------------")
      #limpiar valores
      c=0
      p=0
      cc=0
  elif op==5:
    print("hasta luego")
    sw=0
  else:
    print("opcion incorrecta")