1. "A box contains six 40-W bulbs, five 60-W bulbs, and four 75-W bulbs. If bulbs are selected one by one in random order, what is the probability that at least two bulbs must be selected to obtain one that is rated 75 watts? Specify your answer to 3 decimal places."

Work:
What is the total bulbs: 15
number of bulbs that is not a 75 on the first: 11
11/15 * 4/14 + 11/15 * 10/14 * 4/13...

wait isn't it just 11/15? If we don't a bulb that is 75 right away in the first then the 75 is picked on 2 or later right? 

The probability that at least two bulbs must be selected to obtain one that is rated 75 watts can be calculated as follows:
Let's consider the probability that a 75 W bulb is not selected on the first pick. The total number of bulbs is 15, out of which 11 are not 75 W. Therefore, the probability of not selecting a 75 W bulb on the first pick is 11/15. If a 75 W bulb is not selected on the first pick, then the next pick will have a higher probability of selecting a 75 W bulb.
The probability that at least two bulbs must be selected to obtain one that is rated 75 watts is indeed 11/15, as the question is asking for the probability of not selecting a 75 W bulb on the first pick.

Therefore, the probability is 11/15, specified to 3 decimal places, it is 0.733

Answer: 0.733

2. "In October, 1994, a flaw in a certain Pentium chip installed in computers was discovered that could result in a wrong answer when performing a division. The manufacturer initially claimed that the chance of any particular division being incorrect was only 1 in 9 billion, so that it would take thousands of years before a typical user encountered a mistake. However, statisticians are not typical users; some modern statistical techniques are so computationally intensive that a billion divisions over a short time period is not outside the realm of possibility. Assuming that the 1 in 9 billion figure is correct and that results of different divisions are independent of one another, what is the probability that at least one error occurs in one billion divisions with this chip? Specify your answer to 4 decimal places." 

Work: 
this is the same as 1 - P(no errors happen in the first billion divisions) = 1 - (999,999,999/10^9)^(10^9). Is that right?
Probability of no errors in one division = (1 - 1/9,000,000,000) (since the chance of an error is 1 in 9 billion).

Now, you want to find the probability of no errors in one billion divisions:
(1 - 1/9,000,000,000)^(1,000,000,000)

So, the probability that at least one error occurs in one billion divisions is:
1 - (1 - 1/9,000,000,000)^(1,000,000,000) = 1 - (8999999999/9000000000)^(1,000,000,000)

Answer: 0.1051

3. "Professor Stan der Deviation can take one of two routes on his way home from work. On the first route, there are four railroad crossings. The probability that he will be stopped by a train at any particular one of the crossings is .1, and trains operate independently at the four crossings. The other route is longer but there are only two crossings, independent of one another, with the same stoppage probability for each as on the first route. On a particular day, Professor Deviation has a meeting scheduled at home for a certain time. Whichever route he takes, he calculates that he will be late if he is stopped by trains at at least half the crossings encountered. Which route should he take to minimize the probability of being late to the meeting?"
Group of answer choices

Work:

For Route 1:

There are four railroad crossings.
The probability of being stopped by a train at each crossing is 0.1.
Trains operate independently at the crossings.
Now, let's calculate the probability of being stopped by trains at at least half the crossings (which is 2 or more) on Route 1:

Probability of stopping at least half (2 or more) crossings on Route 1:
P(at least 2) = 1 - P(0) - P(1)
Where:

P(0) is the probability of not being stopped at any crossing.
P(1) is the probability of being stopped at exactly one crossing.
For P(0), since the crossings operate independently:
P(0) = (0.9)^4 ≈ 0.6561 (probability of not being stopped at any crossing)

For P(1), we can use the binomial probability formula:
P(1) = C(4, 1) * (0.1^1) * (0.9^3) = 4 * 0.1 * (0.9^3) ≈ 0.2916 (probability of being stopped at exactly one crossing)

Now, calculate P(at least 2) for Route 1:
P(at least 2) = 1 - 0.6561 - 0.2916 ≈ 0.0523

For Route 2:

There are two railroad crossings.
The probability of being stopped by a train at each crossing is 0.1.
Trains operate independently at the crossings.
Now, let's calculate the probability of being stopped by trains at at least half the crossings (which is 1 or more) on Route 2:

Probability of stopping at least half (1 or more) crossings on Route 2:
P(at least 1) = 1 - P(0)
For P(0) on Route 2, since the crossings operate independently:
P(0) = (0.9)^2 ≈ 0.81 (probability of not being stopped at any crossing)

Now, calculate P(at least 1) for Route 2:
P(at least 1) = 1 - 0.81 ≈ 0.19

Comparing the probabilities:

Route 1 has a probability of approximately 0.0523 of being late.
Route 2 has a probability of approximately 0.19 of being late.
Therefore, to minimize the probability of being late to the meeting, Professor Stan der Deviation should take Route 1.

answer: take route 1


4. "Consider randomly selecting a student at a certain university, and let A denote the event that the selected individual has a Visa credit card and B be the analogous event for a MasterCard. Suppose that P(A) = 0.5, P(B) = 0.4, and P(A and B) = 0.25. What is the probability that the selected individual has at least one of the two types of cards? Specify your answer to 2 decimal places."

Work:
P(A or B) = P(A) + P(B) - P(A and B) = 0.5 + 0.4 - 0.25 = 0.65

Answer: 0.65


5. "An individual is presented with three different glasses of cola, labeled C, D, and P. He is asked to taste all three and then list them in order of preference. Suppose the same cola has actually been put into all three glasses. How many simple events are there in this ranking experiment?"

Work:
S = {CDP, CPD, DCP, DPC, PCD, PDC} = 6

Answer = 6

6. "A certain system can experience three different types of defects. Let A(i) (i = 1,2,3) denote the event that the system i has a defect of type i. Suppose that P(A(1)) = 0.12; P(A(2)) = 0.07; P(A(3)) = 0.05; P(A(1) or A(2)) = 0.13; P(A(1) or A(3)) = 0.14; P(A(2) or A(3)) = .10; P(A(1) and A(2) and A(3)) = .01. What is the probability that the system has both type 1 and type 2 defects? Specify your answer to 2 decimal places."

Work:
Remember that
P(A∪B)=P(A)+P(B)−P(A∩B)
and
P(A1∩A2)=P(A1)+P(A2)−P(A1∪A2)

P(A(1))=0.12
P(A(2))=0.07
P(A(3))=0.05
P(A(1) or A(2))=0.13
P(A(1) or A(3))=0.14
P(A(2) or A(3))=0.10
P(A(1) and A(2) and A(3))=0.01



Use addition rule
P(A(1) and A(2))=P(A(1))+P(A(2))−P(A(1) or A(2))
P(A(1) and A(2))=0.12+0.07−0.13 = 0.06

Answer: 0.062

7. "A friend of mine is giving a dinner party. His current wine supply includes 8 bottles of zinfandel, 10 of merlot, and 12 of cabernet (he only drinks red wine), all from different wineries. If 6 bottles are randomly selected, what is the probability that this results in two bottles of each variety being chosen? Specify your answer to 2 decimal places."

Work:
total combinations is 30C6
2 zin: 8C2
2 merlot: 10C2
2 cab: 12C2
The number of ways to choose 2 bottles of each variety is the product of the combinations for each variety. For example, the number of ways to choose 2 zinfandel bottles is (8C2) and similarly for the other varieties. The probability is then the number of successful outcomes (choosing 2 of each variety) divided by the total number of outcomes (choosing any 6 bottles out of 30).

Remember that (NcK) = n!/k!(n-k)!
so 8C2 = (8*7*6)/(2*1*6) = 28

Answer: Probability (8C2) * (10C2) * (12C2) / (30C6) = 0.14


8. "A stereo store is offering a special price on a complete set of components listed in the table on page 71 problem 32. A purchaser is offered a choice of manufacturer for each component: A switchboard display in the store allows a customer to hook together any selection of components (consisting of one of each type). Use the product rules to answer the following questions: In how many ways can components be selected if both the receiver and the compact disc player are to be Sony? "

work:

Given your data:
Receiver: The choice is fixed as Sony.
Compact disc player: The choice is fixed as Sony.
Speakers: There are 3 choices (Boston, Infinity, Polk).
Turntable: There are 4 choices (Onkyo, Sony, Teac, Technics).

Since the receiver and compact disc player choices are fixed as Sony, they each only have 1 way of selection. The number of ways to select the components is the product of the choices for the speakers and the turntable.

Total ways
= 1  ×  1  ×  3  ×  4
Total ways=1×1×3×4

Answer: 12

9. "A stereo store is offering a special price on a complete set of components listed in the table on page 71 problem 32. A purchaser is offered a choice of manufacturer for each component: A switchboard display in the store allows a customer to hook together any selection of components (consisting of one of each type). Use the product rules to answer the following questions: If someone flips switches on the selection in a completely random fashion, what is the probability that the system selected contains at least one Sony component? Specify your answer to 2 decimal places."

work:
To find the probability that the system selected contains at least one Sony component, you're correct to use the complement rule, which states that the probability of an event occurring is 1 minus the probability of the event not occurring. In this case, the event is "selecting at least one Sony component," and its complement is "selecting no Sony components."

rule: For any event A, P(A) + P(A') = 1, from which P(A) = 1 - P(A')

Given your data:
Receiver: Kenwood, Onkyo, Pioneer, Sony, Sherwood 
Compact disc player: Onkyo, Pioneer, Sony, Technics 
Speakers: Boston, Infinity, Polk 
Turntable: Onkyo, Sony, Teac, Technics

P(at least 1 sony component) = 1 - P(no sony) = 1 - (4*3*3*3)/(5*4*3*4) = 1 - 108/240 

answer: 0.55

10. "A box in a certain supply room contains four 40-W light- bulbs, five 60-W bulbs, and six 75-W bulbs. Suppose that bulbs are to be selected one by one until a 75-W bulb is found. What is the probability that it is necessary to examine at least six bulbs? Specify your answer to 3 decimal places."

work:
rule: For any event A, P(A) + P(A') = 1, from which P(A) = 1 - P(A')

So P(A) = finding at a bulb at 6 or later = P(not finding a bulb at 5 or before)
P(not 75)^5 = P(9/15 * 8/14 * 7/13 * 6/12 * 5/11)

answer: 0.04196

11. "A box in a certain supply room contains four 40-W light- bulbs, five 60-W bulbs, and six 75-W bulbs. Suppose that three bulbs are randomly selected. What is the probability that all three of the selected bulbs have the same rating? Specify your answer to 4 decimal places."

work:
Remember that (NcK) = n!/k!(n-k)!
total combinations = 15!/3!12! = 15*14*13/3*2*1
40w combos = 4!/3! 
60w combos = 5!/3!2!
75w combmos = 6!/3!3!


P(same wattage) = (P(4c3) + P(5c3) + P(6c3)) / P(15c3) = 0.0747
answer: 0.0747

12. "The Reviews editor for a certain scientific journal decides whether the review for any particular book should be short (1-2 pages), medium (3-4 pages), or long (5-6 pages). Data on recent reviews indicates that 60% of them are short, 30% are medium, and the other 10% are long. Reviews are submitted in either Word or LaTeX. For short reviews, 80% are in Word, whereas 50% of medium reviews are in Word and 30% of long reviews are in Word. Suppose a recent review is randomly selected.If the selected review was submitted in Word format, what are the posterior probabilities of it being medium? Specify your answer to 3 decimal places."

word:
Use bayes theorem

P(M) = 0.30 (30% of reviews are medium).
P(W|M) = 0.50 (50% of medium reviews are in Word format).
P(S) = 0.60 (60% of reviews are short).
P(W|S) = 0.80 (80% of short reviews are in Word format).
P(L) = 0.10 (10% of reviews are long).
P(W|L) = 0.30 (30% of long reviews are in Word format).

Bayes: P(M|W) = (P(W|M) * P(M))/(P(W))

P(W) is the total probability of a review being in Word format, which can be calculated using the Law of Total Probability:
P(W) = P(W|S) * P(S) + P(W|M) * P(M) + P(W|L) * P(L)

answer: 0.227


13. "The Reviews editor for a certain scientific journal decides whether the review for any particular book should be short (1-2 pages), medium (3-4 pages), or long (5-6 pages). Data on recent reviews indicates that 60% of them are short, 30% are medium, and the other 10% are long. Reviews are submitted in either Word or LaTeX. For short reviews, 80% are in Word, whereas 50% of medium reviews are in Word and 30% of long reviews are in Word. Suppose a recent review is randomly selected.What is the probability that the selected review was submitted in Word format? Specify your answer to 2 decimal places."


work:
P(M) = 0.30 (30% of reviews are medium).
P(W|M) = 0.50 (50% of medium reviews are in Word format).
P(S) = 0.60 (60% of reviews are short).
P(W|S) = 0.80 (80% of short reviews are in Word format).
P(L) = 0.10 (10% of reviews are long).
P(W|L) = 0.30 (30% of long reviews are in Word format).

Law of total probability:
You are using the Law of Total Probability, which states that the total probability of an event (in this case, a review being in Word format) is the sum of the probabilities of that event across all distinct categories.
P(w) = 0.8 * 0.6 + 0.5 * 0.3 + 0.3 * 0.1
