
import pandas as pd

# ==========================================
# INSIGHTX - CUSTOMER INTELLIGENCE PLATFORM
# ==========================================

# 1. LOAD CUSTOMER FEEDBACK

data = pd.read_csv("data/customer_feedback.csv")

print("\n========== INSIGHTX ==========")

# 2. DISPLAY CUSTOMER FEEDBACK

print("\nCUSTOMER FEEDBACK")
print(data.head())

# 3. DATASET SIZE

print("\nDATASET SIZE")
print("Total reviews:", data.shape[0])
print("Total columns:", data.shape[1])

# 4. COLUMN NAMES

print("\nCOLUMN NAMES")
print(data.columns.tolist())

# 5. MISSING VALUES

print("\nMISSING VALUES")
print(data.isnull().sum())


# ==========================================
# 6. DATA QUALITY CHECKS
# ==========================================

print("\n========== DATA QUALITY CHECKS ==========")

duplicate_mask = data.duplicated()

missing_feedback_mask = data["feedback"].isnull()

invalid_ratings_mask = ~data["rating"].between(1, 5)

empty_feedback_mask = (
    data["feedback"].astype("string").str.strip().eq("")
)

print("Duplicate records:", duplicate_mask.sum())
print("Missing feedback:", missing_feedback_mask.sum())
print("Invalid ratings:", invalid_ratings_mask.sum())
print("Empty feedback:", empty_feedback_mask.sum())


# ==========================================
# 7. DATA CLEANING
# ==========================================

print("\n========== DATA CLEANING ==========")

# Preserve original data
cleaned_data = data.copy()

# Remove unnecessary spaces
cleaned_data["feedback"] = (
    cleaned_data["feedback"].astype("string").str.strip()
)

# Create validation conditions
valid_ratings = cleaned_data["rating"].between(1, 5)

valid_feedback = (
    cleaned_data["feedback"].notna()
    & cleaned_data["feedback"].ne("")
)

unique_records = ~cleaned_data.duplicated()

# Identify valid records
valid_mask = valid_ratings & valid_feedback & unique_records

# Identify rejected records
rejected_records = cleaned_data[~valid_mask].copy()


# ==========================================
# ==========================================
# 8. REJECTION REASONS
# ==========================================

rejected_records["rejection_reason"] = ""

# Invalid ratings
rejected_records.loc[
    ~valid_ratings.loc[rejected_records.index],
    "rejection_reason"
] += "Invalid rating; "

# Missing or empty feedback
rejected_records.loc[
    ~valid_feedback.loc[rejected_records.index],
    "rejection_reason"
] += "Missing or empty feedback; "

# Duplicate records
rejected_records.loc[
    ~unique_records.loc[rejected_records.index],
    "rejection_reason"
] += "Duplicate record; "

# Keep only valid records
cleaned_data = cleaned_data[valid_mask].copy()

# ==========================================
# 9. CLEANING SUMMARY
# ==========================================

print("\n========== CLEANING SUMMARY ==========")

print("Original records:", len(data))
print("Clean records:", len(cleaned_data))
print("Rejected records:", len(rejected_records))

print("\n========== REJECTED RECORDS ==========")

if len(rejected_records) > 0:
    print(rejected_records.to_string(index=False))
else:
    print("No rejected records found.")
    # ==========================================
# 10. EXPORT REJECTED RECORDS
# ==========================================

rejected_records.to_csv(
    "data/rejected_records.csv",
    index=False
)

print("\nRejected records exported successfully!")

print("\n========== INSIGHTX SUMMARY ==========")
print("Data cleaning completed successfully.")