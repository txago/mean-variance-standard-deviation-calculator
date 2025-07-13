import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    clist = np.array(list).reshape(3, 3)
    
    dictionary = {
        'mean': [
            clist.mean(axis=0).tolist(), 
            clist.mean(axis=1).tolist(), 
            clist.mean()
        ],
        'variance': [
            clist.var(axis=0).tolist(), 
            clist.var(axis=1).tolist(), 
            clist.var()
        ],
        'standard deviation': [
            clist.std(axis=0).tolist(), 
            clist.std(axis=1).tolist(), 
            clist.std()
        ],
        'max': [
            clist.max(axis=0).tolist(), 
            clist.max(axis=1).tolist(), 
            clist.max()
        ],
        'min': [
            clist.min(axis=0).tolist(), 
            clist.min(axis=1).tolist(), 
            clist.min()
        ],
        'sum': [
            clist.sum(axis=0).tolist(), 
            clist.sum(axis=1).tolist(), 
            clist.sum()
        ]
    }

    return dictionary