# Simon Algorithm

#### Example with the vector b='110' (thus n=3) as the period of the function.

The circuit looks like:
![Circuit](./images/circuit.png?raw=true)

The measurements of 1024 shots are:
![Measurements](./images/measurements.png?raw=true)

The verification of dot-product between each measured vector with the period vector (b) are indeed equals 0 (modulo 2):
![Verification](./images/verification.png?raw=true)

The general form of Simon Circuit:
![General Form](./images/general_simon.png?raw=true)
