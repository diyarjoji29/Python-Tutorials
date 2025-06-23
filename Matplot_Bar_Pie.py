import matplotlib.pyplot as plt

classes=['I','II','III','IV','V','VI','VII','VIII','IX','X']
strength=[30,29,28,23,27,31,32,21,22,26]

plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.bar(classes,strength,color='lightcoral')
plt.title("Class Strengths Bar Plot")
plt.xlabel("Classes")
plt.ylabel("Strength")
plt.grid(axis='y',linestyle="--",alpha=0.25)
plt.tight_layout()

plt.subplot(1,3,2)
plt.title("Pie Plot")
pie_colors=["wheat","lightgreen","yellow","orange","lavender","coral","lightcyan","lightpink","seashell","plum"]
plt.pie(strength,labels=classes,colors=pie_colors,autopct="%1.1f%%")
plt.tight_layout()

plt.subplot(1,3,3)
plt.barh(classes,strength,color='lightgreen')
plt.title("Class Strengths Horizontal Bar Plot")
plt.xlabel("Classes")
plt.ylabel("Strength")
plt.grid(axis='x',linestyle="--",alpha=0.25)
plt.tight_layout()

plt.show()
