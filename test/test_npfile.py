from npfile import NpFile
import numpy as np
import os


def test_dtype():
    dtype = np.float32

    with NpFile('__pycache__', 'w+', dtype=dtype, shape=(1, 2)) as fp:
        assert fp.dtype == dtype


def test_shape():
    shape = (1, 2)

    with NpFile('__pycache__', 'w+', dtype=np.float32, shape=shape) as fp:
        assert fp.shape == shape


def test_save_and_load():
    data = np.random.rand(100, 1024, 14, 14).astype(np.float32)

    with NpFile('__pycache__', 'w+', dtype=np.float32, shape=(100, 1024, 14, 14)) as fp:
        fp[:] = data

    fp_data = np.memmap(os.path.join('__pycache__', 'data.dat'),
                        dtype=np.float32, shape=(100, 1024, 14, 14))

    assert np.array_equal(data, fp_data)

    with NpFile('__pycache__', 'r') as fp:
        assert np.array_equal(data, fp)
