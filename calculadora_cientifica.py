import math
import re

def evaluar_expresion(expresion):
    try:
        # Reemplaza funciones y constantes matemáticas
        expresion = expresion.replace('^', '**')
        expresion = expresion.replace('√', 'math.sqrt')
        expresion = expresion.replace('π', 'math.pi')
        expresion = expresion.replace('e', 'math.e')
        
        # Expresiones regulares para funciones (ej: sin(30) -> math.sin(math.radians(30)))
        funciones = {
            'sin': 'math.sin(math.radians',
            'cos': 'math.cos(math.radians',
            'tan': 'math.tan(math.radians',
            'ln': 'math.log',
            'log': 'math.log10',
            'exp': 'math.exp'
        }
        
        for func, repl in funciones.items():
            expresion = re.sub(rf'{func}\((.+?)\)', rf'{repl}(\1)', expresion)
        
        # Evalúa la expresión de manera segura
        return eval(expresion, {'math': math, '__builtins__': None})
    
    except Exception as e:
        raise ValueError(f"Error en la expresión: {e}")

def calculadora_avanzada():
    print("\n=== CALCULADORA CIENTÍFICA AVANZADA ===")
    print("Instrucciones:")
    print("- Usa '+' , '-' , '*' , '/' , '^' (potencia), '√' (raíz)")
    print("- Funciones: sin(30), cos(45), tan(90), ln(10), log(100), exp(2)")
    print("- Constantes: π (pi), e (número de Euler)")
    print("- Ejemplo: 3*sin(45)^2 + √(16)/2")
    print("- Escribe 'salir' para terminar\n")
    
    while True:
        expresion = input("Ingresa una expresión matemática: ").strip().lower()
        
        if expresion == 'salir':
            print("¡Hasta luego!")
            break
        
        try:
            resultado = evaluar_expresion(expresion)
            print(f"Resultado: {resultado:.6f}")  # 6 decimales
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    calculadora_avanzada()