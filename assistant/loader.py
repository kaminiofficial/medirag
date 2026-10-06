

from langchain_community.document_loaders import PyPDFLoader
from assistant.logger import get_logger
from assistant import config

logger = get_logger(__name__)

def load_data():
 logger.info("Loading data from PDF files...")
 loader = PyPDFLoader(config.DATA_PATH)
 data = loader.load()
 logger.info(f"Loaded {len(data)} documents from PDF files.")
 return data
