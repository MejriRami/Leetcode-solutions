hamming <- function(strand1, strand2) {
  # Check that strands have equal length
  if (nchar(strand1) != nchar(strand2)) {
    stop("Strands must be of equal length")
  }
  
  # Split the strings into individual characters
  s1 <- strsplit(strand1, "")[[1]]
  s2 <- strsplit(strand2, "")[[1]]
  
  # Count positions where characters differ
  distance <- sum(s1 != s2)
  
  return(distance)
}
