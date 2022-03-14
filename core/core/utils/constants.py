from enum import Enum


class AdmissionStatus(Enum):
    """
    Enum class for AdmissionStatus
    """
    PENDING = 1
    APPROVED = 2
    REJECTED = 3


class Programs(Enum):
    """
    Enum class for Programs
    """
    GENERAL_ARTS = 1
    GENERAL_SCIENCE = 2
    BUSINESS = 3
    VISUAL_ARTS = 4
    TECHNICAL = 5
    AGRIC_SCIENCE = 6
    
