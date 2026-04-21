#este es un programa para saber eldia de la semana
# dia = int(input('Introduzca u numero'))
# if(dia == 1):
#     print('Lunes')
# else:
#     if(dia == 2):
#         print('Martes')
#     else:
#         if(dia == 3):
#             print('Miercoles')
#         else:
#             if(dia == 4):
#                 print('Jueves')
#             else:
#                 if(dia == 5):
#                     print('viernes')
dia = int(input('INtroduzca un numero'))
match dia:
    case 1:
        print('Lunes')
    case 2:
        print('Martes')   
    case 3:
        print('MIercoles')  
    case 4:
        print('Jueves')
    case 5:
        print('Viernes')
        