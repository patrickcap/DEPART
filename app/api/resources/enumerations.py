from enum import Enum

# Enumeration for the training status of a model
class ModelStatus(Enum):
    PENDING = 0         # Training request sent by user
    IN_PROGRESS = 1     # Model currently being trained
    COMPLETED = 2       # Model successfully trained
