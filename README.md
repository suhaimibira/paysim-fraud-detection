# 💳 PaySim Fraud Detection – EDA & Tableau Dashboard

A quick 3.5-hour project exploring mobile money fraud using the PaySim synthetic dataset. This project focuses on detecting fraudulent transaction patterns through data cleaning, exploratory data analysis (EDA), and interactive Tableau visualizations.

---

## 📁 Project Structure
---

## 📌 Objective

To analyze financial transactions from the PaySim dataset and uncover trends that distinguish fraudulent transactions from legitimate ones. The project is designed to simulate how mobile money platforms can proactively detect fraud.

---

## 📊 Dataset

- **Source**: [Kaggle - PaySim Fraud Detection](https://www.kaggle.com/datasets/ealaxi/paysim1)
- **Records**: ~6 million transactions
- **Features**: transaction type, amount, origin/destination, balance info, fraud flags

---

## 🔍 Key Findings

- Fraudulent transactions occur **only in `TRANSFER` and `CASH_OUT`** types.
- Most flagged frauds are **not actually fraudulent**, showing a gap in detection precision.
- Fraudulent transactions tend to involve **large transaction amounts**.
- The total number of frauds is low (~0.13%), but their financial impact is high.

---

## 🛠 Tools Used

- **Python** – `pandas`, `matplotlib`, `seaborn` for data cleaning and EDA
- **Jupyter Notebook** – for interactive exploration
- **Tableau Desktop** – for building a clean, visual dashboard
- **GitHub** – for version control and showcasing the project

---

## 📈 Tableau Dashboard

The final dashboard summarizes:
- Total vs. fraudulent transaction counts
- Fraud by transaction type
- Distribution of transaction amounts
- KPIs: total frauds, total transactions, flagged vs. true fraud

> 📎 You can download and view the `.twbx` file in the `dashboard/` folder using Tableau Desktop.

---

## 🐍 Python Requirements

To run the notebook:

```bash
pip install pandas matplotlib seaborn jupyter
