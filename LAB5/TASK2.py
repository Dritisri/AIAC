# Loan approval eligibility evaluation

def evaluate_loan_eligibility(applicant):
    # Criteria: age >= 21, stable income, good credit score
    if applicant['age'] >= 21 and applicant['stable_income'] and applicant['good_credit_score']:
        return True, "Eligible for loan approval."
    else:
        return False, "Not eligible for loan approval."

# Applicant details
john = {
    'name': 'John',
    'age': 30,
    'stable_income': True,
    'good_credit_score': True
}

priya = {
    'name': 'Priya',
    'age': 30,
    'stable_income': True,
    'good_credit_score': True
}

# Evaluate both applicants
john_result, john_reason = evaluate_loan_eligibility(john)
priya_result, priya_reason = evaluate_loan_eligibility(priya)

print(f"John: {john_reason}")
print(f"Priya: {priya_reason}")

# Comparison
if john_result == priya_result:
    print("Decision does NOT change based only on the name.")
else:
    print("Decision changes based on the name (which should not happen).")