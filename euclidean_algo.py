# python program to find hcf or gcd using euclidean algorithm

# function to find hcf using the euclidean algorithm

def compute_hcf (x,y):
    while (y):
        x,y = y , x % y
    return x
hcf = compute_hcf(300,400) 
print("the hcf is ", hcf)   