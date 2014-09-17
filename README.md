python-for-the-stoopid
======================

I know perl &amp; java - not Python - but you gotta start somewhere; join me in my idiotic baby-steps to usefulness
------

Here's an interesting bit that I picked up:

>>> NewType = type("NewType", (object,), {"x": "hello"})
>>> n = NewType()
>>> n.x
"hello"

which is exactly the same as

>>> class NewType(object):
>>>     x = "hello"
>>> n = NewType()
>>> n.x
"hello"

20140908.1538

From a more concrete perspective, Python programs can be decomposed into modules, statements, expressions, and objects, as follows: 
1. Programs are composed of modules. 2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects. 


------

20140908.0849

More learning!

Namespaces are collections of (name, object reference) pairs (implemented using dictionaries).

------

20140904.2149

IDLE.. it is called IDLE... it is not "***IDEA***"

*That* is something else entirely...  ::slaps-own-face::

20140904.2124

PyDev on Eclipse.  That's the one.

I find my chouces are constrained severely by the fact that I'm running Snow Leopard.  It is amazing how long a Windows or Linux build will remain viable & supported ***even by Apple*** but an aging OS/X rev bearer can basically go eat shit.  :sigh: 

But I'm off-topic right?  meh

------
20140904.1131

Zarquon's-see-through-sandals IDLE is a piece of rubbish!  Even on a multi-core system it is unforgivably slow.

I can see why it exists - from a purely *academic* point of view - pun intended.  You want students to work with such basic crap that they outgrow it almost instantly..  But wow - talk about painful!

The code completion is so slow (on a modern multi-core desktop) as to be completely unusable.

I have opted for a purpose-built EasyEclipse IDE which seems to behave a bit more reasonably - but then am I just more comfortable because I have used Eclipse before?  I doubt others would find it so familiar nor inviting.

Why do developer tools have to look like such budget store garbage?  Don't we have any sense of pride?

------
20140904.1023

There needs to be more Monty Python references.

I don't *care* if you think it is a "generational thing" - that's **bollocks**.  

I love all kinds of stuff from previous generations.  Do I *get* 100% of the content?  No & It doesn't matter.  

The 80/20 rule applies.

------
20140904.0049

I don't *remember* the naming conventions - so I'm going to try to look around & see what everyone else is doing again
I do however grok namespaces - at least in the large grain.

Once again, like everything else in the language, the approach to it strikes me as extremely *relaxed*.

I have been writing a lot of tiny scripts to try things out as I go.

I have to keep stopping myself from putting a semicolon at the end of each line.  It still feels wrong.

------
20140903.1512

So SQLLite is included in Python since 2.5?  SRSLY?

Welcome to Cargo Cult Programming 101



And you know.. for a book called "Learning Python" I'm starting Chapter 3 and I have only run one **Hello, World** program..?

------
20140902.2358

I have been digging into *Learning Python* - the book & the persuit.

As usual, I chafe against the language bigotry and the mudslinging but everyone needs to justify themselves & part of that
is always going to be distinguishing yourself from others in the form of Strongly Held and venomously defended Beliefs.

Also, predictably I am still *bugging out* a little bit about the loose nautre of things.  Stuff that only a Java programmer
could possibly care about.

But the point here is specifically to *learn*.  So I check myself.

And learn I have.

------
20140830.2319

Today I discovered <a href="http://legacy.python.org/dev/peps/">"PEP"'s</a> - Pyhton Enhancement Proposals.

I read <a href="http://legacy.python.org/dev/peps/pep-0008/">PEP8 - The Style Guide for Python code</a>.

As someone whom has been writing code for >3 decades it seemed like a good next step in terms of being able to 
read & write code properly.  I really wanted to know what the Naming Conventions are.

It was very enlightening & made parsing this unfamiliar code much less intimidating.

I have also gone back to poking at <a href="http://omz-software.com/pythonista/">Pythonista</a> on my iOS devices and it really is great stuff!  It is helping me learn much faster than I would otherwise.

------

So the first thing that I have learned of note is that Python has a package management tool called pip.

I used it & it was far less painful, cryptic & verbose than CPAN...

I also learned that No - you do not have to use tabs.  I used my standard 2 space convention & it worked just fine...

*However* it is worth noting that cutting & pasting text can be a real bummer if your text editor doesn't play nicely.

-----

