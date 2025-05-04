import pickle

d = {'int': 100, 'bool': False, 'list': [0, 1, 2]}

with open('TDE\Trabalho2\dados.pkl', 'wb') as f:
    pickle.dump(d, f)