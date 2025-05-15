"""
    Saul Toribio
    4/16/25
    CSE012 Spring 2025: Week 12 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

import pandas as pd

def load_data(csv_filepath: str) -> pd.DataFrame | None:
    """Loads expedition data from a CSV file."""
    try:
        df = pd.read_csv(csv_filepath)
        print(f"Successfully loaded data from {csv_filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {csv_filepath}")
        return None

def find_valuable_artifacts(df: pd.DataFrame, min_value: float | int) -> pd.DataFrame:
    """
    Selects artifacts with an estimated value greater than or equal to min_value.

    Args:
        df (pd.DataFrame): The artifact DataFrame.
        min_value (float or int): The minimum value threshold.

    Returns:
        pd.DataFrame: DataFrame containing only valuable artifacts.
    """
    if df is None or 'EstValue' not in df.columns:
        return pd.DataFrame()

    valuable_df = df[df['EstValue'] >= min_value]
    valuable_df['EstValue'] = valuable_df['EstValue'].astype('int64')
    return valuable_df

def summarize_artifact_types(df: pd.DataFrame) -> pd.Series:
    """
    Counts the occurrences of each unique artifact type.

    Args:
        df (pd.DataFrame): The artifact DataFrame.

    Returns:
        pd.Series: Series with artifact types as index and counts as values,
                   sorted descending by count.
    """
    if df is None or 'Type' not in df.columns:
        return pd.Series(dtype=int)

    type_df = df['Type'].value_counts().sort_values(ascending=False)
    return type_df

def calculate_average_weight_by_material(df: pd.DataFrame, material: str) -> float:
    """
    Calculates the average weight of artifacts made of a specific material.

    Args:
        df (pd.DataFrame): The artifact DataFrame.
        material (str): The material to filter by.

    Returns:
        float: The average weight. Returns 0.0 if no such artifacts are found
               or if weights are missing.
    """
    if df is None or 'Material' not in df.columns or 'Weight_kg' not in df.columns:
        return 0.0

    filtered_df = df[(df['Material'] == material) & df['Weight_kg'].notnull()]

    if filtered_df.empty:
        return 0.0
    return filtered_df['Weight_kg'].mean()

def impute_missing_descriptions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fills missing artifact descriptions with 'Description unavailable'.

    Args:
        df (pd.DataFrame): The artifact DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame with missing descriptions filled.
    """
    if df is None or 'Description' not in df.columns:
        return pd.DataFrame()

    df_copy = df.copy()
    df_copy['Description'] = df_copy['Description'].fillna('Description unavailable')
    return df_copy

def find_heavy_deep_artifacts(
        df: pd.DataFrame, min_weight: float, min_depth: float
    ) -> pd.DataFrame:
    """
    Selects artifacts that are both heavy (>= min_weight) and found deep (>= min_depth).

    Args:
        df (pd.DataFrame): The artifact DataFrame.
        min_weight (float): The minimum weight threshold.
        min_depth (float): The minimum depth threshold.

    Returns:
        pd.DataFrame: DataFrame containing artifacts meeting both criteria.
    """
    if df is None or 'Weight_kg' not in df.columns or 'Depth_m' not in df.columns:
        return pd.DataFrame()

    filtered_df = df[(df['Weight_kg'] >= min_weight) & (df['Depth_m'] >= min_depth)]
    filtered_df['EstValue'] = filtered_df['EstValue'].astype('int64')
    return filtered_df

def get_value_distribution_metric(df: pd.DataFrame) -> float:
    """
    Calculates the median estimated value of all artifacts.

    Args:
        df (pd.DataFrame): The artifact DataFrame.

    Returns:
        float: The median estimated value. Returns 0.0 if column is empty or all NaN.
    """
    if df is None or 'EstValue' not in df.columns or df['EstValue'].isnull().all():
        return 0.0
    return df['EstValue'].median()
