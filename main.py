from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f"stage ---{STAGE_NAME}---STARTED")
   obj=DataValidationTrainingPipeline()
   obj.main()
   logger.info(f"stage ---{STAGE_NAME}---COMPLETED")
   
except Exception as e:
   raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f".......{STAGE_NAME}.STARTED...")
    obj=DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"....{STAGE_NAME}..COMPLETED...")
except Exception as e:
    raise e


STAGE_NAME = "Model Training stage"
try:
    logger.info(f".......{STAGE_NAME}.STARTED...")
    obj=ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"....{STAGE_NAME}..COMPLETED...")
except Exception as e:
    raise e

STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f".......{STAGE_NAME}.STARTED...")
    obj=ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"....{STAGE_NAME}..COMPLETED...")
except Exception as e:
    raise e

