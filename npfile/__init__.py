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

    def __init__(self, name: str, mode: str, dtype=None, shape=None):

        self.name = name
        self.mode = mode

        os.makedirs(name, exist_ok=True)
        self.np_name = os.path.join(name, 'data.dat')
        self.meta_name = os.path.join(name, 'meta.pkl')

        if self.mode == 'w+':
            self.meta = MetaData(dtype, shape)
        elif self.mode in ['r', 'r+', 'c']:
            with open(self.meta_name, 'rb') as f:
                self.meta = pickle.load(f)

        self.fp = np.memmap(
            self.np_name,
            dtype=self.meta.dtype,
            mode=mode,
            shape=self.meta.shape
        )

    @property
    def dtype(self):
        return self.meta.dtype

    @property
    def shape(self) -> Tuple[int, ...]:
        return self.meta.shape

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        # save meta data
        if self.mode == 'w+':
            with open(self.meta_name, 'wb') as f:
                pickle.dump(self.meta, f)
        # save to disk
        del self.fp
