import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ✅ Ensure images save to the visible 'files' directory
save_path = "/home/runner/workspace"   # Replit visible workspace path

data = {
  "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
  "Sales": [20000, 25000, 27000, 30000, 32000, 40000, 42000, 45000, 47000, 48000, 50000, 52000],
  "Profit": [4000, 5000, 5200, 5500, 6000, 7000, 7200, 7500, 7700, 8000, 8500, 8800],
  "Quantity": [120, 150, 160, 180, 200, 220, 240, 260, 270, 280, 290, 300]
}

df = pd.DataFrame(data)

# Create and save plots one by one
plt.figure(figsize=(8,4))
sns.lineplot(x="Month", y="Sales", data=df, marker="o", color="red")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(os.path.join(save_path, "monthly_sales.png"))
plt.close()

plt.figure(figsize=(8,4))
sns.scatterplot(x="Month", y="Profit", data=df, hue="Month", palette="viridis", s=100)
plt.title("Monthly Profit Scatter")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(os.path.join(save_path, "monthly_profit.png"))
plt.close()

plt.figure(figsize=(8,4))
sns.histplot(df["Profit"], kde=True, color="green")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(save_path, "profit_distribution.png"))
plt.close()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(os.path.join(save_path, "correlationn_matrix.png"))
plt.close()


print("✅ All charts saved successfully in Replit workspace folder!")
