# NpFile

## Install

```bash
pip install git+https://github.com/SunDoge/npfile.git
```

## Usage

### Save

```python
import numpy as np
from npfile import NpFile

data = np.random.rand(100, 1024, 14, 14).astype(np.float32)
with NpFile('__pycache__', 'w+', dtype=np.float32, shape=(100, 1024, 14, 14)) as fp:
    fp[:] = data
```

### Load

```python
import numpy as np
from npfile import NpFile

with NpFile('__pycache__', 'r') as fp:
    print(fp.shape)
```