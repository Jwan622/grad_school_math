# Topics
- hypothesis testing


# Quick Review

This margin of error is calculated as the product of the critical value from the Z-distribution (which corresponds to the desired confidence level) and the standard error of the sample statistic, which is the sample standard deviation divided by the square root of the sample size (s/sqrt(n)).

The formula in the spreadsheet (Z critical value * s/sqrt(n)) is the calculation of the margin of error. The critical value depends on the desired confidence level — for a 95% confidence interval, the Z critical value is approximately ±1.96. In your case, the critical value seems to be ±1.6448536, which is the critical value for a 90% confidence interval (this doesn't align with the 95% confidence level mentioned). The margin of error is used to calculate the upper and lower bounds of the confidence interval around the sample mean.

# Notes

this is how you have evidence that something is true
data that falls outside the assumption might make us question our assumptions

That's the point of a hypothesis test
- we make an assumption
- we test it against data
- either we reject or accept the assumption/hypothesis

We call the hypothesis a null hypothesis denoted by `H_0`


## Errors
In social sciences, we set an arbitrary value of p is 0.05. So 1/20 times we make a mistake in our assumption and we reject. 

**Type 1 Error** - probability that we reject the assumption given that it's true. 
- The tail probability happens sometimes 1/20 and we conclude the assumption is bad even thoug the data actually did come from the distribution. Also called a false negative

**Type 2 Error** - probability that we don't reject the assumption but it's false. The assumption is actually different but the data did not fall outside of 0.05 of the tails.

If you get a observed value that only has a probability of 0.01 and since 0.01 < 0.05 threshold, then you can say the data didn't come from the distribution assumed, so you can reject the null hypothesis.


If the data is within range, you cannot prove that null hypothesis is correct. All we can do is say the probability is unlikely that the null is true or that the null is false. Can't prove or disprove.
- the 0.05 is arbitrary btw. It's the cutoff to reject.


## Steps to hypothesis test
![chap8_hypothesis_testing_steps.png](images/chap8_hypothesis_testing_steps.png)


## range of rejection
a prof says it's an outdated way to think about statistics. but he does pay attention to the magnitude of the p value. If it's super small, that does tell you something about the unlikelihood of the null hypothesis.
- don't really use rejection regions anymore in the world.... it's outdated.
