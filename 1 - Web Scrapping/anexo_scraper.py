"""
Script to download and compress PDFs from Annexes I and II of the ANS Procedures List.

This script automates the process of downloading PDF files from the ANS website,
specifically looking for Annexes I and II of the Procedures List. It downloads
the files, compresses them into a ZIP archive, and then removes the original PDFs.
"""

import logging
import os
import zipfile
from typing import List, Tuple
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

BASE_URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
KEYWORDS = ['anexo i', 'anexo ii']
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = SCRIPT_DIR
ZIP_NAME = 'anexos_rol_procedimentos.zip'

def setup_directories() -> Tuple[str, str]:
    """Create and configure the necessary directories for file operations.
    
    This function creates the output directory if it doesn't exist and prepares
    the path for the final ZIP file.
    
    Returns:
        Tuple[str, str]: A tuple containing:
            - The output directory path
            - The complete path for the ZIP file
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    zip_path = os.path.join(OUTPUT_DIR, ZIP_NAME)
    return OUTPUT_DIR, zip_path

def download_pdf(url: str, file_path: str) -> None:
    """Download a PDF file from a given URL and save it locally.
    
    This function downloads a PDF file from the specified URL and saves it to
    the given file path. It includes a timeout to prevent hanging on slow
    connections.
    
    Args:
        url: The complete URL of the PDF file to download
        file_path: The local path where the PDF should be saved
        
    Raises:
        requests.RequestException: If the download fails or times out
        IOError: If there's an error writing the file to disk
    """
    logging.info('Downloading: %s', os.path.basename(file_path))
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    with open(file_path, 'wb') as f:
        f.write(response.content)

def find_pdf_links(soup: BeautifulSoup, keywords: List[str], url: str) -> List[Tuple[str, str]]:
    """Find PDF links in the webpage that match the given keywords.
    
    This function searches through all links in the webpage and filters for
    PDF files that contain any of the specified keywords in their text.
    
    Args:
        soup: BeautifulSoup object containing the parsed webpage content
        keywords: List of keywords to search for in link text
        url: The base URL of the webpage for resolving relative URLs
        
    Returns:
        List[Tuple[str, str]]: A list of tuples, each containing:
            - The complete URL of the PDF file
            - The filename of the PDF
    """
    pdf_links = []
    for link in soup.find_all('a'):
        text = link.get_text(strip=True).lower()
        href = link.get('href')
        
        if (href and 
            any(keyword in text for keyword in keywords) and 
            href.endswith('.pdf')):
            pdf_url = urljoin(url, href)
            filename = os.path.basename(href)
            pdf_links.append((pdf_url, filename))
    
    return pdf_links

def compress_files(files: List[str], zip_path: str) -> None:
    """Compress multiple PDF files into a single ZIP archive.
    
    This function creates a ZIP file containing all the specified PDF files,
    maintaining their original filenames within the archive.
    
    Args:
        files: List of paths to the PDF files to be compressed
        zip_path: The path where the ZIP file should be created
        
    Raises:
        zipfile.BadZipFile: If there's an error creating the ZIP file
        IOError: If there's an error reading any of the source files
    """
    logging.info('Compressing files to: %s', zip_path)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in files:
            zipf.write(file_path, arcname=os.path.basename(file_path))

def cleanup_pdfs(files: List[str]) -> None:
    """Remove the original PDF files after successful compression.
    
    This function deletes the PDF files that were downloaded and compressed
    into the ZIP archive. It handles errors gracefully and logs any issues
    that occur during deletion.
    
    Args:
        files: List of paths to the PDF files to be removed
    """
    logging.info('Removing PDF files...')
    for file in files:
        try:
            os.remove(file)
            logging.info('File removed: %s', os.path.basename(file))
        except OSError as e:
            logging.error('Error removing %s: %s', os.path.basename(file), str(e))

def main() -> None:
    """Execute the complete PDF download and compression workflow.
    
    This function orchestrates the entire process:
    1. Sets up the necessary directories
    2. Downloads the webpage content
    3. Finds relevant PDF links
    4. Downloads the PDFs
    5. Compresses them into a ZIP file
    6. Cleans up the original PDFs
    
    The function includes error handling at each step and will stop
    if any critical error occurs.
    """
    output_dir, zip_path = setup_directories()
    
    logging.info('Accessing ANS page...')
    try:
        response = requests.get(BASE_URL, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        logging.error('Error accessing page: %s', str(e))
        return
    
    logging.info('Searching for Annexes I and II...')
    pdf_links = find_pdf_links(soup, KEYWORDS, BASE_URL)
    
    if not pdf_links:
        logging.warning('No PDFs from Annex I or II were found.')
        return
    
    downloaded_files = []
    for pdf_url, filename in pdf_links:
        file_path = os.path.join(output_dir, filename)
        try:
            download_pdf(pdf_url, file_path)
            downloaded_files.append(file_path)
        except (requests.RequestException, IOError) as e:
            logging.error('Error downloading %s: %s', filename, str(e))
    
    if not downloaded_files:
        logging.error('No files were successfully downloaded.')
        return
    
    try:
        compress_files(downloaded_files, zip_path)
    except (zipfile.BadZipFile, IOError) as e:
        logging.error('Error compressing files: %s', str(e))
        return
    
    cleanup_pdfs(downloaded_files)
    
    logging.info('Completed successfully!')

if __name__ == '__main__':
    main()