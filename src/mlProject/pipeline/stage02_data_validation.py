from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject import logger

STAGE_NAME="Data validation"

class DataValidationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=='__main__':
    try:
        logger.info(f"stage ---{STAGE_NAME}---STARTED")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"stage ---{STAGE_NAME}---COMPLETED")
        
    except Exception as e:
        raise e