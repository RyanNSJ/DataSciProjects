## 2. Assigning a Value to a Variable ##

# This is a comment, and so is any line that starts with a #
# Comments provide helpful information about the code

# Assign the value 10 to the variable bearAwesomeness
bearAwesomeness <- 10

# Assign the value 1.5 to the variable guineaPigAwesomeness
guineaPigAwesomeness <- 1.5
dogAwesomeness <- 10
catAwesomeness <- 9.5

## 3. Displaying Results with the Print Function ##

# We can print out values
print(10)

# We can also assign a value to a variable, then print the variable
lifeSavings <- 5.5
print(lifeSavings)
lifeSavings <- 9999
print(lifeSavings)

## 4. Numeric vs. Character Variables ##

# Assign the value 800 to the variable runDistance
runDistance <- 800

# runDistance is of type "numeric"
print(class(runDistance))

# Assign the value "Peanut Butter Cup" to favoriteDessert
favoriteDessert <- "Peanut Butter Cup"

# favoriteDessert is of type "character" because it contains text
print(class(favoriteDessert))

biggestDog <- "Mastiff"
mastiffCount <- 50
biggestDogType <- class(biggestDog)
mastiffCountType <- class(mastiffCount)

## 5. Storing Values as Vectors ##

# Store a vector of Russian presidents
russianPresidents <- c("Mikhail Gorbachev", "Boris Yeltsin", "Vladimir Putin")

# Store a vector of stock prices on consecutive days
applePrices <- c(113, 114, 115)
fibonacci <- c(0, 1, 1, 2)

## 6. Storing Single Values as Vectors ##

dogCount <- 1
catCount <- c(1)

# We can see that these two assignments are identical
# Both dogCount and catCount are vectors
print(identical(dogCount, catCount))
