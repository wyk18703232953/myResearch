import matplotlib.pyplot as plt
import numpy as np

# 数据准备
complexities = ['linear', 'quadratic', 'constant', 'nlogn', 'logn', 'cubic', 'np']
accuracy = [82.77, 70.02, 64.22, 63.07, 57.40, 53.63, 45.27]
total_samples = [853, 657, 791, 796, 669, 606, 528]

# 创建图表
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [2, 1]})

# 1. 准确率条形图（排序后）
colors = ['#2E86AB' if x != max(accuracy) else '#A23B72' for x in accuracy]
bars = ax1.barh(complexities, accuracy, color=colors, edgecolor='black')
ax1.set_xlabel('Accuracy (%)', fontsize=12)
ax1.set_title('Model Performance by Complexity (Accuracy %)', fontsize=14, pad=15)
ax1.set_xlim([0, 100])
ax1.axvline(x=50, color='gray', linestyle='--', alpha=0.5)
ax1.invert_yaxis()

# 在条形图末端添加数值标签
for i, (bar, acc) in enumerate(zip(bars, accuracy)):
    ax1.text(acc + 1, bar.get_y() + bar.get_height()/2, 
             f'{acc}%', va='center', fontweight='bold')

# 2. 样本数量条形图
ax2.bar(complexities, total_samples, color='#F18F01', edgecolor='black')
ax2.set_ylabel('Total Samples', fontsize=12)
ax2.set_title('Total Samples per Complexity', fontsize=14, pad=15)
ax2.tick_params(axis='x', rotation=45)

# 在条形图顶部添加样本数标签
for i, (comp, samples) in enumerate(zip(complexities, total_samples)):
    ax2.text(i, samples + 20, str(samples), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()