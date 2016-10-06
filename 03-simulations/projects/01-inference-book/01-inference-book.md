# Exercises  from Little Inference Book
Andrey Ziyatdinov  
`r Sys.Date()`  



# Include


```r
library(pander)

library(tidyverse)
```

## Settings



```r
theme_set(theme_light())

panderOptions('table.style', 'rmarkdown')

panderOptions('table.split.table', Inf)
panderOptions('knitr.auto.asis', FALSE)
```

# Simulations

## The standard error of the mean

What is the variability of the mean of a sample, if we get only a single realization?
(Spoiler: $\sigma^2 / n$.)
[Simulation](https://leanpub.com/LittleInferenceBook/read#leanpub-auto-simulation-example-1-standard-normals)
with repeated sample avergaging can answer the question.

Before going to the code, a small recap:

* The sample variance, $S^2$, estimates the population variance, $\sigma^2$.
* The distribution of the sample variance is centered around $\sigma^2$.
* The variance of the sample mean is $\sigma^2 / n$.


```r
nsim <- 1000
n <- 10

set.seed(1)

sim_means <- 
  rep(n, nsim) %>%
  sapply(. %>% rnorm %>% mean)
  
sim_means_sd <- sim_means %>% sd
```


|          method          |   sd   |
|:------------------------:|:------:|
|   theory: 1 / sqrt(n)    | 0.3162 |
| simulation: sim_means_sd | 0.3233 |


```r
ggplot(data.frame(mean = sim_means), aes(mean)) + geom_histogram() + 
  geom_vline(xintercept = c(-sim_means_sd, sim_means_sd)) 
```

![](figures/ex1_hist-1.png) 
 
