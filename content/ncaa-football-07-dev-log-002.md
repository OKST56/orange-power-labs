# NCAA Football 07 Recomp — Dev Log #002: Cracking Open NCAA Football 07

*Orange Power Labs | Development Journal #002*

## Getting Under the Hood

In our first development log, I introduced the NCAA Football 07 Recomp project and explained why bringing this childhood favorite to modern PCs means so much to me.

Now it's time to get our hands dirty.

Before we can even think about playing NCAA Football 07 as a native Windows application, we need to understand what we're working with.

That means digging into the original Xbox version of the game, examining its files, and beginning to understand how its executable was built.

Our first two technical research milestones have given us a much clearer picture of what lies ahead.

And we've already made some interesting discoveries.

## Milestone 002: Exploring the Original Xbox Game

Our first major task was examining the original Xbox game image.

Original Xbox games use a filesystem called **XDVDFS**, which is how the console organizes and accesses files on a game disc.

Think of it like opening a folder on your computer. Instead of immediately running the game, we're looking at everything inside it to understand how the pieces fit together.

Our initial inspection identified **88 files** within the NCAA Football 07 game image.

Among those files was the most important one for our immediate research:

**`default.xbe`**

An XBE, or Xbox Executable, is the original Xbox equivalent of a Windows `.exe` file.

It's the executable that contains the machine code the console uses to run the game.

For our recompilation project, understanding this file is essential.

We're not simply trying to extract the game's textures, stadiums, or player information. We're investigating the actual program instructions that make NCAA Football 07 function.

And `default.xbe` is where that investigation begins.

## Discovering What's Inside the Executable

Our analysis of `default.xbe` revealed several important details.

The executable contains **15 sections**, which are organized regions of the program used to store code, data, and other information needed during execution.

We also identified **XDK version 5849**.

The XDK, or Xbox Development Kit, was the software development environment used to build games for the original Xbox.

Knowing the XDK version provides valuable context when researching the Xbox system libraries and runtime behavior that the game expects.

Another important discovery was the executable's imported symbols.

Our research identified **152 imported symbols** associated with the Xbox environment.

These imports represent functions or references the game expects the console's system software to provide.

For example, a game might need to allocate memory, interact with system resources, or request services from the Xbox kernel.

On an original Xbox, those services are part of the environment the game was designed to run in.

On Windows, we have to investigate how to provide compatible behavior.

That's one of the fundamental challenges of recompilation.

Translating a game's machine code is only part of the equation. The translated code also needs an environment where its original system dependencies can function.

## Milestone 003: Understanding xboxrecomp

With the initial executable inspection complete, our next task was studying the framework we're using to investigate recompilation.

That framework is **xboxrecomp**.

Rather than immediately building our own tools or inventing a custom recompilation process, we're prioritizing the official xboxrecomp documentation and its established development pipeline.

Our research included examining the framework's structure, its instructions, and the steps involved in preparing original Xbox executables for translation.

One of our early objectives was understanding how the game's imported Xbox functions would be handled.

During this milestone, we established routing information for all **152 identified imports**.

This is an important research result, but it comes with a distinction.

Having a route identified for an imported function does not automatically mean that function has a complete, tested Windows implementation.

It means we've begun accounting for the dependencies the game will eventually need.

There's still considerable work ahead to determine whether those routes can provide the correct behavior when the translated game code actually runs.

We also identified additional compatibility and tooling questions that will need to be resolved as development continues.

## Why These Discoveries Matter

At first glance, counting files, examining executable sections, and cataloging imported functions might not sound particularly exciting.

After all, we haven't even reached a playable game yet.

But these are exactly the kinds of discoveries that make a recompilation project possible.

Imagine trying to rebuild an engine without knowing what components it contains or how those components interact.

That's essentially the challenge we're facing.

The original Xbox executable was built for a completely different software environment. Before we can translate it into something Windows understands, we need to identify its components, understand its dependencies, and determine how to reproduce the behavior it expects.

Our first research milestones have started that process.

We now have a better understanding of the game's file structure, the executable we're investigating, and the Xbox system dependencies that must eventually be addressed.

We've also established a clearer direction for using xboxrecomp rather than proceeding through guesswork.

## What We Haven't Accomplished Yet

It's important to keep our progress in perspective.

At this stage of development, we have **not** produced a working native Windows version of NCAA Football 07.

We haven't demonstrated a complete recompiled executable, successfully booted the game on Windows, or reached playable gameplay.

Our achievements so far are in executable inspection, dependency research, and preparation for the recompilation process.

Those are meaningful steps, but they're still early steps.

The real challenge will be turning this research into functioning native code.

## What's Next? Mapping the Game's Functions

With the executable identified and its initial dependencies investigated, our next phase focuses on understanding the game's internal code.

We'll begin examining how many potential functions exist inside `default.xbe`, how those functions interact, and what information xboxrecomp needs before attempting to translate them.

We'll also be investigating something called the **Application Binary Interface**, or ABI.

In simple terms, an ABI describes the rules that compiled code follows when functions communicate with one another, including how arguments are passed and how results are returned.

Getting those details right will be essential for producing reliable native Windows code.

This next phase will be more technical, but it also brings us closer to the central goal of the project: translating the original game's instructions into code that can eventually run outside the Xbox.

For now, we've officially opened up NCAA Football 07 and begun understanding what makes it tick.

It's a small step toward a much bigger goal.

But every successful recompilation has to start somewhere.

**And for Orange Power Labs, the journey is officially underway.**

**#GoPokes**

*— Orange Power Labs*