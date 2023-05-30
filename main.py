from textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
# from src.exception import CustomExpection
from textSummarizer.logging import logging
import sys
logging.info(">>>>> stage_1_data_ingestion started")
try:
    DataIngestionTrainingPipeline().main()
    logging.info(">>>>> stage_1_data_ingestion completed")
except Exception as e:
        logging.exception(e)
        raise e
      