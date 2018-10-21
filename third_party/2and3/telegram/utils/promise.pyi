# Stubs for telegram.utils.promise (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

logger: Any

class Promise:
    pooled_function: Any = ...
    args: Any = ...
    kwargs: Any = ...
    done: Any = ...
    def __init__(self, pooled_function: Any, args: Any, kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def __call__(self) -> None: ...
    def result(self, timeout: Optional[Any] = ...): ...
    @property
    def exception(self): ...
