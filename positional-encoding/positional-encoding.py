import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    res = []

    for y in range(seq_len):
        seq = []
        
        for i in range(d_model):            
            if i % 2 == 0:
                val = np.sin(y / (base ** ((2 * (i // 2)) / d_model)))
                seq.append(val)      
            elif i % 2 == 1:
                val = np.cos(y / (base ** ((2 * (i // 2)) / d_model)))
                seq.append(val)
            else:
                seq.append(i)
        
        res.append(seq)
            
    return np.array(res)
    pass