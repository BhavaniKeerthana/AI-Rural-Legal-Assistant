import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv(
    "legal_assistant_dataset.csv"
)

questions = data["question"]

answers = data["answer"]

categories = data["category"]

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(
    questions
)

def search_answer(query):

    query_vector = vectorizer.transform(
        [query]
    )

    similarity = cosine_similarity(
        query_vector,
        vectors
    )

    index = similarity.argmax()

    return (
        answers.iloc[index],
        categories.iloc[index]
    )