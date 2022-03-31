import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  calculations = {}
  matrix = np.array(list).reshape(3, 3)

  for k, m in {
    'mean': 'mean',
    'variance': 'var',
    'standard deviation': 'std',
    'max': 'max',
    'min': 'min',
    'sum': 'sum'
  }.items():
    calculations[k] = [
      getattr(matrix, m)(axis = 0).tolist(),
      getattr(matrix, m)(axis = 1).tolist(),
      getattr(matrix, m)()
    ]
  
  return calculations