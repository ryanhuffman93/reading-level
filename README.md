# reading-level

## About
This was a python project I worked on as part of a problem set provided in the CS50 course Harvard provides online. A full description of the problem set can be found at https://cs50.harvard.edu/college/2020/spring/psets/2/readability/.

## Purpose
The purpose of this project was to take an input paragram and apply the Coleman-Liau index to it to output what US grade level
is needed to understand the text. Any text that has a reading level of less than 1 should result in 'Before Grade 1' and any text
with a reading level of 16 or above would result in 'Grade 16+'.

Coleman-Liau formula = 0.0588 * L - 0.296 * S - 15.8

L = The average number of letters per 100 words

S = The average number of sentences per 100 words

## Testing
The following input strings should have the results as follows:

"One fish. Two fish. Red fish. Blue fish." (Before Grade 1)

"Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard." (Grade 5)

"It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him." (Grade 10)

"A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains." (Grade 16+)
