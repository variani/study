# Model, Bernoulli distribution
Andrey Ziyatdinov  
`r Sys.Date()`  



### Parameters


```r
nsteps <- 5000
```

## Include


```r
library(rjags)
library(coda)
```

## Data


```r
dat <- data.frame(y = c( rep(1,9), rep(0,3), rep(1,45), rep(0,15), rep(1,3),rep(0,9)),
  s = c(rep("A",12), rep("B",60), rep("C",12)))

str(dat)
```

```
'data.frame':	84 obs. of  2 variables:
 $ y: num  1 1 1 1 1 1 1 1 1 0 ...
 $ s: Factor w/ 3 levels "A","B","C": 1 1 1 1 1 1 1 1 1 1 ...
```

```r
table(dat$s)
```

```

 A  B  C 
12 60 12 
```

## Model


```r
data <- dat

y <- data$y
s <- as.numeric(data$s)

Ntotal <- length(y)
Nsubj <- length(unique(s))

# Data list to be passed to JAGS
dataList = list(y = y, s = s, Ntotal = Ntotal, Nsubj = Nsubj)

# The model string written in the JAGS language
model <- "model {
  for(i in 1:Ntotal) {
    y[i] ~ dbern( theta[s[i]] )
  }
  
  for(sIdx in 1:Nsubj) {
    theta[sIdx] ~ dbeta(2, 2)
  }
}
"

numSavedSteps <- nsteps

parameters <- c("theta")     # The parameters to be monitored
adaptSteps <- 500            # Number of steps to adapt the samplers
burnInSteps <- 500           # Number of steps to burn-in the chains
nChains <- 4                 # nChains should be 2 or more for diagnostics 

thinSteps <- 1
nIter <- ceiling((numSavedSteps * thinSteps) / nChains)

# Create, initialize, and adapt the model:
jagsModel <- jags.model(textConnection(model), data = dataList, 
  n.chains = nChains, n.adapt = adaptSteps)
  
# Burn-in:
update( jagsModel, n.iter = burnInSteps)

# The saved MCMC chain:
samples = coda.samples(jagsModel, variable.names = parameters, 
  n.iter = nIter, thin = thinSteps)

# resulting codaSamples object has these indices: 
#   codaSamples[[ chainIdx ]][ stepIdx , paramIdx ]
```

## Extract summaries

### Summary of coda samples


```r
summary(samples)
```

```

Iterations = 501:1750
Thinning interval = 1 
Number of chains = 4 
Sample size per chain = 1250 

1. Empirical mean and standard deviation for each variable,
   plus standard error of the mean:

           Mean      SD  Naive SE Time-series SE
theta[1] 0.6893 0.11117 0.0015721      0.0015523
theta[2] 0.7343 0.05451 0.0007708      0.0007611
theta[3] 0.3121 0.11120 0.0015726      0.0015629

2. Quantiles for each variable:

           2.5%    25%    50%    75%  97.5%
theta[1] 0.4492 0.6169 0.6974 0.7723 0.8786
theta[2] 0.6228 0.6990 0.7377 0.7723 0.8320
theta[3] 0.1166 0.2296 0.3069 0.3847 0.5462
```


