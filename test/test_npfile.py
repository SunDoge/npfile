from npfile import NpFile
import numpy as np

def test_dtype():
    dtype = np.float32

    with NpFile('__pycache__', 'w+', dtype=dtype, shape=(1,2)) as fp:
        assert fp.dtype == dtype


def test_shape():
    shape = (1,2)

    with NpFile('__pycache__', 'w+', dtype=np.float32, shape=shape) as fp:
        assert fp.shape == shape
