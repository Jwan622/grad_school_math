1. "The weekly demand for propane gas (in 1000s of gallons) from a particular facility is an rv X, with the pdf on page 151 exercise number 22. Which of the following is the cdf of X in the interval 1 <= x <= 2."

topic: cdf

work:

To find the cumulative distribution function (CDF) of X for the interval 1 ≤ x ≤ 2 based on the given probability density function (pdf), we need to integrate the pdf over the interval from the lower bound (which is 1) to x.

since the pdf is only defined for 1 ≤ x ≤ 2, we cannot find the cdf for x < 1. Instead, we will find the cdf for the interval [1, x]:F(x) = P(X ≤ x) = 
∫[pdf(t) dt] from 1 to x
Now, we will compute the integral:
F(x) = ∫[2(1 - 1/t^2) dt] from 1 to x (reember integral of 1/t^2 is just - 1/t) 
F(x) = [2t + 2/t] from 1 to x
then plug in x and 1
F(x) = (2x + 2/x) - (2 + 2/1) 
F(x) = 2x + 2/x - 4
So, the cdf of X for the interval 1 ≤ x ≤ 2 is:

answer:
F(x) = 2x + 2/x - 4

that's the cdf given the pdf in the question./

2. "The article 'Reliability of Domestic-Waste Biofilm Reactors' (J. of Envir. Engr., 1995: 785-790) suggests that substrate concentration (mg/cm^3) of influent to a reactor is normally distributed with mu = .30 and sigma = .06. Which statement characterizes the largest 5% of all concentration values?"

work:

The 95th percentile of a normal distribution corresponds to a point where 95% of the data falls below it. This percentile can be found using the z-score associated with 95% in a standard normal distribution, which is typically around 1.645. This value means that 95% of the values are below the z-score of 1.645 and the top 5% are above it.

Given the normal distribution has a mean (mu) of 0.30 and a standard deviation (sigma) of 0.06, you can calculate the 95th percentile using the z-score and these parameters.

The formula to calculate the value at the 95th percentile (c) is:

c = μ + (z × σ)

where
z is the z-score corresponding to the 95th percentile.

The question provides us with two possible z-scores: +1.645 and -1.645. Since we are looking for the 95th percentile, which is in the upper tail of the distribution, we will use the positive z-score, which is +1.645.

Now, let's use the positive z-score to calculate the concentration value for the 95th percentile: we're finding the actual value

c =  0.30 + (1.645 × 0.06)

Let's compute this.
The concentration value at the 95th percentile, using the z-score of 1.645, is 0.3987 mg/cm³. Therefore, the largest 5% of all concentration values are above 0.3987 mg/cm³.

answer:
The correct statement is:
"The 95th percentile of the standard normal distribution satisfies Phi(z) = .95, from which z = 1.645. So, c = .30 + (1.645)(.06) = .3987. The largest 5% of all concentration values are above .3987 mg/cm³."

3. Construct a normal probability plot for the data found on page 187 problem 88. Which statement is true about the probability plot?
Group of answer choices

work:
![chap4_homework_golfers.png](../images/chap4_homework_golfers.png)

4. "Suppose the reaction temperature X (in degrees Celsius) in a certain chemical process has a uniform distribution with A = -5 and B = 5. For k satisfying -5 < k < k + 4 < 5, compute P(k < X < k + 4)."

work: for a uniform distribution, the PDF is given by f(x) = 1/(b-a)
The uniform is just a straight line so take the width of the interval which is 4 over the width of the total distribution which si 10.

it's 4/10 = 0.4

answer:
0.4
5. Suppose the reaction temperature X (in degrees Celsius) in a certain chemical process has a uniform distribution with A = -5 and B = 5. Compute P(X < 0).

topic: uniform distribution

work:
the probability that X is less than 0 is the length from the lower bound to 0, divided by the total length of the distribution:

P(X < 0)= (0 - (-5)) / (5 − (−5)) = 5/10 = 0.5

answer:
0.5

6. "Let X denote the vibratory stress (psi) on a wind turbine blade at a particular wind speed in a wind tunnel. The article 'Blade Fatigue Life Assessment with Application to VAWTS' (J. of Solar Energy Engr., 1982: 107-111) proposes the Rayleigh distribution, with the pdf given on page 142 exercise number 4 as a model for the X distribution. Suppose theta = 100 (a value suggested by a graph in the article). What is the probability that X is at most 200? Compute to at least four decimal places."

topic: integral, cdf, calculus, u-sub

work:
The CDF is obtained by integrating the PDF from 0 to x.
plug in theta = 100 into the pdf function first. and then integrate using u-substitution

![chap4_assignment_problem_variance.png](../images/chap4_assignment_problem_variance.png)

7. "Let X denote the vibratory stress (psi) on a wind turbine blade at a particular wind speed in a wind tunnel. The article 'Blade Fatigue Life Assessment with Application to VAWTS' (J. of Solar Energy Engr., 1982: 107-111) proposes the Rayleigh distribution, with the pdf given on page 142 exercise number 4 as a model for the X distribution. Suppose theta = 100 (a value suggested by a graph in the article). Suppose theta = 100 (a value suggested by a graph in the article). What is the probability that x is at least 200? Compute to at least four decimal places."

work:
![chap4_assignment_cdf_problem.png](../images/chap4_assignment_cdf_problem.png)


8. "The weekly demand for propane gas (in 1000s of gallons) from a particular facility is an rv X, with the pdf on page 151 exercise number 22; Compute V(X) to at least four decimal places."
compute variance and show work.
work:
Notice that the EV multiple the pdf by X to get the EV. and then E(X^2) is found by multiplying the pdf by X^2

![chap4_assignment_variance.png](../images/chap4_assignment_variance.png)
![chap4_assignment_variance_pdf.png](../images/chap4_assignment_variance_pdf.png)

9."The weekly demand for propane gas (in 1000s of gallons) from a particular facility is an rv X, with the pdf on page 151 exercise number 22; Obtain an expression for the (100p)th percentile. What is the value of mu-tilda? Compute to at least two decimal places."

pg 147 in the book has a similar example

work:
In the context of probability and statistics, q represents the value at which a certain percentage of the probability distribution lies to the left of it. The cumulative distribution function (CDF) represents the probability that a random variable 

X will take a value less than or equal to q.

So when we integrate the probability density function (pdf) up to a certain point q, we are effectively calculating the probability that the random variable X is less than or equal to q. This integral gives us the CDF F(q).

For finding percentiles, including the median, we set the value of the CDF F(q) to the desired percentile in decimal form. The median is the 50th percentile, which is represented by 0.5 in decimal. Therefore, we solve the equation 

F(q)=0.5 to find the value of q that is the median. This value of q is the point at which half the probability mass is on either side, and thus, 50% of the observations fall below this value.

![chap4_integration_median_problem_9.png](../images/chap4_integration_median_problem_9.png)


10. Let Z be a standard normal random variable and calculate P(0 <= Z <= 1) to at least four decimal places.

work:

The probability P(0 ≤ Z ≤ 1) for a standard normal random variable Z can be found using the cumulative distribution function (CDF) of the standard normal distribution, denoted as The probability P(0≤Z≤1) is the difference between the CDF evaluated at 1 and the CDF evaluated at 0:

P(0 ≤ Z ≤ 1)= Φ(1) − Φ(0)

0.8413 - 0.5000 P(0 <= Z <= 1) ≈ 0.3413

answer:
0.3413


11. Let Z be a standard normal random variable and calculate P(0 <= Z <= 2.17) to at least four decimal places.

work:


To calculate the probability for a standard normal random variable, you can use a standard normal table or a calculator with a standard normal function. Using a standard normal table or calculator, we can find the following values: P(Z <= 2.17) ≈ 0.9849 and P(Z < 0) = 0.5000. Now, subtract P(Z < 0) from P(Z <= 2.17) to find the probability between 0 and 2.17: 
P(0 <= Z <= 2.17) = 
P(Z <= 2.17) - P(Z < 0)
so 
P(0 <= Z <= 2.17) = 0.9849 - 0.5000 
P(0 <= Z <= 2.17) ≈ 0.4849
So, the probability that a standard normal random variable falls between 0 and 2.17 (inclusive) is approximately 0.4849, to at least four decimal places.

answer:
0.4849

12. Let Z be a standard normal random variable and calculate P(1.50 <= Z) to at least four decimal places.

work:
Notice that z is greater than 1.50 so we need to do 1 - P(z <= 1.50)
To calculate the probability for a standard normal random variable, you can use a standard normal table or a calculator with a standard normal function.

Using a standard normal table or calculator, we can find the following value:
P(Z <= 1.50) ≈ 0.9332

So, the probability that a standard normal random variable is less than or equal to 1.50 is approximately 0.9332, to at least four decimal places.

P(1.50 <= Z) = 1 - P(Z <= 1.50)
P(1.50 <= Z) = 1 - 0.9332
P(1.50 <= Z) ≈ 0.0668

answer:
 0.0668

So, the probability that a standard normal random variable is greater than or equal to 1.50 is approximately 0.0668, to at least four decimal places.

14.  "The article 'Reliability of Domestic-Waste Biofilm Reactors' (J. of Envir. Engr., 1995: 785-790) suggests that substrate concentration (mg/cm^3) of influent to a reactor is normally distributed with mu = .30 and sigma = .06. What is the probability that the concentration exceeds .25? Compute to at least four decimal places.

work:
Z = X − μ / stddev

we first need to standardize the normal distribution. The given mean (μ) is 0.30 and the standard deviation (σ) is 0.06 where

X is the concentration value of interest (0.25 mg/cm³ in this case)
μ is the mean concentration (0.30 mg/cm³), and
σ is the standard deviation (0.06 mg/cm³).

After calculating the Z-score, we can find the probability that the concentration exceeds 0.25 mg/cm³ by calculating 1 - zi(Z) since we're trying to find the upper bound 

(Z) is the cumulative distribution function (CDF) for the standard normal distribution at the calculated Z-score.

Let's calculate the Z-score for 
X = 0.25 mg/cm³ and then find the corresponding probability.

The Z-score for a concentration of 0.25 mg/cm³ is approximately -0.8333. Therefore, the probability that the concentration exceeds 0.25 mg/cm³ is approximately 0.7977 to at least four decimal places.

answer: 0.7977

15. "The Rockwell hardness of a metal is determined by impressing a hardened point into the surface of the metal and then measuring the depth of penetration of the point. Suppose the Rockwell hardness of a particular alloy is normally distributed with mean 70 and standard deviation 3. (Rockwell hardness is measured on a continuous scale.) If the acceptable range is between 67 and 75 and the hardness of each of ten randomly selected specimens is independently determined, what is the expected number of acceptable specimens among the ten? Compute to at least three decimal places."

work:

To find the expected number of acceptable specimens, we first need to find the probability of a specimen being acceptable. An acceptable specimen has a Rockwell hardness between 67 and 75. 
First, let's find the z-scores for the given hardness values (67 and 75) using the standard normal distribution: 
For 67: z1 = (X - μ) / σ z1 = (67 - 70) / 3 
so  z1 ≈ -1
For 75: z2 = (X - μ) / σ z2 = (75 - 70) / 3 
so z2 ≈ 1.67
Now, we can find the probability using a standard normal table or calculator:P(67 <= X <= 75) = 
P(-1 <= Z <= 1.67) 
P(67 <= X <= 75) = 
P(Z <= 1.67) - P(Z <= -1) 
P(67 <= X <= 75) ≈ 0.9525 - 0.1587 
P(67 <= X <= 75) ≈ 0.7938
Now, let's find the expected number of acceptable specimens. Since the hardness of each of ten randomly selected specimens is independently determined, we can multiply the probability of a specimen being acceptable by the number of specimens (10) to find the expected number of acceptable specimens:
Expected number of acceptable specimens = Number of specimens * Probability of a specimen being acceptable 
Expected number of acceptable specimens = 10 * 0.7938 
Expected number of acceptable specimens ≈ 7.94, to at least three decimal places.
So, the expected number of acceptable specimens among the ten is approximately 7.94.

answer:
7.94


16. Suppose that 10% of all steel shafts produced by a certain process are nonconforming but can be reworked (rather than having to be scrapped). Consider a random sample of 200 shafts, and let X denote the number among these that are nonconforming and can be reworked. What is the (approximate) probability that X is Less than 30? Compute to at least four decimal places."

work: To solve this problem, we will use the Central Limit Theorem (CLT) which states that the distribution of the sum (or average) of a large number of independent, identically distributed random variables approaches a normal distribution.

In this case, the number of nonconforming shafts in a sample of 200, X, can be modeled as a binomial random variable with parameters n = 200 (the sample size) and p = 0.1 (the probability of a shaft being nonconforming).

However, for large n and small p, the binomial distribution can be approximated by a normal distribution with mean μ = n*p and variance σ^2 = n*p*(1-p).

So, for X, we have:

μ = n*p = 200 \* 0.1 = 20
σ = sqrt(n*p*(1-p)) = sqrt(200 \* 0.1 \* 0.9) ≈ 4.24

We want to find P(X < 30), but first, we need to standardize X:

Z = (X - μ) / σ = (X - 20) / 4.24

Now, we want to find P(Z < (30 - 20) / 4.24) = P(Z < 2.36) ≈ 0.9909

However, this is a cumulative distribution function (CDF) value for the standard normal distribution. To find the probability that X is less than 30, we need to subtract the CDF value from 1:

P(X < 30) = 1 - P(Z < 2.36) ≈ 1 - 0.9909 = 0.0091

Therefore, the approximate probability that X is less than 30 is 0.0091, or 0.0091 \* 100% = 0.91%, when rounded to four decimal places.
