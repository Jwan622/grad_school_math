# Terms to Review
- Sample Space
- Events
- mutually exclusive events are not independent
- independent events.
![independent_events](../images/indepedent_definition.png)


events: 
- simple they can be made up of multiple observations. And outcome is how a simple event is evaulated and that needs to be singular. You need be looking for one singular outcome or collection of observations. An event is any collection (subset) of outcomes contained in the sample space S. 
- An event is simple if it consists of exactly one outcome and compound if it consists of more than one outcome.
- Consider an experiment in which each of three vehicles taking a particular freeway exit turns left (L) or right (R) at the end of the exit ramp. The eight possible outcomes that comprise the sample space are LLL, RLL, LRL, LLR, LRR, RLR, RRL, and RRR. Thus there are eight simple events, among which are E1 = {LLL}. So that {LLL} event is still simple even though it has multiple observations.
- A compound event would be the event that all three vehicles turn in the same direction. The event would be: {LLL, RRR}.

# Example problems to review.

1. Example 2.23
![comb_problem_1](../images/combination_problem_1.png)
- the word "least" should suggest to you that you need to add up the probabilities.


2. Non intuitive at first but it makes sense

![comb_problem_2](../images/combination_problem_2.png)

You might ask why does the 2nd way of calculating this make sense. Why is it 95_c_5 on top?
- but why is it just 95C9/100C10? IF you think about it hard, it makes sense. if you add up all the ways you can do 95C9 for the last 9 beatles songs after the first 5 are chosen (and there’s only 1 way for this to happen) you should get the probability of the 5th song being a beatles song. It kind of makes sense. If you take into account all the ways 95C9 occurs, and there’s only 1 way for the last beatles song to be the 5th, and you divide it by the 100C10, you should get the probability that the last beatles song is 5th.

3. independence

events can be independent even if some of A is in the subset C. 
Events are dependent if: `P(A|C) = P(A)` but this can happen even if some of the elements of A are in C as in below.

![independence](../images/independent.png)

- The two probabilites just need to be independent. C occuring just needs to not affect A... so if the probabilities are the same, who cares if C has elements of A.
- P(A) is the same regardless of whether B occured.
- also remember that mutually exclusive events are NOT independent.
