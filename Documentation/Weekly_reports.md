# Weekly Report

## First Week Report (Hours 8h)

- [x] Project creation and setting up version control (GitHub)
- [x] Added issues to GitHub
- [x] Selected project topic
- [x] Conducted research on subject matter needed for the project
- [x] Read Introduction materials

### Problems

- Uncertainty on how to implement a Trie structure with Markov Chain
- Lack of musical knowledge making it difficult to understand what variables should be stored

### What I have Learned

- Markov Chains
- Basics of trie, but still need to understand it in more depth.
- Little bit about Midi files

### Questions

- Should the prediction of note numbers be enough or should velocity for a given note also be predicted using a Markov Chain?
- I think it might be fun to try using Markov Chain, so that each note will be linked to set of velocities, or some other randomization for selection of velocity.
- Is it acceptable for velocity and duration to be hard-coded?
- Any tips regarding this project would be appreciated.

### Next Week

- Focus on coding, including the creation of classes for MIDI handling and playing MIDI files
- Development of User Interface (UI)

## Week 2 Report (Hours 20)

- [x] Create and test basic Markov Chain
- [x] Create and test Trie Data Structure
- [x] Create midi player
- [x] Conducted more research on the project subject
- [x] Fix errors
- [x] Add pylint and other configurations

### Problems

- Had some problem with infinite loop while creating long chains of notes straight from generate_melody method.
So I had to do it from midi handler

### What I have Learned

- Its possible to use second degree Markov chain for this project
- Usage of mido library

### Questions

- I am wondering if I should implement second degree markov chain?

### Next Week

- Sound of generated mav sounds awful, so may be creating trying to make it sound good.
- I still haven't created UI, so that should be next priority.

## Week 3 Report (Hours 15)

- [x] Fix and refactor code
- [x] Trying different codes snippets and their affect on the sound
- [x] Fix errors related to the changes in the code
- [x] Add coverage report

### Problems

- Didn't have any problems this week, because everything was basically same as previous week. Just went through different ways of doing the same.

### What I have Learned

- I have learned that it's possible to do Markov Chain with recursion too, but still at the end it was easier with while loop.

### Questions

- None

### Next Week

- Now that my music sounds good I should do more test to be sure that data isn't being used too much. But before that I will create UI and also test MarkovPlayer class.
