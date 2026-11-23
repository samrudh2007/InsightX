import pandas as pd

# ==========================================
# INSIGHTX - CUSTOMER INTELLIGENCE PLATFORM
# ==========================================

# 1. Load customer feedback
data = pd.read_csv("data/customer_feedback.csv")

print("\n========== INSIGHTX ==========")

# 2. Display customer feedback
print("\nCUSTOMER FEEDBACK")
print(data.head())

# 3. Display dataset size
print("\nDATASET SIZE")
print(f"Total reviews: {data.shape[0]}")
print(f"Total columns: {data.shape[1]}")

# 4. Display column names
print("\nCOLUMN NAMES")
print(data.columns.tolist())

# 5. Check missing values
print("\nMISSING VALUES")
print(data.isnull().sum())
# 6. DATA QUALITY CHECKS

print("\n========== DATA QUALITY CHECKS ==========")

# Check duplicate records
duplicate_count = data.duplicated().sum()

print("\nDuplicate records:", duplicate_count)

# Check missing feedback
missing_feedback = data["feedback"].isnull().sum()

print("Missing feedback:", missing_feedback)

# Check invalid ratings
invalid_ratings = data[
    (data["rating"] < 1) | (data["rating"] > 5)
]

print("Invalid ratings:", len(invalid_ratings))

# Check empty feedback
empty_feedback = (
    data["feedback"].astype("string").str.strip().eq("").sum()
)

print("Empty feedback:", empty_feedback)
# 7. DATA CLEANING

print("\n========== DATA CLEANING ==========")

# Create a copy of original data
cleaned_data = data.copy()

# Remove extra spaces from feedback
cleaned_data["feedback"] = (
    cleaned_data["feedback"].astype("string").str.strip()
)

# Identify valid ratings
valid_ratings = cleaned_data["rating"].between(1, 5)

# Identify valid feedback
valid_feedback = (
    cleaned_data["feedback"].notna()
    & cleaned_data["feedback"].ne("")
)

# Identify duplicate records
unique_records = ~cleaned_data.duplicated()

# Keep only valid records
cleaned_data = cleaned_data[
    valid_ratings & valid_feedback & unique_records
].copy()

# Display cleaning results
print("Original records:", len(data))
print("Clean records:", len(cleaned_data))
print("Removed records:", len(data) - len(cleaned_data))


# 6. Calculate average rating
print("\nAVERAGE CUSTOMER RATING")
# 7. Calculate average rating
print("\nAVERAGE CUSTOMER RATING")
print(cleaned_data["rating"].mean())

# 8. Customer rating distribution
print("\nCUSTOMER RATING DISTRIBUTION")

rating_distribution = cleaned_data["rating"].value_counts().sort_index()

print(rating_distribution)

# 9. Classify reviews using ratings
positive_reviews = cleaned_data[cleaned_data["rating"] >= 4]
negative_reviews = cleaned_data[cleaned_data["rating"] <= 2]
neutral_reviews = cleaned_data[cleaned_data["rating"] == 3]

# 10. Display rating-based classification summary
print("\nCUSTOMER SENTIMENT SUMMARY")

print("Positive reviews:", len(positive_reviews))
print("Neutral reviews:", len(neutral_reviews))
print("Negative reviews:", len(negative_reviews))


# 9. Display rating-based classification summary
print("\nCUSTOMER SENTIMENT SUMMARY")

print("Positive reviews:", len(positive_reviews))
print("Neutral reviews:", len(neutral_reviews))
print("Negative reviews:", len(negative_reviews))

print("\n========== ANALYSIS COMPLETE ==========")