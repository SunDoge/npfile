import torch
import numpy as np
from dataclasses import dataclass
from typing import Tuple, Any
import os
import pickle

__version__ = '0.1.0'


@dataclass
class MetaData:
    dtype: Any
    shape: Tuple[int, ...]


class NpFile:

    def __init__(self, name: str, mode: str, dtype: Any, shape=None):

        self.name = name
        self.mode = mode

        self.meta = MetaData(dtype, shape)

        os.makedirs(name, exist_ok=True)
        self.np_name = os.path.join(name, 'data.dat')
        self.mata_name = os.path.join(name, 'meta.pkl')

    @property
    def dtype(self):
        return self.meta.dtype

    @property
    def shape(self) -> Tuple[int, ...]:
        return self.meta.shape
