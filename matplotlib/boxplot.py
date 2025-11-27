import matplotlib.pyplot as plt

c1=[11,12,13,14,15,16,17,18,45,56]
c2=[21,22,23,24,25,26,27,28,43,57]
c3=[31,32,33,34,35,36,37,38,46,53]
test=[c1,c2,c3]
plt.boxplot(test,patch_artist=True,notch=True)
plt.style.use('dark_background')
plt.grid()
plt.show()