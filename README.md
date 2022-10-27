# Blackjack Card Counter

## What is Card Counting in the Game of Blackjack?

Blackjack (https://en.wikipedia.org/wiki/Blackjack) is a popular card game, and is especially played at casinos. However, the interesting thing about blackjack is that it gives the player the best odds against the house in comparison to other casino games you might find. 
There are also multiple ways that you can increase your odds of winning at blackjack. For example, implementing basic strategy. If you've watched the 2008 film, *21*, you'll know the other way to increase your odds is to count cards.

Counting cards is a technique that allows you to keep track of the cards that have been played, and use that information to make better decisions about how to play your hand. At a very basic level if you know that there are more high cards left in the deck, you have the advantage and should bet more, and if you know that there are more low cards left in the deck, the dealer has the advantage and you should bet less (or not at all).

## How does my application work?

This card counting application works by taking in how many decks the house is using, the betting unit you'll be playing with, and then by repeatedly asking if the last card pulled is high, medium, or low. If the card pulled is high, in the _behind the scenes_ the running count subtracts one and the tru count divides the running count total by the number of decks left (accounting for the card that was just pulled out).
If the card pulled is medium, the running count stays the same and the true count is altered slightly as there is now a card missing from the deck (shrinking the number of decks left by a fractional amount). Similarly, if the card pulled is low then the running count adds one and the true count is altered slightly via the same method.

## Current Use

The application can currently be used as a command line application. 

The user enters the number of decks and the betting unit. Then is prompted to enter an *h* if the face value of the card was high (10-A), an *l* if the face value of the card was low (2-6), and an *m* if the face value of the card was not in the previous categories.

The user can also enter *q* to quit.

After entering what category the face value of the card belonged to, the application will print out the current true count, and how much should bet accordingly to the MIT method. Then this is repeated until the user quits the application.

### MIT Bankroll Method

The MIT method is a method of betting that is based on the true count. The method is as follows:

- To determine the amount you should bet, subtract 1 from the true count and multiply by the betting unit being used.

## Future Plans

The goal with this application is to build a full stack web-application that is hosted by Github and has a much friendlier UI. 

I would use Digital Ocean's Function service to host the Python API (which would be this repo), and then use React to build the interface.

### What I've Currently Done

I am currently working on the React interface, but as I started to experiment more with it as school started, I haven't gotten a chance to fully finish it. My goal is to have it done by winter break.

## My Use of TDD

I built this API with a strong use of TDD. I would build the test first that would fail, make the test pass in the simplest way possible, and then refactor if I could. Allowing the tests to guide my development.

# IMPORTANT !!!

This is a **fun** application that I built to learn more about TDD and to practice my Python skills. It is not meant to be used in a casino, and I am not responsible for any losses you may incur if you use this application. Please gamble responsibly :)