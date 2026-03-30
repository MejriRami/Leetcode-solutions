collatz_step_counter <- function(nums) {
  sapply(nums, function(num) {
    if (!is.numeric(num) || num <= 0 || floor(num) != num) {
      stop("Input must be positive integers")
    }
    
    steps <- 0
    while (num != 1) {
      if (num %% 2 == 0) {
        num <- num / 2
      } else {
        num <- num * 3 + 1
      }
      steps <- steps + 1
    }
    steps
  })
}
