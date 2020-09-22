# ReactionModeling

![Project Image](https://github.com/temmy222/tough_refactor/blob/master/images/Multi%20plot%20vs%20time.png)

> 

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Geochemical software solutions are mostly written in difficult to understand languages such as C and Fortran. Though these languages are highly computationally efficient, they make it difficult for concepts to be easily picked up on. This repository attempts to create a python version of these codes that makes it easier fow newbies to geochemical modeling to pick up easily on fundamental concepts and to be better easily coupled to other subsurface phenomena such as flow and transport.

#### Technologies

- Python

[Back To The Top](#read-me-template)

---

## How To Use
ReactionModeling is developed using Object Oriented Programming concepts. Installation is described below. 

The code is intended for now to be developed using the law of mass action formulation as against the Gibbs free energy minimization approach. 



#### Installation
Use of the code requires the installation of external python libraries Numpy and Pandas. 


#### Code Status Update

```html
    Code can currently read data from thermodynamic databases written for the TOUGHREACT software.

    Calculations for activity coefficients have also been made.

    A simple newton raphson solver also exists for solving nonlinear algebraic equations

    Next major step involves creating a solution framework for n number of geochemical reactions and species in a geochemical batch system.

    Major goal - develop a fully coupled code with flow and transport but with a distinguishable geochemical version.

```
[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

I can be reached on tajayi3@lsu.edu for collaboration or more information on how to use or what I aim to achieve with this.

---

## License

MIT License

Copyright (c) [2020] [Temitope Ajayi]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

Temitope Ajayi is a Graduate Student at Louisiana State University


[Back To The Top](#read-me-template)
