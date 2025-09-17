# Number of grains on a specific square
square <- function(n) {
  if (n < 1 || n > 64) stop("Square must be between 1 and 64")
  return(2^(n - 1))
}

# Total grains on the chessboard
total <- function() {
  return(2^64 - 1)
}
