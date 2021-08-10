import numpy as np
from sklearn.linear_model import LinearRegression

quantidade = int(input("Informe a quantidade de variáveis do modelo: "))
x_ = list(range(0,quantidade))
y_ = list(range(0,quantidade))

print("Informe as ", quantidade, " variáveis dependentes: ")
for n in range(0, quantidade):
    print("Informe o valor ", n+1)
    y_[n] = int(input())

print("Informe as ", quantidade, " variáveis independentes: ")
for n in range(0, quantidade):
    print("Informe o valor ", n+1)
    x_[n] = int(input())

print("Informe o valor que quer prever ")
prev = list(range(0,1))
prev[0] = int(input())

x_ = np.asarray(x_)
x_ = x_.reshape(-1,1)
y_ = np.asarray(y_)

modelo = LinearRegression()
modelo.fit(x_,y_)

prev = np.asarray(prev)
prev = prev.reshape(-1,1)

resp = modelo.predict(prev.reshape(-1,1))
print("Resultado da Previsão: ", resp)