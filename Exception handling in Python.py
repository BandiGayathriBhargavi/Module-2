# Exception handling in Python manage runtime errors safely without crashing
try:
    # Code that might cause an error
    num = int(input("Enter a divisor: "))
    result = 10 / num
except ZeroDivisionError:
    # Runs ONLY if a ZeroDivisionError occurs
    print("Error: You cannot divide by zero.")
except ValueError:
    # Runs ONLY if input cannot be cast to an integer
    print("Error: Please enter a valid number.")
else:
    # Runs ONLY if the try block succeeds without errors
    print(f"Success! The result is {result}")
finally:
    # ALWAYS runs, regardless of what happened above
    print("Cleaning up resources and finalizing execution.")
