# -*- coding: utf-8 -*-
import os
import sys
import numpy

class State(object):

    def __init__(self, basis_number=False, basis=None, components = None):
        self.scalar_factor = 1
        self.basis         = basis
        self.basis_vector  = False
        self.components    = [self] if not components else components
        if basis_number:
            self.basis_vector = basis_number
            self.__check_basis()
    def __invert__(self):
        return self.getCoords().conj().transpose()
    def __add__(self, state):
        new_components = self.getComponents() + state.getComponents()
        if self.getBasis() != state.getBasis():
            raise ValueError("Adding two states is only possible if the basis are the same")
            return False
        sum_state = State(basis = self.getBasis(), components = new_components)
        return sum_state
    def __mult__(self, multiplier):
        """
        Tensor product
        """
        try:
            # if the multiplier is a number
            factor = float(multiplier)
        except Exception as e:
            return self.__tensor(multiplier)
        else:
            self.scalar_factor = factor
            return self
    def __mod__(self, state):
        """
        Normal product
        """
        return numpy.dot(~self, state.getCoords())
    def __tensor(self, state):
        pass
    def __check_basis(self):
        if not self.getBasis():
            raise ValueError("The state %s has no basis assigned"%self)
            sys.exit(1)
    def isBasisVector(self):
        return True if self.basis_vector != False else False
    def isComposed(self):
        return False if self.isBasisVector() else False
    def setBasis(self, basis):
        self.basis = basis
    def getVector(self):
        if self.isBasisVector():
            return self.getBasis().getElementsVector(self.basis_number)
        else:
            print("To do")
    def getFunction(self):
        if self.isBasisVector():
            return self.getBasis().getElementsFunction(self.basis_number)
        else:
            print("To do")
    def getBasis(self):
        self.__check_basis()
        return self.basis
    def getComponents(self):
        return self.components


class Spin(State):
    def __init__(self, l, m):
        self.l     = l
        self.m     = m
        self.basis = None
    def getComponents(self):
        return self.getBasis().getElementBySpinNumber(self.l, self.m)
    def getFunction(self):
        return self.getBasis().getElementBySpinNumber(self.l, self.m)


class Orbital(State):
    def __init__(self, parameters=[]):
        self.parameters      = parameters


