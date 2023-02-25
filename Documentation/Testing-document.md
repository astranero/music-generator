# Test documentation

## Unit testing

[Coverage report for tests](https://astranero.github.io/music-generator/)
![image](https://user-images.githubusercontent.com/77237218/221368657-ed2c0ced-8879-4f14-aa32-1f58110abe65.png)


### MarkovChain

MarkovChain class has been tested with great coverage.
I have tested that Markov Chain generates unique music melody based on the given data.

### UI and MarkovPlayer

I haven't tested this two classes, because there isn't really much to test. These have been manually tested by inserting different kind a values to cause it to crash. Program hasn't crashed with any edge case inputs. It handles exceptions by printing instructions.

### Trie

Trie has OK coverage, and I don't feel like it needs any more tests.

### Unit tests for the Trie Data Structure should verify the following

- Insertion of nodes into the trie in the correct order.
- Proper frequency tracking of children nodes.

### Unit tests for the Markov Chain class should verify the following

- Generation of notes based on the depth of the Markov Chain and their relation to the data with proper probability distribution.
- That the generated notes are related to the given prefix notes as expected.
