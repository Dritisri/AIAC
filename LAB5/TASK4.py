def get_score(education, experience, gender, age):
    # Scoring weights (example)
    education_weights = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    # Experience: 2 points per year, up to 20 years
    experience_score = min(experience, 20) * 2

    # Gender: No score difference (to avoid bias)
    gender_score = 0

    # Age: Neutral, no score difference (to avoid bias)
    age_score = 0

    # Education score
    education_score = education_weights.get(education.lower(), 0)

    total_score = education_score + experience_score + gender_score + age_score
    return total_score

def main():
    print("Job Applicant Scoring System")
    education = input("Enter education (highschool/bachelor/master/phd): ")
    experience = int(input("Enter years of experience: "))
    gender = input("Enter gender (male/female/other): ")
    age = int(input("Enter age: "))

    score = get_score(education, experience, gender, age)
    print(f"Applicant Score: {score}")

    # Bias analysis
    print("\nBias Analysis:")
    print("- Education and experience are weighted.")
    print("- Gender and age are not used in scoring to avoid bias.")
    print("- Ensure education weights reflect job requirements, not stereotypes.")

if __name__ == "__main__":
    main()