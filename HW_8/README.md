# HW 8

## Running
### Install Packages via pip
`$ python3 -m pip install -r requirements.txt`

### Run using Python 3.9
`$ python3.9 main.py`

## Assignment
For this assignment you will use Object-Oriented Programming to create a racing game. You have 2 choices for this assignment - Challenge Mode or Simple Mode (_I recommend Challenge Mode if you plan to take other programming classes after this, and only take Simple Mode if you expect this to be your only programming class_).

## Challenge Mode
(Choose this option if you plan to take other CS classes)

Choose some type of object that would make sense to compete in a race (ie. boxcar, horse, person, ships, bikes, greyhounds, snails... be creative). Create a class of this type of object. It will have a fixed speed it can run (or drive) and maximum distance it can go before becoming exhausted (or running out of gas). It should also have a name to identify it by, but keep it simple (ie. 'Horse 0', 'Horse 1', etc.). During the initialization, the speed and maximum distance should be determined by a random value within a range that makes sense for that type of object, but with no units (ie. assuming miles you would use 40-44 for horse speed and 2 for distance of a horse race). _Use_ `random.uniform(val1,val2)` _if you want to generate a random decimal value rather than an integer, particularly useful with small numbers_.

Create a race that is initialized with a distance that is specified when it is created (ie. pass as a parameter to the __init__). The number of racers can be determined when a new race is started using a startRace method. You'll also need a method to determine which racer wins (based on highest speed within the given distance). In your main function, create a race with a distance of your choice, print the race distance, and start the race with 5 racers, and print out the details of each racer (name, speed, max distance), and then determine which one wins and print the result of the race. Using the same race (don't create a new one), start the race with 8 racers and again print out the details of each racer and then print out which one wins.

Here is a possible output from a Horse race (note that the results of the races will be different each time you run it):
```
Race Distance: 2
Horse 0 Speed: 40 Max Distance: 1.886602776175576
Horse 1 Speed: 43 Max Distance: 2.2543107494109664
Horse 2 Speed: 40 Max Distance: 2.3422628628436923
Horse 3 Speed: 41 Max Distance: 2.237815470871785
Horse 4 Speed: 40 Max Distance: 1.7883226018197373
Winner: Horse 1
Horse 0 Speed: 43 Max Distance: 1.7835187365203125
Horse 1 Speed: 43 Max Distance: 1.651116450587179
Horse 2 Speed: 43 Max Distance: 1.64315256424609
Horse 3 Speed: 42 Max Distance: 2.1279316714432746
Horse 4 Speed: 43 Max Distance: 1.5312846230783852
Horse 5 Speed: 41 Max Distance: 2.44574965247417
Horse 6 Speed: 42 Max Distance: 1.688510862362611
Horse 7 Speed: 43 Max Distance: 1.825278099402782
Winner: Horse 3
```


## Simple Mode
(Choose this option if 303E will be your only CS class)

Create a sports car race representing the Indy 500 (which is a 500-mile car race) as follows:

Start by creating a Car class that is initialized with a name, a speed, and a max_distance. During the __init__ method set the speed to a random number between 60 and 100 and set max_distance to a random number between 450 and 550 (remember to add `import random` at the top). _The logistics of this is that some cars will fail to make it the full 500 miles. The name should be passed as a parameter and set during initialization_.

Next, create a class for Race that will have an attribute for distance and a method to start the race. The distance should be set to 500 during the __init__ method. When a race is started you will specify a number of cars competing. Your Race class will need a method called startRace which will take a number, and use that to create a list of race cars. For each car you create, give it the name "Car #" where # is the number of that car (from 0 up to the total number of cars in the race). You will also need a method to determine the winner called getWinner which determines the fastest car that has a max_distance greater than or equal to the race distance.

In your main function, create a race: indy = Race(). Call the startRace method with 18 to start the race with 18 racers. Print the details of each racer, then call the getWinner method and print the result of the race. Here is some starter code:
```python
import random
class Car:
  def __init__(self,name):
    #set self.name to name
    #set self.speed to a random number between 60 and 100
    #set self.max_distance to a random number between 450 and 550
    
  def __str__(self):
    # return a string formatted with info for the name, speed, and max distance
class Race:
  def __init__(self):
    #set the distance to 500
    
  def startRace(self,racers):
    #create a list attribute called racer_list
    #for each number from 0 up to racers (the total number of racers)
      #create a car named Car # (with the number)
      #add the car to the list
      #print the car details
    
  def getWinner(self):
    #create a variable called winner and set it equal to 'No winner'
    #loop through all racers in the list of racers
      #check if its max distance is greater than the race distance
      #if the current winner is 'No winner' set this to the winner
      #otherwise, check if the speed of this racer is faster than winner.speed
      #update the current winner accordingly
    #after finishing the loop, return the winner
    
def main():
  #create a new race indy = Race()
  #start a new race with 18 racers
  #print the results of the race by calling getWinner()
if __name__=="__main__":
    main()
```

And here is some sample output (note that the results of the race will be different each time you run it):
```
Car 0 Speed: 65 Max Distance: 499
Car 1 Speed: 64 Max Distance: 489
Car 2 Speed: 86 Max Distance: 537
Car 3 Speed: 63 Max Distance: 549
Car 4 Speed: 90 Max Distance: 517
Car 5 Speed: 76 Max Distance: 468
Car 6 Speed: 66 Max Distance: 533
Car 7 Speed: 74 Max Distance: 529
Car 8 Speed: 87 Max Distance: 454
Car 9 Speed: 98 Max Distance: 488
Car 10 Speed: 63 Max Distance: 548
Car 11 Speed: 72 Max Distance: 465
Car 12 Speed: 62 Max Distance: 456
Car 13 Speed: 80 Max Distance: 475
Car 14 Speed: 79 Max Distance: 459
Car 15 Speed: 69 Max Distance: 543
Car 16 Speed: 85 Max Distance: 486
Car 17 Speed: 79 Max Distance: 461
Winner: Car 4
```


## Submission:
Name your file last_first_hw8_challenge.py if you chose challenge mode, or last_first_hw8_simple.py if you chose simple mode (replace with your name, and be sure to choose simple or challenge correctly so we grade based on the correct instructions).

## Bonus Points:
For +2 bonus points (regardless of if you chose Simple or Challenge) visualize your race using Python Turtle Animation (or other python graphics tool of your choice)

Important! You must still print all of the details required above, and note that the example animated race at that link does not follow the instructions for our race, so it is only a starting point to help you see how to apply animations (if you submit just the code from that site, you will not receive any points).