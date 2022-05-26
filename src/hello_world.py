from typing import Any
import torch


class HelloWorld:
    
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        x = torch.rand(5,3)
        return x
        