import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_mock_dataset() -> pd.DataFrame:
    """Create a mock dataset similar to raw_skills.csv.

    The DataFrame columns are:
    - role: the job role or item name
    - skills: a string containing associated skills and tools
    """
    data = {
        "role": [
            "Data Scientist",
            "DevOps Engineer",
            "Backend Developer",
            "Android Developer",
            "Cloud Architect",
            "Frontend Developer",
            "Machine Learning Engineer",
        ],
        "skills": [
            "Python, Statistics, Machine Learning, Data Visualization, SQL, Pandas, Scikit-learn",
            "Cloud Computing, Automation, Docker, Kubernetes, CI/CD, Linux, Monitoring",
            "Python, Java, REST APIs, SQL, Databases, Microservices, Spring Boot",
            "Kotlin, Java, Android SDK, UI Design, Firebase, Mobile Development",
            "AWS, Azure, Cloud Computing, Infrastructure as Code, Networking, Security",
            "HTML, CSS, JavaScript, React, Responsive Design, UX, Web Development",
            "Python, Deep Learning, TensorFlow, PyTorch, Model Deployment, AI, Data Engineering",
        ],
    }
    return pd.DataFrame(data)


def ingest_user_profile(user_skills: list[str]) -> list[str]:
    """Validate and return a normalized user profile list.

    Requires at least 3 skills. If the input is invalid, it raises ValueError.
    """
    if not isinstance(user_skills, list):
        raise ValueError("User profile must be provided as a list of skill strings.")

    normalized = [skill.strip() for skill in user_skills if isinstance(skill, str) and skill.strip()]
    if len(normalized) < 3:
        raise ValueError("Please provide at least 3 skills for the user profile.")

    return normalized


def handle_cold_start(dataset: pd.DataFrame, top_n: int = 3) -> list[tuple[str, float]]:
    """Return a trending fallback list for cold-start users.

    This example assumes that the most globally popular tech stacks are the top rows
    in the dataset by role order. In a real system, popularity metadata would be used.
    """
    trending = dataset.head(top_n)[["role"]].copy()
    trending["score"] = 0.0
    return list(trending.itertuples(index=False, name=None))


def score_roles(dataset: pd.DataFrame, user_skills: list[str]) -> list[tuple[str, float]]:
    """Compute cosine similarity between the user profile and each role's skills."""
    if not user_skills:
        return []

    corpus = dataset["skills"].tolist() + [" ".join(user_skills)]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)

    role_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]

    similarity_scores = cosine_similarity(role_vectors, user_vector).flatten()
    scored_roles = list(zip(dataset["role"].tolist(), similarity_scores))
    return scored_roles


def sort_and_filter(scored_roles: list[tuple[str, float]], top_n: int = 3) -> list[tuple[str, float]]:
    """Sort scored roles by similarity score and return the top N results."""
    sorted_roles = sorted(scored_roles, key=lambda x: x[1], reverse=True)
    return sorted_roles[:top_n]


def recommend_tech_stacks(user_skills: list[str], dataset: pd.DataFrame, top_n: int = 3) -> list[tuple[str, float]]:
    """Main recommender function implementing the 4-step IPO pipeline."""
    if not user_skills:
        print("Cold start detected: returning trending fallback results.")
        return handle_cold_start(dataset, top_n)

    validated_skills = ingest_user_profile(user_skills)
    scored_roles = score_roles(dataset, validated_skills)
    return sort_and_filter(scored_roles, top_n)


def print_recommendations(title: str, recommendations: list[tuple[str, float]]) -> None:
    """Print a clear recommendation result block."""
    print(f"\n=== {title} ===")
    for rank, (role, score) in enumerate(recommendations, start=1):
        print(f"{rank}. {role} - score: {score:.4f}")


def main() -> None:
    dataset = build_mock_dataset()

    # Standard user input example
    user_profile = ["Python", "Cloud Computing", "Automation"]
    standard_recommendations = recommend_tech_stacks(user_profile, dataset, top_n=3)
    print_recommendations("Standard User Input Recommendations", standard_recommendations)

    # Cold-start example
    cold_start_recommendations = recommend_tech_stacks([], dataset, top_n=3)
    print_recommendations("Cold Start Trending Fallback", cold_start_recommendations)


if __name__ == "__main__":
    main()
