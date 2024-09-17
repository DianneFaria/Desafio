def calcula_fibonacci(num):
    fibonacci_sequencia = [0, 1]
    
    while fibonacci_sequencia[-1] < num:
        fibonacci_sequencia.append(fibonacci_sequencia[-1] + fibonacci_sequencia[-2])
    
    print(f"Sequência de Fibonacci até {num}: {fibonacci_sequencia}")
    
    if num in fibonacci_sequencia:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

numero = int(input("Informe um número: "))
calcula_fibonacci(numero)
