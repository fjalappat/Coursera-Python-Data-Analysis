[MUSIC] In this video, we will model stock
return using normal random variable and demonstrate the importance of distribution
in identifying financial risk. Why it is important to know the
distribution or model for stock return. It is really crucial in risk management. For example,
the stock price of Apple drop over 40% from August 2012 to May 2013,
roughly one year. We need to compute what's the chance
that the yearly return can be less than negative 40%. Is that possible, or
just an extreme case like black swan. We compute log daily return for
stock price of Apple. The histogram of a return is symmetric and
bell shaped, which is very similar
to normal distribution. Using scipy which is a scientific
computation package of python, we can get density function and
a cumulative distribution function. norm.pdf where a given density for each possible value of
a normal random variable. In fact normal random
variable can take values from positive infinity to negative infinity. In Python code here, we get the density
between -4 and 4 for simplicity. Two parameters 0, 1 in
norm.pdf gives the mean and the standard deviation of
a normal random variable. This normal random variable is also
called a standard normal random variable, and its distribution is
also called z-distribution. You can change these two values in order
to get a different normal variables. Because, 
>> **the density functions of
a normal variables are only related to their mean and their variance.** 
We also can get a **cumulative distribution function, or in short a CDF which outputs the probability for the area**, and lower side of each possible value. 

``On the left side of this slide is the graph for normal density, symmetric with a mean and symmetric center. It is also bell shaped. On the right side that is cumulative distribution function, where x takes large values.``

**The cumulative probability will approach 1.** 

We can model daily stock return using normal distribution. We do not know the real mean and standard
deviation of this normal random variable. We have a large collection of
data return from historic data. We can compute the mean and
the standard deviation in this collection. They are not the same as
those of normal variable, but close enough, as this shown on the right. Then, what is the chance data
loss can be more than 5%? First, we will plot the normal
density curve for this daily return. This pink area is the probability
of losing more than 5% in one day. We can use CDF to get this probability,
which is 0.5%. Hence we have 0.5% chance to
have a daily loss more than 5%. Our goal is to find out how
likely that the stock price of Apple were dropped over 40%,
1 year which has 220 trading days. We will use another normal
distribution to model yearly return. We need to figure out the mean and
the standard deviation of a yearly return. **We make assumption that
the daily returns are independent, which is quite wrong.**
But it can simplify our discussion here, to get the mean and variance of a year return. We have formulas for sum of variables. We need the independence when we compute the variance. If the data returns independent the variance of a unit return is equal to the sum of a variance of 220 daily return. Again, with no CDF we compute a probability, and it is less than 2%. That implies,
there's only less than 2% chance to have yearly loss to be more than 40%. What happened to Apple in 2012 and 2013? Is not consistent with
its overall performance. In many circumstances, we need to solve a different type
of problem with distribution. For example, 
> finding quantiles of
a normal distribution is a common task when performing statistical test
in the financial risk management. *Normal distribution quantiles
can obtain using norm.ppf*. *Ppf stands for percent point function*. 
>> **In finance related to the quantile there is an important risk measure value of risk or VaR.** It estimates **how much a set of investments might lose with a given probability.** 

>> VaR is typically used by firms and the regulators in the financial industry to **gauge the amount of assess needed to cover possible loss.**

For example, 5% of quantile of daily return is called a 95% VaR or
VaR at the level of 95%. We can use a ppf to get a 5% of
quantile which is negative 0.03. hence, 95% of VaR is negative 0.03, it means with the 5% chance that daily return is worse than -3%. 
Is it safe to use normal distribution to model stock return?
> Two famous professors in the field asset pricing, **Fama and French** responds in this way. *Distribution of a daily and monthly stock return, are rather symmetric about their means, but the tails are fatter.* 
Which means there are more outliers that would be expected with normal distributions. 
>> It means that, if tail returns negative, as well as positive,
may occur more often than we expect. If we use normal distribution,
this is debatable, at least for the returns of some assets
with different time window size. 

>> To modal a fat tail, people proposed modal return using **t-distributions with low degree of freedom.** We will discuss and use t-distribution
in the next several topics.