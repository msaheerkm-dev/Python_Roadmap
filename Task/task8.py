x=[1,2,3,4,5]
y=[2,4,5,4,5]

x_mean=sum(x)/len(x)
y_mean=sum(y)/len(y)

numer=0
denom=0
for i in range(len(x)):
    numer+=(x[i]-x_mean)*(y[i]-y_mean)
    denom+=(x[i]-x_mean)**2

m=numer/denom
print(m)

c=y_mean-m*x_mean
print(c)

def prediction(new_x):
    return c+m*new_x

def mse():
    total=0
    for i in range(len(x)):
        ypred=prediction(x[i])
        total+=(y[i]-ypred)**2
        return total/len(x)
    
print(mse())