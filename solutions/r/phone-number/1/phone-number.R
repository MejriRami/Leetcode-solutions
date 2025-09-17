parse_phone_number <- function(number_string) {
  # Remove all non-digit characters
  digits <- gsub("[^0-9]", "", number_string)
  
  # Remove leading 1 if present and length is 11
  if (nchar(digits) == 11 && substr(digits, 1, 1) == "1") {
    digits <- substr(digits, 2, 11)
  }
  
  # Check for valid length
  if (nchar(digits) != 10) {
    return(NULL)
  }
  
  # Check NANP rules: NXX NXX-XXXX
  area_code <- as.integer(substr(digits, 1, 1))
  exchange_code <- as.integer(substr(digits, 4, 4))
  
  if (!(area_code %in% 2:9 && exchange_code %in% 2:9)) {
    return(NULL)
  }
  
  return(digits)
}

