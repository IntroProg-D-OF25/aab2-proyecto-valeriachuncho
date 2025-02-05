import datetime

# Configuración inicial
FECHA_INICIO = datetime.date(2025, 8, 30)
FECHA_FIN = datetime.date(2025, 9, 8)
PRECIOS = {"normal": 5.0, "especial": 10.0}
PROMOCIONES = {"especial": {"jueves": 8.0, "viernes": 9.0, "sábado": 9.0}}
asistencia = []  # Lista para registrar asistencia a funciones especiales
ventas = []  # Lista para registrar todas las ventas

# Función para validar la fecha de la feria
def validar_fecha(fecha):
    return FECHA_INICIO <= fecha <= FECHA_FIN

# Función para comprar boletos
def comprar_boletos(tipo, fecha, cantidad):
    if not validar_fecha(fecha):
        print("Fecha fuera del rango de la feria.")
        return
    
    if tipo not in PRECIOS:
        print("Tipo de entrada no válido.")
        return
    
    precio = PRECIOS[tipo]
    if tipo == "especial":
        dia_semana = fecha.strftime("%A").lower()
        if dia_semana in PROMOCIONES[tipo]:
            precio = PROMOCIONES[tipo][dia_semana]
    
    total = precio * cantidad
    ventas.append({"tipo": tipo, "fecha": fecha, "cantidad": cantidad, "total": total})
    
    if tipo == "especial":
        asistencia.append({"fecha": fecha, "cantidad": cantidad})
    
    print(f"Compra realizada. Total a pagar: ${total:.2f}")

# Función para generar estadísticas
def generar_estadisticas():
    total_ventas = sum(venta["total"] for venta in ventas)
    total_boletos = sum(venta["cantidad"] for venta in ventas)
    asistencia_por_dia = {}
    for registro in asistencia:
        fecha = registro["fecha"]
        if fecha not in asistencia_por_dia:
            asistencia_por_dia[fecha] = 0
        asistencia_por_dia[fecha] += registro["cantidad"]
    
    print("\nEstadísticas de la feria:")
    print(f"Total de boletos vendidos: {total_boletos}")
    print(f"Total de ingresos: ${total_ventas:.2f}")
    print("Asistencia a funciones especiales por día:")
    for fecha, cantidad in asistencia_por_dia.items():
        print(f"  {fecha}: {cantidad} personas")

# Menú principal
def menu():
    while True:
        print("\nSistema de Gestión de Entradas - Feria Internacional de Loja")
        print("1. Comprar boletos")
        print("2. Generar estadísticas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tipo = input("Ingrese tipo de entrada (normal/especial): ").lower()
            fecha_str = input("Ingrese fecha (YYYY-MM-DD): ")
            cantidad = int(input("Ingrese cantidad de boletos: "))
            fecha = datetime.date.fromisoformat(fecha_str)
            comprar_boletos(tipo, fecha, cantidad)
        elif opcion == "2":
            generar_estadisticas()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
menu()
