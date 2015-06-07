#! /usr/bin/python
class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __sub__(self,otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __div__(self,otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(self,otherfraction)
        return Fraction(newnum//common,newden//common)

    def __eq__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum == secondnum)

    def __lt__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum < secondnum)

    def __gt__(self,otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num
        return (firstnum > secondnum)



def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
