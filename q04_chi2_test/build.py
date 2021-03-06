# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    crosstab = pd.crosstab(df['LandSlope'], price)
    chi2,pval,dof,expected = stats.chi2_contingency(crosstab)
    return pval, pval < 0.1
