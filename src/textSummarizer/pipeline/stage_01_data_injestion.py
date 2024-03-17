### Import the ConfigurationManager from config folder's configuration.py file
from textSummarizer.config.configuration import ConfigurationManager
### Import data_injestion class from component folder's data_injestion.py file
from textSummarizer.components.data_injestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
