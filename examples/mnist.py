#!/usr/bin/env python3
import os, sys, traceback
sys.path.append(f'{os.getcwd()}/scratchgrad')

import numpy as np
from tensor import Tensor



print(Tensor.randn(2, 2, 3, 2))
T1 = Tensor(np.ones([1,2]))

