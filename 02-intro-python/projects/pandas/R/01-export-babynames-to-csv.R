library(babynames)

write.csv(babynames, "babynames.csv", quote = FALSE, row.names = FALSE) # file size ~ 80M
