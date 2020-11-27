The Idea:

A bunch of scripts to experiment with parallelism and concurrency in python.
There are a lot of ways to do this in python but none of them are straight
forward imho.

Multiprocessing:
For highly CPU intensive task we tend to want to run things in parallel.
If things are big / complex enough then just use spark. However we can 
also do the following.
- run python scripts from a bash script where the bash script just fires off
python processes to run. This is very easy but only really useful if you don't care
about what you get back i.e. bulk clean of large number of csvs, where each process 
picks up a csv cleans it and puts it somewhere else
- run python scripts as subprocesses in python, or alternative run bash or unix commands
This is slightly better than the previous as it give you more control, but still not great.
- concurrent.futures ProcessPoolExectuor. This is the most "magic" it handles a lot of 
stuff but can be a bit tricky to get to work.

Concurrency:
Threads, or AsyncIo


