# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:06:23 2022

@author: hp
"""

import matplotlib.pyplot as plt

data = [[0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0]]

def imshow():
    
    plt.imshow(data, cmap='rainbow')
    
    root.mainloop()
    
    

