class KaggleConstants(object):
    MOBILE_DATASET_HANDLE = 'valakhorasani/mobile-device-usage-and-user-behavior-dataset'
    MOBILE_DATASET_FILE_NAME = 'user_behavior_dataset.csv'

class ModelSelectionConstants(object): 
    MODEL_SELECTION_FOLDER = 'model_selection/'
    DATA_FOLDER = MODEL_SELECTION_FOLDER + 'data/'
    MODEL_FOLDER = MODEL_SELECTION_FOLDER + 'models/'

class RandomStateConstants(object): 
    TRAIN_TEST_SPLIT = 424242
    QUANTILE_SCALER = 123456
    SVC_SEED = 789012
    LOG_REG_SEED = 345678
    DECISION_TREE_SEED = 890123
    RANDOM_FOREST_SEED = 456789
    GRADIENT_BOOSTING_SEED = 110797