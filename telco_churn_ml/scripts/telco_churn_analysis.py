import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

username = "root" 
password = "Mophsik9876"
host = "localhost"             
database = "telco_churn"      

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")


df = pd.read_csv("D:/Churn_ML/telco_churn_ml/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")


df.to_sql(
    name="customers",         
    con=engine,               
    if_exists="replace",      
    index=False               
)

query = """
SELECT 
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers,
    AVG(TotalCharges) AS avg_total_charges,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate  # Добавлен расчет
FROM customers
GROUP BY Contract;
"""


result_df = pd.read_sql_query(query, engine) 

plt.figure(figsize=(10, 6))
result_df.plot.bar(x='Contract', y='churn_rate', rot=45)
plt.title('Churn Rate by Contract Type')
plt.ylabel('Churn Rate (%)')
plt.tight_layout()
plt.savefig('D:/Churn_ML/telco_churn_ml/reports/contract_churn.png')
plt.show()

print(result_df)



# выгрузка данных для M, это позже понадобится 
ml_data_query = """
SELECT 
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    TotalCharges,
    Churn
FROM customers;
"""
ml_df = pd.read_sql_query(ml_data_query, engine)
ml_df.to_csv('telco_ml_dataset.csv', index=False)

engine.dispose()