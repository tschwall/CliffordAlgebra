# CliffordAlgebra
Repository für MathSem


## Aufbau Vortrag:
1. Was ist Clifford Algebra
Was ist die Motivation für die GA?
https://www.youtube.com/watch?v=YxpGRnv8lVU --> Gute Intuition wieso GA nützlich sein kann

1.1 Notation u = a*e_1 + b*e_2 --> Vergleich lineare Algebra (e1 und e2 als [1 0] und [0 1]) WICHTIG: Sagen das diese einheitsvektoren in der GA kein Sinn machen --> auf später verweisen

1.2 Zeigen für was multiplikation nützlich wäre --> direkt Länge bestimmen (mit Quadrat).
Es werden Orthonormal Vektoren als Baisvektoren gebraucht
 u^2 = (a*e_1 + b*e_2)*(a*e_1 + b*e_2) = a^2e_1*e_1 + b^2e_2e_2 + abe_1e_2 + abe_2e_1
 Damit dies die Länge ergibt muss u^2 = a^2e_1*e_1 + b^2e_2e_2 gelten.
 Daher abe_1e_2 + abe_2e_1 = 0 --> anticommutative e_1e_2 = -e_2e_1
 Multiplikationstabelle:
        1   e1  e2  e12
  1     1   e1  e2  e12
  e1    e1  1   e12 e2
  e2    e2  -e12
  e12   e12 -e2 
 Quadrat von e_1e_2 ---> (e_1e_2)^2 = e_1e_2e_1e_2 = -1 ---> Weil Quadrat -1 --> I
 
 u*v = (a*e_1 + b*e_2)(c*e_1 + d*e_2) = ac + bd + (ad - bd)e_1e_2
 ac + bd =  
 
 

Was ist der Unterschied zu Linearer Algebra? Geometrische Algebra ist eine Erweiterung der linearen Algebra. (LA subset of GA)
