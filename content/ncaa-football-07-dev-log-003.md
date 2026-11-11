# NCAA Football 07 Recomp — Dev Log #003: Mapping the Game: 33,755 Functions and Our First Major Roadblocks

*Orange Power Labs | Development Journal #003*

## From Exploring Files to Understanding Code

In our previous development log, we cracked open the original Xbox version of NCAA Football 07 and began examining what makes the game work.

We identified the game's executable, investigated its structure, and started mapping the Xbox system functions it depends on.

Now we're moving into something considerably more complicated.

**Understanding the actual code inside NCAA Football 07.**

Our next two development milestones focused on analyzing the game's executable, identifying potential functions, and determining how much of that code might be ready for translation into native Windows code.

And the results gave us a much better understanding of just how big this project really is.

## Milestone 004: Mapping Thousands of Functions

One of our first major research tasks was analyzing the executable to identify its internal functions.

A function is essentially a collection of instructions designed to perform a particular task.

In a football game, functions might be responsible for processing controller inputs, updating player movement, calculating gameplay logic, managing menus, or handling countless other operations.

The game relies on enormous numbers of these individual pieces working together.

Our initial analysis identified:

- **33,755 potential functions**
- **46,466 analysis entries**

These numbers immediately illustrated the scale of what we're investigating.

However, there's an important distinction here.

The 33,755 functions are **candidates identified through analysis**, not 33,755 individually verified functions that are ready to be recompiled.

Some candidates may represent genuine functions. Others may require additional investigation to determine their boundaries, purpose, or relationship to surrounding code.

Likewise, the 46,466 analysis entries represent information generated during our investigation, not 46,466 confirmed working components.

This is a crucial part of our development philosophy: distinguishing what our tools identify from what we've actually verified.

Still, these results provide an important starting point.

We now have an initial map of a substantial portion of the executable's potential code structure.

## Understanding the ABI Problem

Another major focus of Milestone 004 was investigating the game's **Application Binary Interface**, or ABI.

That sounds complicated, but the basic concept is fairly straightforward.

Imagine two people trying to communicate using a set of rules.

They need to agree on how information is delivered, where it goes, and how responses are returned.

Computer functions work in a similar way.

An ABI defines important rules about how compiled functions interact, including how arguments are passed, which registers are used, and how results are returned.

These details matter enormously when translating code from one environment to another.

The original Xbox used a 32-bit x86 processor, while our target is a modern 64-bit Windows environment.

Even when the underlying instructions can be analyzed, the translated functions still need to communicate correctly.

If those rules are misunderstood, the resulting program may compile but behave incorrectly when executed.

During our analysis, we generated ABI information for the game's function candidates.

However, **27,224 entries relied on low-confidence default assumptions**.

That was a significant finding.

It meant that while we had produced a large amount of useful information, much of it still needed additional validation before we could confidently rely on it for recompilation.

And that led directly into our next milestone.

## Milestone 005: Are We Actually Ready to Translate the Code?

With our initial function map and ABI information available, the next logical question was:

**Can we safely begin translating these functions into native code?**

This process is often called *lifting*.

In recompilation, lifting generally refers to translating machine instructions from the original executable into another representation that can be compiled or processed for the target platform.

For our project, the goal is to eventually turn the original Xbox game's code into something that can become part of a native Windows application.

But before attempting that at scale, we needed to investigate the reliability of our analysis.

Our readiness evaluation uncovered several issues.

One finding involved **761 overlaps** identified during analysis.

Overlapping code regions can complicate the process of determining where one function begins and another ends.

They don't automatically mean the executable is damaged or that recompilation is impossible.

But they do mean we need to be careful about trusting every automatically identified function boundary.

We also encountered uncertainty involving **thunks**.

A thunk is a small piece of code that typically redirects execution or helps connect one function to another.

These can be perfectly normal parts of a compiled program.

The challenge is correctly identifying them.

Our analysis included thunk classifications based on heuristics, meaning the tools were making educated determinations using recognizable patterns rather than confirming every case individually.

That introduced another area where additional verification was necessary.

Taken together, the function overlaps, uncertain classifications, and low-confidence ABI information showed that our broader lifting process was not yet ready to proceed without additional work.

## Why We Didn't Just Push Ahead

One of the easiest mistakes in a project like this would be treating every generated analysis result as correct and immediately attempting to translate the entire game.

That might produce a tremendous amount of output.

But producing output isn't the same thing as producing working code.

If our function boundaries are incorrect, our ABI assumptions are unreliable, or our control-flow analysis misses important behavior, those problems can carry directly into the translated program.

And tracking down thousands of errors afterward would be considerably more difficult than addressing the underlying problems early.

So instead of rushing into full-scale recompilation, our research highlighted the importance of validating smaller pieces of the process first.

We need to understand what our tools are doing, identify where their assumptions are weakest, and establish reliable ways to test the generated results.

That may not be the fastest-looking route to a working game.

But it's a much more defensible engineering approach.

## A Different Kind of Progress

This development log doesn't end with a playable game, a new menu, or even a successfully compiled executable.

Instead, it ends with something equally important for this stage of development.

**A clearer understanding of the problems we need to solve.**

We've identified tens of thousands of potential functions inside NCAA Football 07.

We've generated a substantial body of analysis information.

We've begun investigating the calling conventions and compatibility requirements involved in translating the game's code.

And we've identified several limitations that prevent us from treating the initial analysis as fully verified.

These findings give us a more realistic picture of the work ahead.

The project is moving beyond simply understanding the executable's structure and toward understanding whether its individual pieces can be translated reliably.

## What's Next? Our First Function Lifting Experiment

Our next step is to move from broad analysis into a much smaller, more controlled experiment.

Rather than attempting to translate thousands of functions at once, we'll focus on generating and validating a lifting artifact for an individual function.

This will allow us to begin testing the recompilation pipeline on a manageable scale.

We'll also need to prepare the Windows compilation environment and investigate how the generated code interacts with the framework's supporting components.

There's still a long way to go before NCAA Football 07 can run natively on Windows.

But the project is beginning to transition from studying the game's executable to experimenting with actual code translation.

And that's an exciting step forward.

**We're not just looking inside NCAA Football 07 anymore. We're beginning to figure out how to rebuild it.**

**#GoPokes**

*— Orange Power Labs*