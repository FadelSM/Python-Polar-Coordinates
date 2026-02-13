import cmath

def solve():
    # Read the input string and convert it to a complex number
    # Example: "1+2j"
    z = complex(input())
    
    # Calculate modulus (r) and phase (phi)
    r = abs(z)
    phi = cmath.phase(z)
    
    # Alternatively, you could use:
    # r, phi = cmath.polar(z)
    
    print(r)
    print(phi)

if __name__ == "__main__":
    solve()
