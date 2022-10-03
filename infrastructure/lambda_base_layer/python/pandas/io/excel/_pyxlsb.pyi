from pandas._typing import FilePathOrBuffer as FilePathOrBuffer, Scalar as Scalar
from pandas.io.excel._base import _BaseExcelReader
from typing import Any, List, AnyStr


class _PyxlsbReader(_BaseExcelReader):
    def __init__(self, filepath_or_buffer: FilePathOrBuffer[AnyStr]) -> None: ...
    def load_workbook(self, filepath_or_buffer: FilePathOrBuffer[AnyStr]) -> Any: ...
    @property
    def sheet_names(self) -> List[str]: ...
    def get_sheet_by_name(self, name: str) -> Any: ...
    def get_sheet_by_index(self, index: int) -> Any: ...
    def get_sheet_data(self, sheet: Any, convert_float: bool) -> List[List[Scalar]]: ...
