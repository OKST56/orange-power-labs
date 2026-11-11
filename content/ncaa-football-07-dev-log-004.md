# NCAA Football 07 Recomp — Dev Log #004: Our First Native Windows Object File

*Orange Power Labs | Development Journal #004*

## From Research to Actual Recompilation

In our previous development log, we took a deep dive into the original Xbox version of NCAA Football 07 and began mapping the game's internal code.

Our analysis identified an incredible **33,755 potential functions and 46,466 analysis entries** inside the executable.

But we also discovered some significant challenges.

Function boundaries weren't always clear, thousands of entries contained uncertain assumptions, and we still needed to determine whether our tools could reliably translate the original Xbox instructions into code that Windows could understand.

Now, after four more development milestones, we've reached our first tangible recompilation achievement.

**We've successfully compiled a small piece of NCAA Football 07 into a native Windows object file.**

It's not a playable game. It's not even a complete executable yet.

But for the first time, we've moved beyond analyzing the original Xbox code and successfully produced a compiled Windows artifact from our recompilation work.

And that's an exciting milestone for Orange Power Labs.

## Milestone 006: Lifting Our First Function

Our first objective was to take everything we'd learned about the game's executable and attempt a controlled function-lifting experiment.

Rather than trying to translate tens of thousands of functions simultaneously, we selected one function for an initial test.

That function was located at:

**`0x00026D40`**

This hexadecimal address identifies a specific location in the original Xbox executable.

Using our recompilation workflow, we generated a small lifting artifact representing this function.

The result was a **17-line C source artifact totaling 322 bytes**.

That might not sound particularly impressive compared to the size of an entire football game.

But the significance wasn't the amount of code generated.

It was demonstrating that we could take an identified portion of the original executable and produce a source-level artifact for the next stage of recompilation.

This was our first practical step toward translating the game's original machine instructions into something a modern Windows compiler could process.

Of course, generating source code doesn't automatically mean that code is correct or executable.

We still needed to build it.

## Milestone 007: Preparing the Windows Compilation Environment

With our first lifting artifact available, the next challenge was preparing the environment needed to compile it.

Our project uses the **xboxrecomp** framework, and we've made following its official documentation and development pipeline a priority.

During Milestone 007, we established a compilation scaffold based on the framework's template.

A compilation scaffold is essentially the supporting project structure that allows generated code to be passed into a compiler.

Think of it as preparing the workshop before attempting to assemble the first component.

We needed the correct source files, compiler configuration, supporting headers, and build instructions.

The initial scaffold was considered conditionally ready, meaning the necessary structure had been prepared, but a successful compilation had not yet been demonstrated.

We also encountered an environment limitation involving PowerShell execution policy that prevented part of the qualification process from completing normally.

The next step would be attempting an actual compilation and determining what still needed attention.

## Milestone 008: Our First Compilation Attempt Fails

Our first attempt to compile the lifted function didn't go as planned.

The Microsoft C++ compiler stopped with an error:

**`C1083: Cannot open include file: 'stdint.h'`**

For anyone unfamiliar with C programming, `stdint.h` is a standard header that defines common integer types.

These types help programmers specify exactly how large certain numbers should be in memory.

That precision is particularly important when working with low-level code originally designed for a different hardware environment.

The problem wasn't necessarily with the original NCAA Football 07 instructions.

Instead, our selected compilation environment couldn't locate a required standard header.

This meant we had encountered a toolchain configuration problem before we could properly evaluate the generated code.

It's a good example of how recompilation involves much more than translating machine instructions.

Even a tiny function depends on having a correctly configured development environment.

Our first compilation attempt produced no usable object file.

But the error gave us a specific problem to investigate.

## Milestone 009: Our First Successful Windows Compilation

After investigating the compilation environment, we adjusted the toolchain configuration and attempted the build again.

This time, we successfully compiled the lifted function using the Microsoft Visual C++ toolchain.

The result was:

**`sub_00026D40.obj`**

A **1,310-byte Windows x64 COFF object file**.

This is our first successfully compiled native Windows object artifact from the NCAA Football 07 recompilation project.

For those unfamiliar with the terminology, an object file is an intermediate product of compilation.

When a compiler translates source code into machine code, it commonly produces object files before those pieces are linked together into a complete executable.

In other words, we've successfully created one small compiled component.

We haven't assembled the entire application.

But this result demonstrates that our workflow can take an individual lifting artifact and compile it into the Windows x64 object-file format.

That's a meaningful technical achievement.

Our Milestone 009 report also recorded **87 out of 87 preservation checks passing**.

Those checks provided additional validation of the milestone's preservation requirements, although they do not establish that the complete game behaves correctly.

The important result is that we've moved from theoretical research into a successful, verifiable compilation experiment.

## Why This Is Such an Important Step

When we started this project, our first questions were fairly basic.

Could we inspect the original Xbox game files?

Could we identify the executable?

Could we map its internal functions?

Could we begin translating those functions into a form that modern development tools could understand?

And now we've answered another important question.

**Can we compile one of our generated function artifacts into a native Windows object file?**

Yes.

That doesn't mean the remaining work will be easy.

In fact, the challenges ahead are significantly larger.

A complete game consists of enormous amounts of interconnected code, data, and system behavior.

Even if we successfully compile thousands of functions, those functions must still work together correctly.

We'll also need to address the original Xbox services the game depends on, including memory management, graphics, audio, input, and other runtime functionality.

But every large recompilation project needs a way to validate its smallest building blocks.

This milestone gives us an initial foundation for doing exactly that.

## What We Still Haven't Accomplished

It's worth emphasizing what this milestone does and doesn't represent.

We've successfully produced a Windows x64 object file from one of our function-lifting experiments.

However, we have **not yet demonstrated a complete linked NCAA Football 07 executable**.

We also haven't successfully booted the game natively on Windows or reached playable gameplay.

Compiling an individual function doesn't guarantee that it will behave correctly when connected to the rest of the game.

And it certainly doesn't mean we've finished recompiling NCAA Football 07.

We're still in the early stages of a much larger technical process.

But we've now demonstrated an important part of the pipeline.

## What's Next? From One Function to a Larger Build

With our first object file successfully produced, the next challenge is expanding the recompilation process.

Rather than working with only one function, we'll need to investigate how the workflow handles larger groups of functions and how those compiled components can eventually be linked together.

We'll also continue studying the xboxrecomp framework's runtime requirements and build process.

The long-term objective remains the same: produce a native Windows application capable of running NCAA Football 07.

And beyond that, we still have the bigger dream of eventually transforming the game into a Missouri High School Football experience.

But for now, we're focused on building the technical foundation one milestone at a time.

Four development logs into this journey, we've gone from a childhood favorite and an ambitious idea to examining the original Xbox executable, mapping thousands of potential functions, and successfully compiling our first piece of native Windows code.

There's still a tremendous amount of work ahead.

But this is the kind of progress that makes the project feel a little more real.

**For the first time, a small piece of our NCAA Football 07 recompilation work has successfully become native Windows machine code.**

And that's a milestone worth celebrating.

**#GoPokes**

*— Orange Power Labs*