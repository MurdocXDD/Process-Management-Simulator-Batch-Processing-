
import time

from itertools import cycle



# Función para validar la operación y realizarla

def realizar_operacion(operacion, a, b):

    if operacion == '+':

        return a + b

    elif operacion == '-':

        return a - b

    elif operacion == '*':

        return a * b

    elif operacion == '/':

        return a / b if b != 0 else "Error: División entre cero"

    elif operacion == '%':

        return a % b

    elif operacion == '**':

        return a ** b

    else:

        return "Operación no válida"



# Capturar los procesos desde el teclado

def capturar_procesos():

    procesos = []

    numero_programas = set()  # Para validar que el número de programa sea único



    while True:

        num_procesos = int(input("¿Cuántos procesos quieres introducir? "))



        for i in range(num_procesos):

            print(f"Capturando datos del proceso {i+1}:")

           

            nombre_programador = input("Nombre del programador: ")

           

            operacion = input("Operación a realizar (+, -, *, /, %, **): ")

            while operacion not in ['+', '-', '*', '/', '%', '**']:

                print("Operación no válida.")

                operacion = input("Operación a realizar (+, -, *, /, %, **): ")



            a = float(input("Introduce el primer número: "))

            b = float(input("Introduce el segundo número: "))



            tiempo_estimado = float(input("Tiempo máximo estimado (debe ser mayor a 0): "))

            while tiempo_estimado <= 0:

                print("El tiempo debe ser mayor a 0.")

                tiempo_estimado = float(input("Tiempo máximo estimado: "))



            numero_programa = int(input("Número de programa (debe ser único): "))

            while numero_programa in numero_programas:

                print("El número de programa ya existe.")

                numero_programa = int(input("Número de programa (debe ser único): "))

            numero_programas.add(numero_programa)



            # Guardar el proceso como un diccionario

            proceso = {

                "Nombre": nombre_programador,

                "Operacion": operacion,

                "a": a,

                "b": b,

                "Tiempo": tiempo_estimado,

                "NumeroPrograma": numero_programa

            }

            procesos.append(proceso)

       

        respuesta = input("¿Deseas capturar más procesos? (s/n): ")

        if respuesta.lower() != 's':

            break



    return procesos



# Mostrar el estado de los lotes

def mostrar_estado(lotes, lote_actual, procesos_terminados, tiempo_global):

    print(f"\n--- Estado Actual ---")

    print(f"Lotes pendientes: {len(lotes)}")

   

    print(f"\nLote en Ejecución (Lote {lote_actual + 1}):")

    for proceso in lotes[lote_actual]:

        print(f"  - Programa {proceso['NumeroPrograma']}: Tiempo Máximo Estimado {proceso['Tiempo']}s")



    print(f"\nProcesos Terminados:")

    for terminado in procesos_terminados:

        print(f"  - Programa {terminado['NumeroPrograma']}: {terminado['Operacion']} {terminado['a']} {terminado['Operacion']} {terminado['b']} = {terminado['Resultado']}")

   

    print(f"\nContador Global: {tiempo_global}s")



# Simular la ejecución de los lotes y procesos

def ejecutar_procesos(procesos):

    # Dividir los procesos en lotes de 4

    lotes = [procesos[i:i + 4] for i in range(0, len(procesos), 4)]

    lote_actual = 0

    tiempo_global = 0

    procesos_terminados = []



    while lote_actual < len(lotes):

        lote_en_ejecucion = lotes[lote_actual]



        # Ejecutar cada proceso del lote

        for proceso in lote_en_ejecucion:

            nombre = proceso["Nombre"]

            operacion = proceso["Operacion"]

            a = proceso["a"]

            b = proceso["b"]

            tiempo_estimado = proceso["Tiempo"]

            numero_programa = proceso["NumeroPrograma"]



            print(f"\nEjecutando proceso {numero_programa}...")

            tiempo_transcurrido = 0



            # Simulación del tiempo de ejecución del proceso

            while tiempo_transcurrido < tiempo_estimado:

                time.sleep(1)  # Simula 1 segundo de ejecución

                tiempo_transcurrido += 1

                tiempo_global += 1

                tiempo_restante = tiempo_estimado - tiempo_transcurrido

               

                print(f"  - Proceso {numero_programa} ({nombre})")

                print(f"    Operación: {operacion} {a} {operacion} {b}")

                print(f"    Tiempo transcurrido: {tiempo_transcurrido}s, Tiempo restante: {tiempo_restante}s")

                print(f"    Contador Global: {tiempo_global}s")



            # Calcular el resultado de la operación

            resultado = realizar_operacion(operacion, a, b)



            # Añadir a la lista de procesos terminados

            procesos_terminados.append({

                "NumeroPrograma": numero_programa,

                "Operacion": operacion,

                "a": a,

                "b": b,

                "Resultado": resultado

            })



        # Lote completado

        print(f"\nLote {lote_actual + 1} completado.")

        lote_actual += 1



        # Mostrar el estado actualizado

        mostrar_estado(lotes, lote_actual, procesos_terminados, tiempo_global)



    # Pausar al final para observar el resultado

    input("\nTodos los lotes han sido ejecutados. Presiona Enter para terminar...")



# Función principal

def main():

    print("Simulación de Procesamiento por Lotes")

    procesos = capturar_procesos()

    ejecutar_procesos(procesos)



# Ejecutar el programa

if __name__ == "__main__":

    main()