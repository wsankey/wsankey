title: My Stata Workflow
categories: [workflow, programming]
tags: [workflow, analysis]
description: Some tips on structuring your data analysis using Stata.


People new to analysis generally and Stata in particular might be
confused by how to start and structure their scripts. I know I felt
the same way when staring at a blank command prompt. 

Let's say you've already imported and opened your dataset and you know what you need to do to turn this into something you can work with. You've heard that you should use Do files and Logs but you're confused about what those are and exactly how you can use them.

The following code is my boilerplate template I use when starting a new
Stata project, I explain this boilerplate language section by section
after this code block:

    /*
    Programmer:	    W. Sankey
    Date:		 	   Feb 19, 2015
    Project:		  The name of the project I'm working on.  
    Purpose:		  The outcome of *this* particular script.
    Approach:		  How I structure the code in this script. 
    */
    log using "path/to/logs/NewLog.smcl"
    
    set more off

    global input "path/to/raw/data"
    global output "path/to/manipulated/data"
    global scripts "path/to/other/Do/files"

    cd "$input"

	    use Statadata.dta, clear
    
        Your analysis code here.

    log close

* All the code between /* and */ are notes picked up by Stata and are
  pieces of information you should be tracking and updating.

* The statement 'log using' initializes the Log file which will capture
  everything that happens in the program from this point on. 

* The command 'set more off' tells Stata not to stop when the display
  fills with code. It will just keep zipping through your program until
hits and error or completed. 

* The reserved word 'global' sets aside a macro variable that will
  persist over the course of the Stata instance. So, if I were to write
"global one 1" and clear my dataset that macro variable $one would
remain instantiated and I could use it to create other Stata variables
(e.g. "gen x = 1 + $one")

* In this file I use global variables to track my paths so I don't have
  to remember where I'm pulling or saving files to. When I want to save
a dataset I cd (change directory) into that path and save my output
(notice the global variable $output) and I know where datasets are
going.

* The remainder of the code after cd-ing into my $input path simply uses
  my dataset of interest nad notes that afterwards I'm writing my
general analysis code. At the end I close my log and the analysis is
done. 

Note that I have a global variable $scripts that is linking to my Do file path. When you're new to Stata you might think it's efficient to document your entire analysis in one
Do file. **It is not.** I regularly have Do files that contain variable
labels, exlcusions, or other side analyses that I may want to reference
in my main Do file. As a general rule I keep my Do files to 50 lines.
This prevents me from getting too confused about what is happening in my
codebase. Once you get really adept at calling different Do files in
your programs you may even create a 'controller' Do file that manages
your analysis, instantiates the Log file, and runs all of your Do files
in their necessary order. 

Once projects get so large that you are managing more than ten or so Do
files (and you have multiple people working on different parts of the project) you will have to create a system of documentation. This is a topic for another blog post but I will point you to ideas generated in the SAS setting by Elizabeth Axelrod and Louise Hadden of Abt. Associates who have written papers on the subject. [This is a link to one of Louise Hadden's SAS papers.][1] [If you are looking for more detail on how to structure your Stata project, I recommend this book.][2]




[1]: http://www2.sas.com/proceedings/sugi25/25/po/25p204.pdf
[2]: http://www.amazon.com/Workflow-Data-Analysis-Using-Stata/dp/1597180475/ref=sr_1_1?ie=UTF8&qid=1424487013&sr=8-1&keywords=stata+workflow+of+data+analysis 
