# pyhon program to add matrix using nested list comprehension

x = [[12,7,3],
     [4,9,7],
     [7,9,4]]

y = [[5,8,1],
     [5,7,9],
     [3,7,9]]

result = [[x[i][j]+y[i][j] for j in range (len(x[0]))] for i in range(len(x))]

for r in result:
    print(r)