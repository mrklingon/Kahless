# Kahless
Search for Klingon words from the book "Kahless" and "The Final Reflection"

## Files
ASCII ART IMAGES
* D7
* bird
* emblem
* fleet
* ship
* warbird
* blade

CODE
* code.py
* kahless.bmp
* kahless.py
* metadata.json
  
TEXT FILES
* kahless.txt - info from "Kahless" by Michael Jan Friedman
* klingonaase.txt - info from "The Final Reflection" my John M Ford
* worf - Worf quotes

* kahless.bas BASIC version of Kahless

## Project description

KAHLESS is a reengineering of a C64 Basic program I wrote almost 30 years ago after I found a website listing Klingon words used in the novel "Kahless" by Michael Jan Friedman. My C64 program was written and compiled on an emulated C64. Interpreted string operations are SLOW - without the emulator running in "warp" mode, the program would not have been useable.

This project involved recovering the language info from the C64 binary (which I had posted in uuencoded form to a website).
I then thought I should include some of John Ford's "Klingonaase" from "The Final Reflection" - happily I found https://afrodita.rcub.bg.ac.rs/~alexp/books/klingon.html which listed the vocabulary (fan and gaming sites have added more, but for this project I stuck to the words from these two Classic Klingon novels (Available in the omnibus edition "The Hand of Kahless").

## How to Use

On a Fruit Jam, copy all the files except kahless.bas to a directory "apps/KAHLESS". Then you can click on the KAHLESS icon to start the program. When run you'll see:

```
              |
              |
              |
             ' `
             | |
             | |
            '   `
         .-'|   |`-.
        /  /     \  \
       |__,\     /   |
      -'   \\   //\_ |
   ,-'   ___\\.//   `-__
  /__,--'       `--.____--
         `-._____.-'

-------------
What do you want to search for in the Kahless/The Final Reflecton lexicons?
```
Enter any string, for example "op"

```
-------------
What do you want to search for in the Kahless/The Final Reflecton lexicons?
op


Kerpach(a modern Klingon  (shopkeeper) KAHLESS

kleon               Enemy, or opponent.  Same, to a Klingon. [TFR]

  tai-kleon         Worthy opponent.  See 'kleon' above. [TFR]

teskas tal'tai-kleon  Compliments to a worthy opponent. [TFR]
```
Entries from KAHLESS are labeled, and entries from The Final Reflection are marked [TFR].

The program pauses 10 seconds then displays one of the ascii art files and gives the search prompt.

To use it a sort of screen saver, type "dorandom" for the search. Then the program will display a random artwork, a random word from one of the two lexicons and then a random quote from Worf.

You can customize it by adding more quotes in the "worf" file. 

## Basic Version

Copy the file kahless.bas to apps/PyBasic/examples on a Fruit Jam. Then you can start PyBasic, and load "examples/kahless" and type "run"

```

What would you like to search for from Kahless or The Final Reflection?
? op
Kerpach(a modern Klingon  (shopkeeper) KAHLESS
kleon               Enemy, or opponent.  Same, to a Klingon. [TFR]
  tai-kleon         Worthy opponent.  See 'kleon' above. [TFR]
teskas tal'tai-kleon  Compliments to a worthy opponent. [TFR]

```
