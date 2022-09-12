# Deutsch-Jozsa Algorithm


#### Explanation for the algorithm, and why it's actually working:

![Deutsch-Jozsa Algorithm](/images/deutch_algorithm-1.jpg?raw=true)
![Deutsch-Jozsa Algorithm](/images/deutch_algorithm-2.jpg?raw=true)


#### Example of n=4 of the Deutsch-Jozsa Algorithm in code.

The circuit looks like:
![Circuit](/images/deutch_algorithm-2.jpg?raw=true)

A circuit of a balanced oracle (the balanced oracle can be built in many ways, so this is only one of them):
![Balanced Oracle](/images/balanced_oracle.png?raw=true)

The circuit of constant 0 oracle (the identity function):
![Constant 0 Oracle](/images/constant_0_oracle.png?raw=true)

The circuit of constant 1 oracle:
![Constant 1 Oracle](/images/constant_1_oracle.png?raw=true)

The result on balanced oracle:
![Result on Balanced Oracle](/images/result_on_balanced_oracle.png?raw=true)

The result on constant oracle:
![Result on Constant Oracle](/images/result_on_constant_oracle.png?raw=true)


#### The circuits as shown in the books.

The one dimension case:
![One Dimension Case](/images/one_dimension_case.png?raw=true)

The general case:
![General Case](/images/general_case.png?raw=true)
