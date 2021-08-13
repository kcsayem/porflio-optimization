# porflio-optimization-advanced-investment-science
This is the project done in the course Advanced Investment Science. Here I had made two portfolios for a hypothetical client who is teaching English in Korea to pay his college debt. He can do invest of $50K but of which $30K has to be paid as the loan. And from rest $20K, he wants to start a new business after going back to the US. He doesn’t want to take very high risk on the $30K portion but he is okay to take risk in $20K if there is around 6% annual return. One of the portfolios done with Robust Portfolio optimization &amp; I applied algorithmic trading strategies in other. But it was giving less profit than just holding the asset. Therefore, I then decided to continue with holding the portfolio made by markowitz portfolio.

### Used Data Details
        Stocks Used: the dow jones industrial average stocks
        Bonds: 10 years US Treasury Bonds
        Data from 2009 to 2017 were used to make portfolios.
        Data of 2018 were used to test the portfolios
        Investment was done in year 2019.
        Data is collected from yahoo finance. 
        (I ignored data after 2019 data due to the volatile nature of stock for covid 19 situation)

### Overall portfolio Report
        Portfolio 1: 
            Invested = $30000
            Cumulative Return = 31.73 %
            Final = $39519
        Portfolio 2:
            Invested = $20000
            Cumulative Return = 48.99 %
            Final = $29798
        Total Portfolio Value = $69317
        Total Portfolio Growth = 38.63%


## Steps of Optimizing portfolio:

**Calculating daily return & risk:**

- Return was calculated using log return.
- Standard deviation is taken as the risk parameter.

**For the first portfolio, I have used Robust portfolio optimization, as the client wanted an investment with minimal risk.**
 - In portfolio 1, I have added bonds as client wanted it to be least risky. 
 
 **Return Data Frame:**

![Screenshot](screenshots/return-data-frame.png)


This is the return data frame & last column is the 10 years US treasury bond.

**Equation of Robust Portfolios under box uncertainity**

![Screenshot](screenshots/robust-theory.png)

**Implementation of Robust Portfolios**

![Screenshot](screenshots/implementation-robust.png)

Here is the code been used to do the robust portfolio optimization. Points to be noticed here, in the
robust_opt function there are **two parameters tuner & lambda 0** which are used to **optimize value of
delta & lambda** later. mu, Sigma & delta have been calculated using the functions below,


![Screenshot](screenshots/helper-robust-theory.png)

To optimize the robust portfolio, i.e. finding the optimal value for the tuner & lambda 0 following code
was used,

![Screenshot](screenshots/optimize-robust-theory.png)

First, I took values for lamda & tuner to test in the range of 0.1 to 3 with 0.1 difference. Then I ran a loop
using these value & saved the expected return & standard deviation in a pandas data frame.

![Screenshot](screenshots/robust-theory-optimization-result.png)

After that, I sorted the value where we can get the most expected return with least possible standard
deviation. So, I took the 1st row’s value for tuner & lamda shown in the screenshot. That gave following weights for stocks & bonds

![Screenshot](screenshots/robust-theory-weights.png)

After taking the mentioned lambda & tuner, robust optimization almost assigned 99% of the weight in
the stocks. The value was similar almost in every case of the value of lambda & tuner.

To test the portfolio strategy & simulate return for the portfolio, I have used empyrial library. Simulated
return for next 156 days after 2017 December 31st is given below,

![Screenshot](screenshots/robust-theory-pred.png)

