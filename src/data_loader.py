import pandas as pd
import os


def load_insurance_data(file_path=None):
    """
    Safely loads the AlphaCare Insurance Solutions historical dataset.
    Automatically handles pathing whether run from notebooks or root directory.
    """
    if file_path is None:
        # Default target location
        file_path = os.path.join("data", "insurance_data.csv")

    # If it can't find it relative to current directory, check one level up
    # (helps when notebooks run with a different working directory context)
    if not os.path.exists(file_path):
        alternative_path = os.path.join("..", file_path)
        if os.path.exists(alternative_path):
            file_path = alternative_path

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"❌ Dataset not found at {file_path}. Please ensure your extracted "
            "CSV file from the zip folder is placed inside the 'data/' directory "
            "and named 'insurance_data.csv'."
        )

    print(f"✅ Successfully loaded dataset from: {file_path}")
    return pd.read_csv(file_path)
