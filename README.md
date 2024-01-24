# superhuman-gpt

## Philosophy

One thing people often criticize LLM is that it only knows existing knowledge, but cannot generate new or innovative contents for human.  

However, we are the ones that trained LLMs with texts that we deem as good or true. We limit LLMs to human knowledge, so it certainly cannot generate things beyond our knowledge.  

But this repo is to break this boundary. LLMs are trained to understand 1. _What human know_. 2. _What human want_. If we take the negation of 1 then AND it with 2, it's possible to 
generate unknown knowledge that can be beneficial for human, i.e. the "new knowledge" that we dream of.

## Experiment 1 [(code)](https://github.com/ScottLinnn/superhuman-gpt/tree/experiment-1)

It's hard to directly ask LLMs to generate ^1. 

- One way is changing the architecture to intentionally generate the lowest probability words, but that could be too expensive as an initial experiment.
- Another way is simply promting LLM to do so, but what I got is "due to OpenAI's policy, I can't do this..."
- So I start with making a random word generator that outputs pairs of words _absolutely randomly_. The idea/philosophy here is that what human don't know lie within the unprecedent, unreasonable combination of
words, so we can generate the "unknown" by randomly combining words, then we can leverage LLM's inference ability to judge if any values or any inspirations can be drawn from the words. Of course, it doesn't have to be
pairs, it can be any length, but I need to figure out the computation and running plan before implementing that.

What I got looks like this: 

```
------------------------------------
Current words are: rutin, otomycosis

The idea can be used in the field of medical research and treatment.

The idea is to explore the potential use of rutin, a natural compound found in many plants, as a therapeutic agent for treating otomycosis, a fungal infection of the ear. Rutin's antifungal properties could be harnessed to develop a novel and effective treatment to combat otomycosis, providing a natural and safe alternative to current medications.
------------------------------------
Current words are: unvisionary, Leora

The idea can be used in the field of personal development and self-improvement.

The idea is to combine the concept of being unvisionary with the name Leora to create a character who starts off with a lack of vision but overcomes obstacles to become an inspiring figure. This idea can be used to teach the importance of perseverance, self-belief, and the ability to redefine oneself in the face of adversity.
------------------------------------
Current words are: muscid, hemoclasia

The idea can be used in the field of medical research and innovation.

By studying the muscid fly and its ability to cause hemoclasia (blood clotting), scientists can develop novel methods for controlling and preventing bleeding disorders in humans. This could lead to the development of new treatments or therapies that improve blood clotting mechanisms in patients with hemophilia or other bleeding disorders.
```

Seems like a thing, but there are some problems I observe, and my next step is to build a multi-agent system to address these problems:

1. Too many professional terminologies or uncommon words. We need a _consultant_ to understand the contents.
2. Many of the generated contents seem to be BS. We need a _verifier_ to filter the BS.
3. It only generates simple ideas, we need a _designer_ to expand the idea to a feasible, specific plan.

Next time when I have time to work on this, I will try to build this agent system!

