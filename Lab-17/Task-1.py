import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load your employee dataset
# df = pd.read_csv('employee_data.csv') # Uncomment and set your CSV path

# Handle missing values in 'salary', 'department', 'joining_date'
df['salary'] = df['salary'].fillna(df['salary'].median())
df['department'] = df['department'].fillna('Unknown')
df['joining_date'] = df['joining_date'].ffill()  # Fixed: replaced deprecated fillna(method='ffill') with ffill()

# Convert "joining_date" column into proper datetime format
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')

# Standardize department names
department_map = {
    'hr': 'HR',
    'human resources': 'HR',
    'human resource': 'HR',
    'finance': 'Finance',
    'fin': 'Finance',
    'it': 'IT',
    'information technology': 'IT',
    'marketing': 'Marketing',
    'sales': 'Sales'
}
def standardize_department(dep):
    if pd.isnull(dep):
        return 'Unknown'
    dep_str = str(dep).strip().lower()
    return department_map.get(dep_str, dep.upper())

df['department'] = df['department'].apply(standardize_department)

# Encode categorical variables ('department', 'job_role')
le_department = LabelEncoder()
le_job_role = LabelEncoder()

df['department_encoded'] = le_department.fit_transform(df['department'].astype(str))
df['job_role_encoded'] = le_job_role.fit_transform(df['job_role'].astype(str))

