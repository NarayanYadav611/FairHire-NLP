import pandas as pd
import random

def generate_fake_resume_data(num_samples=100):
    skills = ["Python", "Java", "C++", "Machine Learning", "Data Analysis",
              "Communication", "SQL", "NLP", "Deep Learning", "Leadership"]

    data = []

    for _ in range(num_samples):
        resume_skills = random.sample(skills, random.randint(3, 6))
        experience = random.randint(0, 5)
        hired = 1 if ("Python" in resume_skills and experience > 2) else 0

        data.append({
            "skills": ", ".join(resume_skills),
            "experience_years": experience,
            "hired": hired
        })

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = generate_fake_resume_data(200)
    df.to_csv("resume_data.csv", index=False)
    print("Dataset generated successfully!")
