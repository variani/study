## JAGS & rjags

### Debian package

1) Install JAGS from an Ubuntu rep

```
add-apt-repository ppa:marutter/rrutter
apt-get update
apt-get install jags 
```

via http://stackoverflow.com/q/7250533

2) rjags R package

```
install.packages("rjags")
```

3) Test JAGS

Actual testing of [BayesianFirstAid](https://github.com/rasmusab/bayesian_first_aid) R package.

```
library(testthat)
test_package("BayesianFirstAid")
```

Expected output:

```
> test_package("BayesianFirstAid")
bayes.binom.test : ..........
bayes.cor.test : ..........
bayes.poisson.test : ..................
bayes.prop.test : ...........
bayes.t.test : ..............................

Warning messages:
1: In bayes.binom.test(6, 11, p = 0.84, alternative = "two.sided",  :
  The argument 'alternative' is ignored by bayes.binom.test
2: In bayes.prop.test(smokers, patients, p = c(0.1, 0.2, 0.3, 0.4),  :
  The argument 'alternative' is ignored by bayes.prop.test
3: In bayes.prop.test(smokers, patients, p = c(0.1, 0.2, 0.3, 0.4),  :
  The argument 'correct' is ignored by bayes.prop.test
```


### Source

A more tricky was is to install JAGS from source: http://mcmc-jags.sourceforge.net/.

Further nstallation of rjags R package becomes complicated (paths, shared libs, etc).

See https://cran.r-project.org/web/packages/rjags/INSTALL.
