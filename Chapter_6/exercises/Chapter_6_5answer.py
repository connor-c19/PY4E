## PROMPT ##
"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475"

## Find index for everything after "X-DSPAM-Confidence:"

result_start_index = text.find(":")

## Get substring containing "X-DSPAM-Confidence" score

result = text[result_start_index+1:]

## Strip whitespace

stripped_result = result.strip()

## Convert to float

float_result = float(stripped_result)

## Print float

print(float_result)










## NOTES ##
# Desired input:
# Desired output: 0.8475