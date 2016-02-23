import os
import sys
import numpy

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

class PauliBasis(object):
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
    def getDimension(self):
        return self._dimension
    def getLs(self):
        return self.L
    def getMs(self, l):
        mNumber = int(2*l)
        return [-l+m for m in range(0, mNumber+1)]
    def getElement(self, l, m):
        self.__check_l(l)
        self.__check_m(l,m)
        elementNumber = self.__get_element_order(l,m)
        vector = numpy.eye(self.getDimension())[elementNumber-1]


class Basis(object):

    def __init__(self):
        """TODO: to be defined1. """
    def __mult__(self, other_basis):
        """
        Tensor product of the basis
        """
        pass


class State(object):

    def __init__(self):
        """TODO: to be defined1. """
        pass
    def __add__(self, state):
        pass
    def __mult__(self, state):
        """
        Tensor product
        """
    def __mod__(self, state):
        """
        Normal product
        """
    def __check_basis(self):
        if not self.getBasis():
            raise ValueError("The state %s has no basis assigned"%self)
            sys.exit(1)
    def setBasis(self, basis):
        self.basis = basis
    def getBasis(self):
        self.__check_basis()
        return self.basis
    def getComponents(self):
        pass
    def getFunction(self):
        pass


class Spin(State):
    def __init__(self, l, m):
        self.l     = l
        self.m     = m
        self.basis = None
    def getComponents(self):
        return self.getBasis().getElement(self.l, self.m)
    def getFunction(self):
        return self.getBasis().getElement(self.l, self.m)


class Orbital(State):
    def __init__(self, parameters=[]):
        self.parameters      = parameters


