from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


 

import sys
if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        logging.info("initiated the data ingestion config")
        data_ingestion_obj = DataIngestion(dataingestionconfig)
        dataingestionartifact = data_ingestion_obj.initiate_data_ingestion()
        logging.info(" data ingestion completed")
        print(dataingestionartifact)


        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)


    
        data_validation_artifact = data_validation.initiate_data_validation()
        logging .info("data validation completed")


        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)