import logging
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class CompilerError:
    message: str
    line: int
    column: int
    file: str
    severity: str
    suggestion: Optional[str] = None

class ErrorHandler:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.errors: List[CompilerError] = []
        
    def report_error(self, error: CompilerError):
        self.errors.append(error)
        logging.error(
            f"{error.file}:{error.line}:{error.column} - {error.severity}: {error.message}"
        )
        if error.suggestion:
            logging.info(f"Suggestion: {error.suggestion}")
            
    def has_errors(self) -> bool:
        return any(e.severity == 'ERROR' for e in self.errors)

    def log_summary(self):
        if self.errors:
            logging.info(f"Total errors: {len(self.errors)}")
            for error in self.errors:
                logging.info(f"{error.severity}: {error.message} at {error.file}:{error.line}:{error.column}") 