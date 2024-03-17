# import DataIngestionTrainingPipeline class from pipeline
from textSummarizer.pipeline.stage_01_data_injestion import DataIngestionTrainingPipeline
# Import logger
from textSummarizer.logging import logger

STAGE_NAME = "Data Injestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} finished <<<<<<")
except Exception as e:
    logger.exceptions(e)
    raise e