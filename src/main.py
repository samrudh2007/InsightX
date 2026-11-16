import pandas as pd

# Load customer feedback
data = pd.read_csv("data/customer_feedback.csv")

print("\n========== INSIGHTX ==========")

# 1. Display customer feedback
print("\nCUSTOMER FEEDBACK")
print(data.head())

# 2. Display dataset size
print("\nDATASET SIZE")
print(f"Total reviews: {data.shape[0]}")
print(f"Total columns: {data.shape[1]}")

# 3. Display column names
print("\nCOLUMN NAMES")
print(data.columns.tolist())

# 4. Check missing values
print("\nMISSING VALUES")
print(data.isnull().sum())

# 5. Calculate average rating
print("\nAVERAGE CUSTOMER RATING")
print(data["rating"].mean())
# 6. Customer rating distribution
print("\nCUSTOMER RATING DISTRIBUTION")

rating_distribution = data["rating"].value_counts().sort_index()

print(rating_distribution)


# 7. Separate positive and negative reviews
positive_reviews = data[data["rating"] >= 4]

negative_reviews = data[data["rating"] <= 2]

neutral_reviews = data[data["rating"] == 3]


print("\nCUSTOMER SENTIMENT SUMMARY")

print("Positive reviews:", len(positive_reviews))
print("Neutral reviews:", len(neutral_reviews))
print("Negative reviews:", len(negative_reviews))# 6. Customer rating distribution
print("\nCUSTOMER RATING DISTRIBUTION")

rating_distribution = data["rating"].value_counts().sort_index()

print(rating_distribution)


# 7. Separate positive and negative reviews
positive_reviews = data[data["rating"] >= 4]

negative_reviews = data[data["rating"] <= 2]

neutral_reviews = data[data["rating"] == 3]


print("\nCUSTOMER SENTIMENT SUMMARY")

print("Positive reviews:", len(positive_reviews))
print("Neutral reviews:", len(neutral_reviews))
print("Negative reviews:", len(negative_reviews))
print("\n========== ANALYSIS COMPLETE ==========")