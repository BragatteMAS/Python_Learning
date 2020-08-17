# -*- coding: utf-8 -*-
"""Statistical_Tests_Py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s7CekFckCab0v_cRIB9LbfxGP6TYFHv-

# Statistical Tests with Python

A statistical test provides a mechanism for making quantitative decisions about a process or processes. It is a way to evaluate the evidence the data provides against a hypothesis.
The flow chart that shows which statistical test to use depending on your data and test requirements.  Focus on how to perform these tests in Python. A statistical test examines two opposing hypotheses about a population: the null hypothesis and the alternative hypothesis. The null hypothesis states that a population parameter (such as the mean, the standard deviation, and so on) is equal to a hypothesized value. The alternative hypothesis states that a population parameter is smaller, greater, or different than the hypothesized value in the null hypothesis.
"""

from IPython.display import Image
##E.g.: to show images
##Exemplo para mostrar imagens
display(Image(filename='/content/stat_map.png'))

"""## One Sample Z test


One sample Z test is used to compare the population mean to a sample. Population standard deviation must be known to perform the Z test and data should be normally distributed.
"""

x = sample mean
mu = population mean
s = population standard deviation
n = sample size
z =  (x - mu)/(s / np.sqrt(n))
p = 1 - stats.norm.cdf(z)[Ref1](https://medium.com/python-in-plain-english/statistical-tests-with-python-880251e9b572)
if p < alpha  # Reject Null Hypothesis
if p > alpha  # Failed to reject Null Hypothesis

"""## One Sample T-test
One sample T-test is used to compare the population mean to a sample. This test is similar to the Z test as it checks the same thing. The difference between these two tests is that the Z test needs population standard deviation but the T-test needs sample standard deviation. If the sample size is greater than 30 One sample T-test is always used regardless of the known population standard deviation.
"""

from scipy import stats
t_stat, pval = stats.ttest_1samp(sample, popmean)
critical_value  = stats.t.ppf(1 - 0.05, df)
If t_stat > critical_value Reject Null Hypothesis
p = 1 - stats.t.cdf(t_stat, df)
If p < alpha # Reject Null Hypothesis

"""## Z test for Proportion

### One-Sample
One-Sample Z test for proportion is used to compare an observed proportion to a theoretical one. The test of proportion can only be performed on categorical data.
"""

p = proportion in sample
p0 = theoretical proportion
z_stat = (p - p0) / np.sqrt(p0 * (1 - p0) / n)
p = 1 - stats.norm.cdf(z)
if p < alpha  # Reject Null Hypothesis
if p > alpha  # Failed to reject Null Hypothesis

"""### Two sample
Two Sample Z test for proportion is used to compare two proportions with a theoretical proportion.
"""

x1 = sample1 mean
x2 = sample2 mean
n1 = sample1 size
n2 = sample2 size
sigma1 = standard deviation of sample1
sigma2 = standard deviation of sample2
delta = hypothesized difference between the population means (0 if testing for equal means)
mu = population mean
s = population standard deviation
n = sample size
z_stat = (x1 - x2 - delta)/np.sqrt((sigma1**2/n1) + (sigma2**2/n2))
p = 1 - stats.norm.cdf(z_stat)
if p < alpha  # Reject Null Hypothesis
if p > alpha  # Failed to reject Null Hypothesis





"""##  Two Samples T-Test
Two sample T-test is used to compare two samples. There are two types of Two-sample T-test, a Paired T-test, and a Pooled T-test.

### Paired T-test
A paired T-test is used when both samples have different variances.
"""

t_stat, pval =  stats.ttest_ind(sample1, sample2, equal_var=False)
critical_value  = stats.t.ppf(1 - 0.05, df)
If t_stat > critical_value Reject Null Hypothesis
p = 1 - stats.t.cdf(t_stat, df)
If p < alpha  # Reject Null Hypothesis

"""### Pooled T-test
The pooled T-test is used when both samples have equal or almost equal variances.
"""

t_stat, pval =  stats.ttest_ind(sample1, sample2)
critical_value  = stats.t.ppf(1 - 0.05, df)
If t_stat > critical_value Reject Null Hypothesis
p = 1 - stats.t.cdf(t_stat, df)
If p < alpha  # Reject Null Hypothesis

"""## Two Sample Z test
Two sample Z test is used to compare the means of two populations.
"""

x1 = sample1 mean
x2 = sample2 mean
n1 = sample1 size
n2 = sample2 size
sigma1 = standard deviation of sample1
sigma2 = standard deviation of sample2
delta = hypothesized difference between the population means (0 if testing for equal means)
mu = population mean
s = population standard deviation
n = sample size
z_stat = (x1 - x2 - delta)/np.sqrt((sigma1**2/n1) + (sigma2**2/n2))
p = 1 - stats.norm.cdf(z_stat)
if p < alpha  # Reject Null Hypothesis

"""## Chi-Squared Test
The chi-squared test is used to compare the relationship between the two categorical (nominal) variables in a contingency table. There are three kinds of chi-squared tests: the test of independence, the goodness of fit, and the test of homogeneity. This test is applied to a contingency table of values in the dataset.
"""

from scipy.stats import chi2_contingency
table = np.array([[16, 18, 16], [32, 24, 16]]).T #contingency table
stat, p, dof, expected = chi2_contingency(table)
critical_value = chi2.ppf(0.95, dof)
if stat >= critical_value # Reject Null Hypothesis
if p <= alpha # Reject Null Hypothesis

"""## ANOVA
ANOVA test is used to compare means between three or more variables. It is the same as Independent T-test for two samples.
"""

from statsmodels.formula.api import ols
import statsmodels.api as sm
anova = ols('var1~var2', data=data).fit()
anova_table = sm.stats.anova_lm(anova, type=2)
print(anova_table)

'''
                     df        sum_sq           mean_sq             F               PR(>F)
var2              3.0    9.5059e+08   3.1686e+08   128.769622  6.720391e-67
Residual        727.0  1.7889e+09  2.4607e+06         NaN           NaN
p_value = 6.720391e-67
p_value <<<<< alpha
Reject Null Hypothesis
'''

"""[Ref](https://medium.com/python-in-plain-english/statistical-tests-with-python-880251e9b572)
[Ref2](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/)
"""