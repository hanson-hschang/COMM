"""
Created on Oct. 15, 2021
@author: Heng-Sheng (Hanson) Chang
"""

import numpy as np
from numba import njit

from comm.actuations.muscles.muscle import MuscleForce

class ObliqueMuscle(MuscleForce):
    def __init__(
        self,
        muscle_init_angle,
        ratio_muscle_position,
        rotation_number,
        rest_muscle_area,
        max_muscle_stress,
        **kwargs
    ):
        n_elem = rest_muscle_area.shape[0]
        s = np.linspace(0, 1, n_elem+1)
        s_muscle_position = (s[:-1]+s[1:])/2
        self.N = rotation_number
        kwargs.setdefault("type_name", "OM")
        MuscleForce.__init__(
            self,
            ratio_muscle_position * np.array(
                [np.cos(muscle_init_angle+2*np.pi*self.N*s_muscle_position), 
                 np.sin(muscle_init_angle+2*np.pi*self.N*s_muscle_position),
                 np.zeros(n_elem)]
            ),
            rest_muscle_area,
            max_muscle_stress * np.ones(n_elem),
            **kwargs
        )
