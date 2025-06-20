import matplotlib.pyplot as plt

classes=['I','II','III','IV','V','VI','VII','VIII','IX','X']
strength=[30,29,28,23,27,31,32,21,22,26]

plt.figure(figsize=(8,5))
plt.title("Class strengths")
plt.plot(classes,strength,marker="o",color='blue')
plt.grid(True,linestyle="--",alpha=0.2)
plt.xlabel("Classes")
plt.ylabel("Strength")
plt.show()