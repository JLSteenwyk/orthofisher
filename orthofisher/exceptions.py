class OrthoFisherError(Exception):
    """Base exception for orthofisher runtime errors."""


class InputValidationError(OrthoFisherError):
    """Raised when CLI/user inputs are invalid."""


class OutputDirectoryExistsError(OrthoFisherError):
    """Raised when output directory exists and overwrite is not allowed."""


class HMMSearchError(OrthoFisherError):
    """Raised when hmmsearch execution or output validation fails."""
