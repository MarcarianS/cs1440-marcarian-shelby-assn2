*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

Use FIPS codes to determine which fields of lines to include in the report 
for each field of information. ignore FIPS codes beginning with letters or 
ending in 000.
It looks like we will just be ignoring lines with the wrong FIPS codes, and 
cutting out columns with unnessecary data.
after the appropriate rows and columns have been ignored and cut from 
the file, the appropriate fields of data will be returned to the program to
be printed out in the report. Will need to keep cols 1, 2 3, 9, 10, 11 

# 1.  System Analysis

**Input
-a single directory which contains the 2019 data file, trimmed appropriately

**Internal Data: 
-if the lines first entry contains a letter or ends in 000, ignore that line
-then, for all industry, if the first and second entry are 0 and 10
-add appropriate column values to variables for total annual wages, total 
number establ, total ann emplvl. 
-keep counter for how many lines make it this far(will be number of FIPS
in report for this section)
-check if each wage, est, and emplvl is greater than current max. set max to 
that val, and record FIPS so I can reference the titles csv for the name.
-or, for all software, repreat the process.
-for through the titles csv to find the name of each county max.
# 2.  Functional Examples

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
