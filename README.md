# ESPICH: Pronunciation Training Game for Spanish Speakers
> ESPICH is a small text-based game written in Python that challenges Spanish
speakers with different pronunciation difficulties such as minimal pairs and
consonant clusters.

This game has been designed and created as a part of an evaluation for the
Education and NLP module of the Advanced Applications of Language Technologies
course in the HAP-LAP Master's Program at the University of Basque Country.

## Execution
*Disclaimer: This game has only been tested and ran on only one computer running OS X.*

OS X & Linux:

```sh
python3 game.py
```

## Game information
```
You wake up in the middle of a forest...
```
### Objective
The objective of the game is to make it out of the forest alive.
In the forest, you can encounter 3 different types of enemies, of which 2 are
standard enemies (The Evil Twins and The Wise Trees) and 1 a boss (The Old
Grumpy Troll).

### Basic information
You start with 100 HP and lose 5 HP points per (improper pronunciation).
To navigate around the forest, you use the indicated keys listed under actions,
which only shows the currently available actions.

### Enemies
These enemies represent sentences with different challenges implemented into the
game:
* Evil Twins - Minimal pairs (e.g. the vowel in 'beat' vs. 'bit')
* Wise Trees - Other pronunciation challenges (consonant clusters, voicing,
  silent r)
* Old Grumpy Troll - tongue twisters

To fight these enemies, you must pronounce things appropriately and make your
way out of the forest!

When enemies are defeated once, they do not respawn so you can safely find your
way to the exit. You will know that you are near the exit once you encounter The
Old Grumpy Troll as there is only one per game.

### Feedback
Should you have trouble against the enemies, you can always ask The Fairies of
the Forest for help! They offer help in three different ways:
* ARPAbet transcription - the ARPAbet transcription of the given sentence
* IPA transcription - the IPA transcription of the given
* Descriptive advice - descriptive advice of mouth placements for sounds that
  appear in the sentence

## Dependencies

In order to run the game, you must have Python 3 (and not Python 2).
You must also install the SpeechRecognition module found [here](https://pypi.python.org/pypi/SpeechRecognition/).
To use the feedback module, [NLTK](http://www.nltk.org/) must be installed.

You will also need a microphone to do the recording.

## Release History
* 0.1.1 - 6/14/17
    * README edited to mention NLTK dependencies.
* 0.1.1 - 6/8/17
    * README finally added.
* 0.1.0 - 4/26/17
    * The first 'working' release
    * Submitted for small project evaluation.


## Meta

Created by Ona de Gibert Bonet, Kenny Lino and Jovana Urosevic, students in the
Erasmus Mundus Language and Communication and Technologies program at the
University of Basque Country.

Not currently distributed under a license.
