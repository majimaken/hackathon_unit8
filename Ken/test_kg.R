# Challenge 2

# Packages
library(randomForest)

# Data prep
setwd("~/GitHub/Ken")
train <- read.csv("data2_train.csv")
test <- read.csv("data2_test.csv")

# Transpose
train <- t(train)
test <- t(test)

# Index
colnames(train) <- train[1,]
train <- train[-1,]
train <- as.data.frame(train)

colnames(test) <- test[1,]
test <- test[-1,]
test <- as.data.frame(test)

# Set factors
train$`1` <- as.factor(train$`1`)
train$`18` <- as.factor(train$`18`)
train$label <- as.factor(train$label)

test$`1` <- as.factor(test$`1`)
test$`18` <- as.factor(test$`18`)

names(train) <- make.names(names(train))
names(test) <- make.names(names(test))
rownames(train) <- make.names(rownames(train))
rownames(test) <- make.names(rownames(test))

# Train rfm
head(train)
head(test)

rfm <- randomForest(label~., data = train)
plot(rfm)

pred.val  <- predict(rfm, newdata = test, type = "class")
