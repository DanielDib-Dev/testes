"""
Script to extract data from the Health Procedures and Events Table from the PDF of Annex I
and convert it to CSV with complete column descriptions.

This script performs the following operations:
1. Extracts a ZIP file containing PDF documents.
2. Locates and reads the specific PDF file starting with 'Anexo_I_'.
3. Extracts table data from the PDF.
4. Processes and transforms the data.
5. Saves the result as a CSV file.
6. Compresses the CSV into a ZIP archive.
7. Cleans up temporary files.
"""

import logging
import os
import pandas as pd
import zipfile
from tabula import read_pdf

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WEB_SCRAPING_DIR = os.path.join(PROJECT_DIR, "1_web_scrapping_test")
INPUT_DIR = WEB_SCRAPING_DIR
INPUT_ZIP = 'anexos_rol_procedimentos.zip'

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = SCRIPT_DIR

NAME = "Daniel_Dib"
CSV_NAME = f"procedures_list_{NAME}.csv"
ZIP_NAME = f"Teste_{NAME}.zip"

COLUMN_MAP = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial',
}

def extract_zip(zip_path: str, extract_dir: str) -> None:
    """Extract contents from a ZIP file into the specified directory.

    Args:
        zip_path (str): Full path to the source ZIP file.
        extract_dir (str): Directory where the ZIP contents will be extracted.

    Raises:
        Exception: If there's an error during extraction.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_dir)
            logging.info(f'Files extracted successfully to: {extract_dir}')
    except Exception as e:
        logging.error(f'Error extracting ZIP: {str(e)}')
        raise

def find_pdf_file(directory: str) -> str:
    """Locate a PDF file that starts with 'Anexo_I' in the given directory.

    Args:
        directory (str): Directory path to search for the PDF file.

    Returns:
        str: Name of the found PDF file.

    Raises:
        FileNotFoundError: If no PDF file starting with 'Anexo_I_' is found in the directory.
    """
    for file in os.listdir(directory):
        if file.startswith('Anexo_I_') and file.endswith('.pdf'):
            return file
    raise FileNotFoundError("No PDF file starting with 'Anexo_I' was found")

def extract_table_from_pdf(pdf_path: str) -> pd.DataFrame:
    """Extract table data from a PDF file using tabula-py.

    This function reads the specified PDF file and extracts table data,
    returning it as a pandas DataFrame. It handles multiple pages and
    concatenates the results.

    Args:
        pdf_path (str): Full path to the PDF file to process.

    Returns:
        pd.DataFrame: DataFrame containing the extracted table data.

    Raises:
        Exception: If there's an error reading or processing the PDF file.
    """
    try:
        dfs = read_pdf(pdf_path, pages='all', lattice=True)

        if not dfs:
            raise Exception("No tables found in the PDF")

        df = pd.concat(dfs, ignore_index=True)

        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')

        for key, value in COLUMN_MAP.items():
            df[key] = df[key].replace(key, value)
        df.rename(columns=COLUMN_MAP, inplace=True)

        logging.info(f'Extracted table with {len(df)} rows and {len(df.columns)} columns')
        return df
    except Exception as e:
        logging.error(f'Error extracting table from PDF: {str(e)}')
        raise

def save_to_csv(df: pd.DataFrame, csv_path: str) -> None:
    """Save a pandas DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        csv_path (str): Full path where the CSV file will be created.

    Raises:
        Exception: If there's an error writing the CSV file.
    """
    try:
        df.to_csv(csv_path, index=False, header=True)
        logging.info(f'CSV saved successfully to: {csv_path}')
    except Exception as e:
        logging.error(f'Error saving CSV: {str(e)}')
        raise

def compress_csv(csv_path: str, zip_path: str) -> None:
    """Compress a CSV file into a ZIP archive.

    Args:
        csv_path (str): Full path to the source CSV file.
        zip_path (str): Full path where the ZIP archive will be created.

    Raises:
        Exception: If there's an error creating the ZIP archive.
    """
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_path, arcname=os.path.basename(csv_path))
        logging.info(f'CSV compressed successfully to: {zip_path}')
    except Exception as e:
        logging.error(f'Error compressing CSV: {str(e)}')
        raise

def cleanup_files(directory: str) -> None:
    """Remove all PDF files from the specified directory.

    This function scans the given directory and removes any files with the .pdf or .csv extension.

    Args:
        directory (str): Directory path to clean up the files from.

    Raises:
        Exception: If there's an error during the cleanup process.
    """
    try:
        for file in os.listdir(directory):
            if file.endswith('.pdf') or file.endswith('.csv'):
                file_path = os.path.join(directory, file)
                os.remove(file_path)
                logging.info(f'File removed: {file}')
    except Exception as e:
        logging.error(f'Error during cleanup: {str(e)}')

def main() -> None:
    """Execute the complete data extraction and transformation workflow.

    This function orchestrates the entire process:
    1. Extracts the input ZIP file.
    2. Locates and processes the PDF file.
    3. Extracts and transforms the table data.
    4. Saves the result as CSV.
    5. Compresses the CSV into a ZIP.
    6. Cleans up temporary files.

    Raises:
        Exception: If any step of the process fails.
    """
    try:
        input_zip_path = os.path.join(INPUT_DIR, INPUT_ZIP)
        csv_path = os.path.join(OUTPUT_DIR, CSV_NAME)
        zip_path = os.path.join(OUTPUT_DIR, ZIP_NAME)
        
        extract_zip(input_zip_path, OUTPUT_DIR)
        
        pdf_name = find_pdf_file(OUTPUT_DIR)
        pdf_path = os.path.join(OUTPUT_DIR, pdf_name)
        
        df = extract_table_from_pdf(pdf_path)
                
        save_to_csv(df, csv_path)
        compress_csv(csv_path, zip_path)
        
        logging.info('Process completed successfully!')
        
    except Exception as e:
        logging.error(f'Error during execution: {str(e)}')
        raise
    finally:
        cleanup_files(OUTPUT_DIR)

if __name__ == '__main__':
    main() 