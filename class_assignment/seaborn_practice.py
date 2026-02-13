import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = sns.load_dataset("tips")
print(data.head())
sns.set_style("darkgrid")
sns.lineplot(x="size", y="total_bill", data=data)
plt.title("Line Plot")
plt.show()

# # 4. Bar Plot
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Bar Plot")
plt.show()

# # -------------------------------
# # 5. Scatter Plot
# # -------------------------------
# sns.scatterplot(x="total_bill", y="tip", data=data)
# plt.title("Scatter Plot")
# plt.show()

# # -------------------------------
# # 6. Histogram
# # -------------------------------
# sns.histplot(data["total_bill"], bins=10, kde=True)
# plt.title("Histogram")
# plt.show()

# # -------------------------------
# # 7. Box Plot
# # -------------------------------
# sns.boxplot(x="day", y="total_bill", data=data)
# plt.title("Box Plot")
# plt.show()

# # -------------------------------
# # 8. Violin Plot
# # -------------------------------
# sns.violinplot(x="day", y="total_bill", data=data)
# plt.title("Violin Plot")
# plt.show()

# # -------------------------------
# # 9. Count Plot
# # -------------------------------
# sns.countplot(x="day", data=data)
# plt.title("Count Plot")
# plt.show()

# # -------------------------------
# # 10. Pair Plot (VERY IMPORTANT)
# # -------------------------------
# sns.pairplot(data)
# plt.show()

# # -------------------------------
# # 11. Regression Plot
# # -------------------------------
# sns.regplot(x="total_bill", y="tip", data=data)
# plt.title("Regression Plot")
# plt.show()

# # -------------------------------
# # 12. Heatmap (Correlation)
# # -------------------------------
# corr = data.corr(numeric_only=True)

# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

# # -------------------------------
# # 13. KDE Plot
# # -------------------------------
# sns.kdeplot(data["total_bill"], fill=True)
# plt.title("KDE Plot")
# plt.show()

# # -------------------------------
# # 14. Hue Example
# # -------------------------------
# sns.scatterplot(x="total_bill", y="tip", hue="sex", data=data)
# plt.title("Scatter with Hue")
# plt.show()
print("✅ Seaborn practice completed successfully!")
 