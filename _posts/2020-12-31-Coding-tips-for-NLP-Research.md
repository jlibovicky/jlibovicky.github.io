---
layout: post
title: "Coding Tips for Python for NLP Research"
tags: [mt-weekly, en]
lang: en
---

This is yet another blog post where a clever-clever person writes pearls of
wisdom about how other should write their code. In what follows in this post, I
try to summarize some of my personal best practices in writing Python code for
research in NLP and share some code snippets that I tend to copy from one
project into another.

Writing code for NLP research has some specifics that makes it different from
developing code for production use and therefore many standard axioms of
software engineering do not hold. On the other hand, there

### Reproducibility and Basic Experiment Management

There is no reproducibility without versioning. However, having the code base
in git does not guarantee itself that you will know at what stage your
repository were at when you run specific experiements. There are many tools for
experiment management in machine learning, but experience is that they mostly
have a steep learning curve and almost never do what I need. What I do instead
that I keep experiments in directories, __one directory per experiment__.

To ensure, I can replicate the experiments with the same code base, I always
__store the commit hash and the diff from the last commit__ alongside with the
experiment.

```python
def save_git_info(git_commit_file: str, git_diff_file: str,
                  branch: str = "HEAD") -> None:
    repo_dir = os.path.dirname(os.path.realpath(__file__))

    with open(git_commit_file, "wb") as file:
        subprocess.run(["git", "log", "-1", "--format=%H", branch],
                       cwd=repo_dir, stdout=file, check=False)

    with open(git_diff_file, "wb") as file:
        subprocess.run(
            ["git", "--no-pager", "diff", "--color=always", branch],
            cwd=repo_dir, stdout=file, check=False)
```

The usual way of setting the experiment parameters is via command-line options
(using the `argparse` package in Python). I save the command line options in a
yaml format (using the [`pyaml`](https://github.com/mk-fg/pretty-yaml)
package).

```python
args_dict = {}
for key, val in args.__dict__.items():
    if isinstance(val, _io.TextIOWrapper):
        args_dict[key] = os.path.realpath(val.name)
    else:
        args_dict[key] = val

with open(os.path.join(experiment_dir, "args"), "w") as file:
    print(yaml.dump(args_dict), file=file)
```

### Logging is documentation

Large part of the source code for NLP experiments are scripts which are
literary scripts: some scenarios performing steps one after each other.

And of course Tensorboard -- is an invaluable tool.

### Linters are not bullies, but friends

Unlike compiled languges, where the compiler tells you plenty of stuff that
very likely indicate bug (e.g., unused variables), Python allows to write
whatever you wish, sometimes leading to very sofisticated bugs. This is the
reason why I often use `pylint` in my projects. By default pylint is very
strict about the code style, however, it is fully configurable.

Sometimes, I use a tool called `mypy` for static type checking. This requires
writing type annotations to your methods (just as you can in the code snippets
in this post). Although I already managed to spot several bugs that would be
otherwise hard to find, I am still not really sure if the effort you need to
make to annotate the types in the code pays off or not.

### Test moderately, but test

People with software engineering background tend to have an obcession that
every single line of code needs to be covered by unit tests. Test-driven
development sounds like a wonderful concept, but it is very hard to do it in
practice
