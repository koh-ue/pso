#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: FIXME: XXX: HACK: NOTE: INTENT: USAGE:

import numpy as np

class Griewank:
    def __init__(self, max_range_value=600):
        self.problem_name = 'griewank'
        self.max_range_value = max_range_value
        self.x_range = np.array([-max_range_value, max_range_value])
        self.y_range = np.array([-float('inf'), 0])
    
    def init(self):
        pass

    def eval(self, x_array):
        summation = np.sum(x_array**2, axis=-1)
        prod = np.prod(np.cos(x_array / np.sqrt(np.arange(1, x_array.shape[-1]+1))), axis=-1)
        res = 1 + summation/4000 - prod
        return res
    
    def best_index(self, x_array):
        res = self.eval(x_array)
        return np.unravel_index(np.argmin(res), res.shape)
    
    def personal_best(self, old_and_new_pos):
        res = self.eval(old_and_new_pos)

        best_idx = np.argmin(res, axis=-1)
        not_best_idx = best_idx == 0

        tmp_is_best_array = np.stack([not_best_idx, best_idx]).T
        tmp_is_best_array2 = np.tile(tmp_is_best_array, (2, 1, 1))
        is_best_array = np.transpose(tmp_is_best_array2, (1, 2, 0))

        return np.sum(old_and_new_pos * is_best_array, axis=-2)

class FiveWellPotential(Griewank):
    def __init__(self, max_range_value=20):
        super().__init__(max_range_value)
        self.problem_name = 'fivewellpotential'
    
    def eval(self, x_array):
        x1, x2 = x_array[..., 0], x_array[..., 1]
        #print(f'x1 = {x1.shape}')
        
        a = 1  /(1 + 0.05 * (x1**2 + (x2 - 10)**2))
        b = 1  /(1 + 0.05 * ((x1 - 10)**2 + x2**2))
        c = 1.5/(1 + 0.03 * ((x1 + 10)**2 + x2**2))
        d = 2  /(1 + 0.05 * ((x1 - 5)**2 + (x2 + 10)**2))
        e = 1  /(1 + 0.1  * ((x1 + 5)**2 + (x2 + 10)**2))

        f = 1 + 0.0001 * (x1**2 + x2**2)**1.2

        return (1 - a - b - c - d - e) * f

