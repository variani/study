### par
n <- 100
beta <- c(3, 2, 1)

### simulate data
set.seed(1)

x0 <- rep(1, n)
x1 <- cbind(rnorm(n, 0, 2))
x2 <- cbind(rnorm(n, 0, 1))
X <- cbind(x0, x1, x2)

error <- cbind(rnorm(n, 0, 2)) # Noise

y <- X %*% beta + error # Linear Regression Model

### model
mod <- lm(y ~ -1 + X)
