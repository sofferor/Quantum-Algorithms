from oracle import oracle
from deutchJozsa import algorithm
from utils import Case

n = 4
oracle_gate = oracle(Case.balanced, n)
result = algorithm(oracle_gate, n)
print("Result: {}".format(result))
