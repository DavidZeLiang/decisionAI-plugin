import enum

class ModelState(enum.Enum):
    Pending = 0
    Training = 1
    Ready = 2
    Deleted = 3
    Failed = 4

class InferenceState(enum.Enum):
    Pending = 0
    Running = 1
    Ready = 2
    Failed = 3

STATUS_SUCCESS = 'Success'
STATUS_FAIL = 'Fail'

TIMESTAMP = 'timestamp'
VALUE = 'value'

LAG = 'lag'
FORECAST = 'forecast'
UPPER = 'upper'
LOWER = 'lower'

DAY_IN_SECONDS = 86400
HOUR_IN_SECONDS = 3600
MINT_IN_SECONDS = 60