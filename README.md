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



