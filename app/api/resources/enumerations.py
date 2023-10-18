from enum import Enum

# Enumeration for the training status of a model
class ModelStatus(Enum):
    PENDING = "pending"             # Training request sent by user
    IN_PROGRESS = "in_progress"     # Model currently being trained
    COMPLETED = "completed"         # Model successfully created
    FAILED = "failed"               # Error somewhere in creating the model