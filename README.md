# Pronunciation Similarity Algorithm (Version 1.0.2)

The algorithm uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) which contains the spelling of each word in English as well as its [ARPAbet](https://en.wikipedia.org/wiki/Arpabet) translation.

- [Feature to Numeric Representation Reference Sheet](http://tomlisankie.com/pronunciation-algorithm-resources/feature-to-number-reference.txt)
- [Phonemes and Their Features (in Numerical Form)](http://tomlisankie.com/pronunciation-algorithm-resources/features.txt)

There are two cases encountered when comparing two words for pronunciation similarity: either they have the same phonemic length (that is, they are composed of the same number of phonemes) or they have differing phonemic lengths. In either of these cases, the algorithm awards pronunciation “points” between phonemes based on how many [distinctive features](https://en.wikipedia.org/wiki/Distinctive_feature) two phonemes share with one another. All features are treated the same when calculating how many points are to be awarded except for voicing and sonority. The reasoning for treating voicing differently is that when comparing two phonemes that are identical with the exception of their voicing, voicing doesn't make too much of a difference for the rest of the articulation. Thus, a smaller deduction is made when there's a voicing difference. The reasoning for treating sonority differently is that sonorous consonants in English can be nuclei for syllables. Considering sonority separately is also important when comparing a vowel (which we define as a phoneme that at the very least is syllabic, sonorous, continuous, an approximant, and voiced) and a consonant.
The measurements for comparing two phonemes are as follows:

| **Comparison Case**      | **Number of Points Awarded** |
| :-------------: |:-------------:         |
| Vowel and Vowel        | 5 - (number of features they don't share) - (difference in stress)         |
| Consonant and Consonant   | 2 - (0.15 * (number of features they don't share)) - (0.1 if they both aren't voiced) - (1 if they both aren't sonorous)              |
| Vowel and Consonant   | (0.1 * (the number of features that they have in common)) + (0.1 if they both are voiced) + (1 if they're both sonorous)               |

### Some Basic Definitions 

* **Rhyme Value**: the sum of the points awarded between phonemes for any two given words as well deductions when necessary.
* **Homophonic Rhyme Value**: the Rhyme Value given when comparing a word to itself.
* **Rhyme Percentile**: ((Rhyme Value)/(Homophonic Rhyme Value)) * 100%

## Pronunciation Similarity Between Words of Same Phonemic Length

Finding pronunciation similarity between words that have the same number of phonemes is relatively straightforward and can be broken down into three steps:

1. Iterate through each phoneme in one of the words and compare it to its corresponding phoneme in the other word, adding the resulting points awarded to the total Rhyme Value along the way.
2. Find Homophonic Rhyme Value (as previously defined).
3. Divide Rhyme Value by Homophonic Rhyme Value and multiply by 100.

### Example:

Let’s choose two words that have the same phonemic length and compare them to one another: *upright* [AH0 P R AY1 T] and *uptight* [AH0 P T AY1 T]. (**note:** numbers next to vowel phonemes indicate stress)

#### Step 1

|  |  |  |  |  |  |  |
| :--------------------: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Phonemes of Word 1** | AH0 | P | R | AY1 | T |  |
| **Phonemes of Word 2** | AH0 | P | T | AY1 | T |  |
| **Points Awarded** | 5 | 2 | 0.45 | 5 | 2 | **Total RV: 14.45** |
 
#### Step 2
|  |  |  |  |  |  |  |
| :--------------------: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Phonemes of Word 1** | AH0 | P | R | AY1 | T |  |
| **Phonemes of Word 1** | AH0 | P | R | AY1 | T |  |
| **Points Awarded** | 5 | 2 | 2 | 5 | 2 | **Total HRV: 16** |
(note that performing this same operation on *uptight* would result in the same total)
 
#### Step 3
(14.45/16)*100% = 90%

## Pronunciation Similarity Between Words of Differing Phonemic Length

The process of finding pronunciation similarity between two words of differing phonemic lengths is a bit trickier since simple iteration through the phonemes of a word is simply not enough to gain an accurate picture of whether or not two words have similarity in pronunciation. While the last two steps may remain the same, it is necessary to test a variety of combinations and then give the benefit of the doubt to the combination with the highest Rhyme Value output. This process can be rather hard to explain, so I’ll try and explain by example first:

Let’s say we’re comparing the words *shifter* (SH IH F T ER) and *ship* (SH IH P). (These were chosen because they only differ in size by two phonemes which makes them an easy example to showcase). First, we must identify which word is phonemically longer and which is shorter. In this case *ship* is the shorter word and *shifter* is the longer word.

Once we have identified which word is shorter and which is longer, we then compare the first phoneme of the shorter word to every phoneme in the longer word and then store the positions in the longer words where there were points awarded:

| **Index of Longer Word** | **Phonemes of Longer Word** | **Points Awarded for Comparison** |
| :--: | :--: | :--: |
| 0   | SH | 2 |
| 1   | IH1 | 0.1 |
| 2   | F | 1.55 |
| 3   | T | 1.4 |
| 4   | ER0 | 0.3 |

Thus, the indexes of the three phonemes that were awarded points (SH, F, T) are stored along with the number of points awarded at each index. These comprise the first “layer” of comparisons and can be represented as such with each pair being represented as (index, points):

![diagram](http://tomlisankie.com/pronunciation-algorithm-diagrams/1.jpg "1")

Now that we have some starting indexes, we can begin to figure out where the succeeding phonemes of the shorter word fit into the rest of the longer word. Now we compare the next phoneme of the shorter word (IH) to every phoneme in the longer word that starts after one of the previously recorded indices. The only two phonemes that return points for the first recorded pair are “IH” at index 1 and “ER” at index 4. The only phoneme that awards points after the next two recorded pairs is “ER.” Now our situation looks like this:

![diagram](http://tomlisankie.com/pronunciation-algorithm-diagrams/2.jpg "2")

Last, but not least, we have the final phoneme in the word to compare. Since the there’s no phonemes in the longer word that succeed the fourth index, those index-point pairs are not checked for any follow up phonemes. However, checking the phonemes after index 1 does return some phonemes that award points:

![diagram](http://tomlisankie.com/pronunciation-algorithm-diagrams/3.jpg "3")

All possible positions for placement of the shorter word’s phonemes for Rhyme Value with the max number of points have now been found. It’s now necessary to find which path leads to the highest Rhyme Value and thus what individuals are most likely to intuitively see as similarity in pronunciation between the two words.

To do this, whichever index-point pair in each node that has the largest point value is sent up and added to the point value of the node’s parent index-point pair as well as that pair’s index(es) added to the parent’s. For example, in the bottom layer, there is only one node that contains index-point pairs. These pairs are (2, 0.5) and (3, 0.5). Their point value is equivalent so whichever is sent up is arbitrary as far as we’re concerned, so let’s send up (3, 0.5):

![diagram](http://tomlisankie.com/pronunciation-algorithm-diagrams/4.jpg "4")

This process is then repeated for each node in each layer until the initial layer is reached:

![diagram](http://tomlisankie.com/pronunciation-algorithm-diagrams/5.jpg "5")

Once the initial layer has been reached, it would make sense to deduce points from the remaining index-point pairs by seeing how much space is between each of the indices as well as from the first recorded index to the beginning of the word and from the last recorded index to the end of the word. We will deduce 0.25 from the Rhyme Value for each space between indices and deduce log(x+1) and log(y+1)  where x is the amount of space from the front to the first index and yis the amount of space from the last index to the end of the word. The results are as follows:

![diagram](http://tomlisankie.com/pronunciation-algorithm-diagrams/6.jpg "6")

The dominant index-pair here is clearly the first one. The Homophonic Rhyme Value is then found for the longer word. In this case it comes out to be 16. The Rhyme Percentile is then found and it comes out to be (7.1/16)*100% = 44%
