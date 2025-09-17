rotate <- function(input, key) {
  shift_letter <- function(char, key) {
    if (grepl("[a-z]", char)) {
      # Lowercase letter
      shifted <- ((utf8ToInt(char) - utf8ToInt("a") + key) %% 26) + utf8ToInt("a")
      return(intToUtf8(shifted))
    } else if (grepl("[A-Z]", char)) {
      # Uppercase letter
      shifted <- ((utf8ToInt(char) - utf8ToInt("A") + key) %% 26) + utf8ToInt("A")
      return(intToUtf8(shifted))
    } else {
      # Non-letter, keep unchanged
      return(char)
    }
  }
  
  chars <- strsplit(input, "")[[1]]
  result <- sapply(chars, shift_letter, key = key)
  paste(result, collapse = "")
}
