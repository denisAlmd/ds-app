import pandas as pd
from abc import ABC, abstractmethod

class BaseReader(ABC):

    def __init__(self, file_object, encoding:str='utf-8', header: int = 0, dtype: dict | type = str, **kwargs) -> None:
        self.file_object = file_object
        self.encoding: str = encoding
        self.header: int = header
        self.dtype: dict | type = dtype
        self.kwargs = kwargs
        self.data_frame: pd.DataFrame | None = None

    def set_encoding(self, encoding: str):
        self.encoding = encoding
        return self

    def set_header(self, header: int):
        self.header = header
        return self
    
    def set_dtype(self, dtype: dict | type):
        self.dtype = dtype
        return self
    
    @abstractmethod
    def read(self) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement the read method.")