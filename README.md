<!---

TASK LIST:

  * Use cp -rf *.* to copy all of the files and directories in this repository
    to the starter repository for this assignment
  * Change into the directory for the starer repository
  * Update the header (e.g., #) to only give the name of the assignment
  * Update the first paragraph to include the commented-out content
  * Change the link in the # Problems section to point to this lab's starter
  * Create the assignment in the GitHub Classroom, noting the URL
  * Test the assignment by accepting it with your own GitHub account
  * Check to ensure that your GitHub repository is created correctly
  * Share the assignment link with all of the students using email or Slack

PROBLEMS?

  * Contact Gregory M. Kapfhammer by email or Slack
  * Raise an issue in the GitHub repository for this assignment

-->

# cs280-F2017-lab3

Designed for use with [GitHub Classroom](https://classroom.github.com/), this
repository contains the solution for Laboratory 3 in Computer Science 280.
Since the Travis builds for this repository will initially fail (as evidenced
by a red &#x2717; appearing in the commit logs instead of a green &#x2714;),
the programmer is responsible for completing all of the steps needed to satisfy
the requirements for the assignment, thus causing a &#x2714; to instead appear
in the commit logs.

## Introduction

This assignment requires a programmer to implement and test a Python 3 program,
called `generator.py`, that will generate a list of lists from an input list.
Currently, the main function in `generator.py` is not implemented. However,
before you start to implement this function, you should read the requirements
provided to you by your customer (as given in the previous laboratory
assignment) and study the existing test cases that the implementation should
ultimately pass. Along with adding additional test cases to establish a
confidence in the correctness of your system, your goal is to implement a
function that meets the specification and passes the existing test cases.

The programmer is also responsible for completely revising and adding many
sections of content to the file called `README.md`. This is a Markdown file
that must adhere to the standards described in the [Markdown Syntax
Guide](https://guides.github.com/features/mastering-markdown/). Remember, you
can preview the contents of a comitted Markdown file by clicking on the name of
the file in your GitHub repository. Finally, don't forget that your `README.md`
file should adhere to the Markdown standards established by the [Markdown
linting tool](https://github.com/markdownlint/markdownlint). Ultimately, the
goal of this assignment is for you to gain experience in using the GitHub flow
approach to collaboratively develop software.

## Learning

If you have not done so already, please read all of the relevant [GitHub
Guides](https://guides.github.com/) that explain how to use many of the features
that GitHub provides. In particular, please make sure that you have read the
following GitHub guides: [Mastering
Markdown](https://guides.github.com/features/mastering-markdown/), [Hello
World](https://guides.github.com/activities/hello-world/), and [Documenting Your
Projects on GitHub](https://guides.github.com/features/wikis/). Each of these
guides will help you to understand how to use both [GitHub](http://github.com)
and [GitHub Classroom](https://classroom.github.com/). Please see the laboratory
assignment sheet for links to the other reading assignments about GitHub flow.

To do well on this assignment, you should review Chapters 1 and 2 of the SETP
course textbook. Additionally, you should also read Chapter 3 of SETP, paying
particularly close attention to content about project management and team work.
Please see the course instructor if you have questions about any of these
reading assignments.

## Requirements

The Python3 software that supports this assignment requires you to install the
`pytest` library by typing the command `python3 -m pip install --user -r
generator/requirements.txt` from the root directory of your GitHub repository.

## Commands

When you are in the `generator` directory of your GitHub repository, you can
type the command `python3 generator.py --list 1 2 3` to run the program. The
correct version of this program would then produce the following output.

```
Generator generates a lists of lists from an input list!

Generating the List:

Length of Generated List: 4

Generated List:

1 2 3
2 1 3
3 2 1
1 3 2
```

However, when you run the provided version of the program, you should notice
that it does not produce the same output. This means that there is a defect in
this program and/or a misunderstanding of its specification! In fact, when you
run the test suite for the program with the command `pytest tests` in the
`generator` directory you should notice that the test suite fails.

## Assignment

For this assignment, you are invited to find and fix the defect in the program
and/or its specification. If you would like to learn more about the Python 3
programming language, then you can download the free book called [A Whirlwind
Tour of
Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp).
After learning more about Python 3 and reading the specification for this
project that is given in the assignment sheet, you should ensure that your
program produces the intended output in the terminal window. Next, you should
ensure that the test suite for your program passes correctly. After the tests
pass, you should add at least four more test cases that all successfully
demonstrate that your program is working correctly.

Finally, you should edit the file, called `README.md`, in your GitHub
repository. This file should contain all of the sections that are described in
the main assignment sheet. Note that you will need to delete most of the
existing content in the `README.md` file to create the final content needed for
this submission. Don't forget that you should also apply linting tools to both
your Python source code and your Markdown-based writing.

## Updates

If the course instructor updates the provided material for this assignment and
you would like to receive these updates, then you can type this command in the
main directory for this assignment:

```
git remote add download git@github.com:Allegheny-Computer-Science-280-F2017/cs280-F2017-lab3-starter.git
```

You should only need to type this command once; typing the command additional
times may yield an error message but will not negatively influence the state of
your repository. Now, you are ready to download the updates provided by the
course instructor by typing:

```
git pull download master
```

This second command can be run whenever the course instructor needs to provide
you with new source code for this assignment. However, please note that, if you
have edited the files that the course instructor updated, running the previous
command may lead to Git merge conflicts. If this happens, you may need to
manually resolve them with the help of the course instructor.

## Travis

This assignment uses [Travis CI](https://travis-ci.com/) to automatically run
the test suite for the program every time you commit to your GitHub repository.
The checking will start as soon as you have accepted the assignment, thus
creating your own private repository, and the course instructor enables Travis
for it. If you are using Travis for the first time, you will need to authorize
Travis CI to access the private repositories that you created on GitHub.

## Problems

If you have found a problem with this assignment's provided source code, then
you can go to the [Computer Science 280 Lab 3
Starter](https://github.com/Allegheny-Computer-Science-280-F2017/cs280-F2017-lab3-starter)
repository and create an issue by clicking the "Issues" tab and then clicking
the green "New Issue" button. To ensure that your issue is properly resolved,
please provide as many details as is possible about the problem that you
experienced. If you discover a problem with the laboratory assignment sheet,
then please raise an issue in the
[cs280-F2017-lab-sheets](https://github.com/Allegheny-Computer-Science-280-F2017/cs280-F2017-lab-sheets)
repository and mention this assignment.

Students who find, and use the appropriate GitHub issue tracker to correctly
document, a mistake in any aspect of this laboratory assignment will receive
free laptop stickers and extra credit towards their grade for it.

## Assistance

If you are having trouble completing any part of this project, then please talk
with the course instructor. Alternatively, you may ask questions in the Slack
team for this course. Finally, you can schedule a meeting during the course
instructor's office hours.
