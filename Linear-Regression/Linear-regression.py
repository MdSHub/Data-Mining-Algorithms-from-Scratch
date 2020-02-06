
import matplotlib.pyplot as plt

def getData(filename):
    with open(filename) as file:
        data = file.read()
        data = [[float(j) for j in i.split(',')] for i in data.split('\n')]
        return data

data = getData('data1.txt')
data

x = []
y = []
for i in range(len(data)):
    x.append(data[i][0])
    y.append(data[i][1])
    
plt.scatter(x,y)

def cal(n, xs, ys, xxs, yys, xys):
    b = (n * xys - xs * ys) / (n * xxs - xs * xs)
    a = ys / n - b * xs / n
    return (a, b)

def regLinear(data):
    xs, ys, xxs, yys, xys = 0, 0, 0, 0, 0
    for i in data:
        xs += i[0]
        ys += i[1]
        xxs += i[0] * i[0]
        yys += i[1] * i[1]
        xys += i[0] * i[1]
    a, b = cal(len(data), xs, ys, xxs, yys, xys)
    return a, b

a, b = regLinear(data)
print(f'{a} + ({b})x')

def predict(x):
    return a + b*x

px = []
py = []

for i in range(12):
    px.append(i)
    py.append(a + b*i)

    
pdx = [1,3,6,7,9]
pdy = []

for i in range(len(pdx)):
    pdy.append(a + b*pdx[i])
print(pdy)

plt.plot(px, py)
plt.scatter(x,y)
plt.scatter(pdx,pdy)
