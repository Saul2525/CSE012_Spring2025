"""
    Saul Toribio
    4/10/25
    CSE012 Spring 2025: Week 11 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

import re
from datetime import datetime
import pandas as pd

def load_artifact_data(excel_filepath: str) -> pd.DataFrame:
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    artifact = pd.read_excel(excel_filepath, sheet_name="Main Chamber", skiprows=3)
    return artifact

def load_location_notes(tsv_filepath: str) -> pd.DataFrame:
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    location = pd.read_csv(tsv_filepath, sep="\t")
    return location

def extract_journal_dates(journal_text: str) -> list:
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    raw_journal = re.findall(r"\d{2}/\d{2}/\d{4}", journal_text)
    journal = []
    for date in raw_journal:
        try:
            datetime.strptime(date, "%m/%d/%Y")
            journal.append(date)
        except ValueError:
            pass
    return journal

def extract_secret_codes(journal_text: str) -> list:
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    codes = re.findall(r"AZMAR-\d{3}", journal_text)
    return codes
