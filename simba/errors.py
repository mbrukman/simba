class DimensionError(Exception):
    """Represents an error involving matrix dimensions."""


class CoefficientError(Exception):
    """Represents an error involving transfer function coefficients."""


class StateSpaceError(Exception):
    """Represents a miscellaneous error involving `StateSpace`."""
