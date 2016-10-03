# Exercises  from Little Inference Book
Andrey Ziyatdinov  
`r Sys.Date()`  



# Include


```r
library(tidyverse)
```

## Simulation example 1: standard normals

[link](https://leanpub.com/LittleInferenceBook/read#leanpub-auto-simulation-example-1-standard-normals)


```r
nosim <- 1000
n <- 10
mat <- matrix(rnorm(nosim * n), nosim)
dim(mat)
```

```
[1] 1000   10
```

```r
means <- apply(mat, 1, mean)
length(means)
```

```
[1] 1000
```

```r
sd(means)
```

```
[1] 0.3144809
```


```r
nsim <- 1000
n <- 10

sim_means <- 
  rep(n, nsim) %>%
  sapply(. %>% rnorm %>% mean)

sim_means_sd <- sim_means %>% sd
```
 
