library(data.table)

dt <- fread('../../gen/data-preparation/output/dataset.csv')

# tag retweets
dt[, retweet:=FALSE]
dt[grepl('^RT', text), retweet:=TRUE]

dir.create('../../gen/analysis/temp/', recursive = TRUE)

fwrite(dt, '../../gen/analysis/temp/preclean.csv')


