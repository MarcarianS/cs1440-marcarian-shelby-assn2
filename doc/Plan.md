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
Do accept:
-overseaslocations- 996
-multiCounty not statewide - 997
-out of state - 998
-unknown or unidentified - 999
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

**Function Stub:
if length sys.argv < 2
	print usage message, need one directory
if opening the areatitles fails, let python crash
convert areaTitles tp dictionary??

open 2019data (crash if doesn't open)
def variables allNumAreas, allTotalAnnualWages, etc all = 0
for line in fileObj, split on "," max 11, remove 12th element 
	check is Fips numeric and if endswith 000
	if not, consider that line
		if lineLst[1] =  "0" and [2] = "10"
			allNumAreas += 1
			alltotAnnualWages += int(linelist[11]
			allTotEst += int(linelist[9])
			alltotempl += int(lineList[10])
			if lineList[9] > allmaxest
				allmaxest = linelist[9]
				keep fips to get name(use dict?)
			if lineList[10] > allmaxempl and [11] >maxwage
				same process
		if linelist[1] = "5" and[2] = "5112"
			same process, replace all with soft for varName
					
**Output:
-a formatted data report of all and software industries.

# 2.  Functional Examples
 
if len(sys.argv) < 2
	print(Usage: src/main.py DATA_DIRECTORY)
else
	areaTitlesObj = open(data.area_titles.csv)
	areaTitlesObj.readline()
        for line in areaTitlesObj:
            line = line.strip()
		line = line.strip("\"")		
            fips, title = line.split("","")
            if fips.isnumeric() and not fips.endswith("000"):
                areaTitlesDict[fips] = title	
	
	dataObj = open(data.2019.annual.singlefile.csv)
	allNumAreas = 0
	allTotWages = 0
	allMaxWage = 0
	allmaxwagearea = ''
	allTotestab = 0
	allMaxEstab = 0
	allmaxestabArea = ''
	allTotEmp = 0
	allmaxEmp = 0
	allMaxEmparea = ''

	softNumAreas = 0
        softTotWages = 0
        softMaxWage = 0
        softmaxwagearea = ''
        softTotestab = 0
        softMaxEstab = 0
        softmaxestabarea = ''
        softTotEmp = 0
        softmaxEmp = 0
        softMaxEmparea = ''
	
	for line in dataObj
		line.split(11, ",")
		line.remove(line[11])
		for i in range(len(lineList))
			lineList[i] = lineList[i].strip(""")
		if line[0] in areaDictionary
			if line[1] = "0" and line[2] = "10"
				allnumAread += 1
				alltotAnnualWages += int(linelist[10]
        	                allTotEst += int(linelist[8])
	                        alltotempl += int(lineList[9])
                	        if lineList[8] > allmaxest
                                	allmaxest = linelist[8]
                                	keep fips to get name(use dict?)
                        	if lineList[9] > allmaxempl and [10] >maxwage
					same process
			if linelist[1] = "5" and[2] = "5112"
	                        same process, replace all with soft for varName



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

-Ran through each of the files in data.
-(fixed)found that i had an off by one error in the first run (linelist was 11 long)
-(fixed)Found another off by 1 with wages, emp, and estab
-(fixed)removed the qutations from each value so the program could tell ifnumeric
-(fixed)copy/paste error: was using code from allindustry, forgot to change 
variable name to soft for max reports, returned an empty string for areas.
-tested with ending "/" and without, runs correct with both
	ex. INPUT: data/DE_soft/
	    INPUT: data/DE_soft
-Note* does not work if "/" is taken uot of the hardcoded path, but the
extra front slash from the command line argument doesn't seem to affect it.
Seems like it doesn't matter how many frontslashes there are hardcoded, as
long as there is at least one, either from CLI or hardcoded.
