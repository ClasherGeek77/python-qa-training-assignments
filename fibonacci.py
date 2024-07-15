def main():
    try:
        limit = int(input("Enter the number of Fibonacci terms: "))
        fibonacci_numbers = fibonacci(limit)
        
        print(f"Fibonacci numbers of length {limit}:")
        print(', '.join(map(str, fibonacci_sequence)))
        
    except ValueError:
        print("wrong input!")
    
if __name__ == "__main__":
    main()
