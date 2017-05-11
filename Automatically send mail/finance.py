def npv_f(rate, cashflows):
    '''
    net present value is defined as different between the present value of  all the benefit and cost.
    :param rate:
    :param cashflows:every year cashflow
    :return:
    '''

    total = 0
    for i, cashflows in enumerate(cashflows):
        total += cashflows/(1+rate)**i
    return total


def IRR_f(cashflows, interations=100):
    '''
    IRR is the discount rate resulting in a zero NPV(项目流入现金额与流出现金的现值相等的利率)
    :param cashflows:
    :param interations:
    :return:
    '''
    rate = 0.1
    investment = cashflows[0]
    for i in range(1, interations+1):
        rate *= (1-npv_f(rate, cashflows)/investment)
        # print(i, rate)
    return rate

cashflows = [-100, 20, 40, 50, 20, 10]
print(IRR_f(cashflows))

# 13 lines of python to price a call option(期货理论)
from math import *


def bs_call(S, X, T, r, sigma):
    '''

    :param S:is the current stock prices
    :param X:is the exercise price(a fixed price)
    :param T:is the maturity(the years)
    :param r:is continuously compounded risk-free rate
    :param sigma:is the volatility of the underlying security(such as stock)
    :return:
    '''
    d1 = (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*CND(d1)-X*exp(-r*T)*CND(d2)


def CND(X):
    (a1, a2, a3, a4, a5) = (0.31938153, -0.356563782, 1.781477937, -1.821255978, 1.330274429)
    L = abs(X)
    K = 1.0/(1.0+0.2316419*L)
    w = 1.0 - 1.0 / sqrt(2 * pi) * exp(-L * L / 2.) * (a1 * K + a2 * K * K + a3 * pow(K, 3) + a4 * pow(K, 4) +
                                                       a5 * pow(K, 5))
    if X < 0:
        w = 1.0-w
    return w
print(bs_call(40, 42, 0.5, 0.1, 0.1))
# bs_call(40,42,0.5,0.1,0.2)



