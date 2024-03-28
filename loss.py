import matplotlib.pyplot as plt

# 读取txt文件的前200行数据作为损失值
with open("loss.txt", "r") as file:
    lines = file.readlines()[:200]
    loss_values = [float(line.strip()) for line in lines]

# 绘制损失曲线
plt.plot(loss_values, color='red', linewidth=2)
plt.xlabel("Epoch",fontsize=16)
plt.ylabel("Loss",fontsize=16)
plt.title("Loss Curve",fontsize=16)
plt.grid(True)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
# 保存为loss.jpg文件
plt.savefig("loss.jpg")
plt.show()
