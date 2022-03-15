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
    GENERAL_ARTS = 'GENERAL ARTS'
    GENERAL_SCIENCE = 'GENERAL SCIENCE'
    BUSINESS = 'BUSINESS'
    VISUAL_ARTS = 'VISUAL ARTS'
    TECHNICAL = 'TECHNICAL'
    AGRIC_SCIENCE = 'AGRIC SCIENCE'

    def get_programs(self):
        return list(map(str, self))
