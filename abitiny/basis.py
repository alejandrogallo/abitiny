# -*- coding: utf-8 -*-
import os
import sys
import numpy

DEFAULT_BASIS_FILENAME = "basis.abitiny"

class Basis(object):

    def __init__(self, fileName=DEFAULT_BASIS_FILENAME):
        """TODO: to be defined1. """
        self._dimension = 0
        self.fileName = fileName
    def __eq__(self, basis):
        return True if id(self) == id(basis) else False
    def __mult__(self, other_basis):
        """
        Tensor product of the basis
        """
        return ProductBasis(self, other_basis)
    def parseFile(self):
        pass
    def getDimension(self):
        return self._dimension
    def getElementsFunction(self, i):
        pass
    def getElementsVector(self, i):
        pass

class ProductBasis(Basis):

    def __init__(self, basis1, basis2):
        """TODO: to be defined1. """
        self.basis1 = basis1
        self.basis2 = basis2
        self._dimension = self.basis1.getDimension() * self.basis2.getDimension()
    def getElement(self, i):
        counter = 0
        for i in range(self.basis1.getDimension()):
            for j in range(self.basis2.getDimension()):
                counter+=1
                if counter == i:
                    state1 = self.basis1.getElement(i)
                    state2 = self.basis2.getElement(j)
                    return state1*state2



class GaussianBasis(object):

    """
    Implementation of a gaussian basis

    \psi_{\zeta, n, l, m } (r, \theta, \phi) =
        N Y_{l, m} (\theta, \phi) r^{2n-2-l} e^{-\zeta r^{2} }

                                                        2
                                             2n-2-l  -ζr
     ψ           (r, θ, ϕ) = N Y     (θ, ϕ) r       e
      ζ, n, l, m                l, m

    \psi_{z, l_{x} , l_{y} , l_{z} }(x, y, z) =
        N x^{l_{x} } y^{l_{y} } z^{l_{z} } e^{-\zeta r^{2} }

                                    l   l   l      2
                                     x   y   z  -ζr
     ψ               (x, y, z) = N x   y   z   e
      z, l  , l  , l
          x    y    z

    """

    def __init__(self, filename=DEFAULT_BASIS_FILENAME):
        self.fileName = filename

    def parseInformation(self):
        pass

class PauliBasis(Basis):
    """
    Basis based on the canonical Pauli matrices
    """
    def __init__(self, L=[0.5]):
        self.L = L
        self._dimension = sum([2*l +1 for l in self.L])
    def __get_element_order(self, l, m):
        counter = 0
        for i in self.getLs():
            if i==l:
                for j in self.getMs(l):
                    counter+=1
                    if j==m:
                        return counter
            else:
                counter = counter + 2*i+1
    def __check_m(self,l,m):
        if not m in self.getMs(l):
            raise ValueError("Angular number m = %s is not in the basis, please choose a suitable basis."%(m))
            sys.exit(1)
    def __check_l(self, l):
        if not l in self.L:
            raise ValueError("Angular number l = %s is not in the basis, please choose a suitable basis."%(l))
            sys.exit(1)
    def getLs(self):
        return self.L
    def getMs(self, l):
        mNumber = int(2*l)
        return [-l+m for m in range(0, mNumber+1)]
    def getElementBySpinNumber(self, l, m):
        self.__check_l(l)
        self.__check_m(l,m)
        elementNumber = self.__get_element_order(l,m)
        vector = numpy.eye(self.getDimension())[elementNumber-1]
    def getElement(self, i):
        if i>seld.getDimension():
            raise ValueError("The number of elements in this basis is just %s"%(self.getDimension()))
            return False
        counter = 0
        for l in self.getLs():
            for m in self.getMs(l):
                counter+=1
                if counter == i:
                    return self.getElementBySpinNumber(l,m)

