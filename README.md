# 42 — Object Oriented Programming

*Projects completed as part of the 42 curriculum by **ybarakat** at 42 Irbid.*

## About this module

This module goes deep into Python and modern software design: building clean, maintainable applications with classes, inheritance and design patterns. Along the way it covers data manipulation and visualization, functional programming and game development, ending with interactive projects. The goal is to think in objects and write solutions that are both powerful and Pythonic.

## Projects

Listed in curriculum order.

| Project | Topic | Highlights |
|---|---|---|
| [Growing Code](./Growing_Code) | Python basics | Functions, input, loops, and recursion vs. iteration |
| [Code Cultivation](./Code_Cultivation) | Classes and OOP | `Plant` → `FloweringPlant` → `PrizeFlower` inheritance, encapsulation, factories, a `GardenManager` |
| [Garden Guardian](./Garden_Guardian) | Exceptions | `try` / `except` / `finally`, `raise`, custom exception hierarchies (`GardenError`, `PlantError`, `WaterError`) |
| [Data Quest](./Data_Quest) | Built-in data structures | Lists, tuples, sets, dicts, comprehensions, generators, `sys.argv` |
| [Data Archivist](./Data_Archivist) | File I/O | Reading and writing files, context managers, stdin/stdout/stderr, handling `FileNotFoundError` and `PermissionError` |
| [Code Nexus](./Code_Nexus) | Abstraction and interfaces | `ABC`, `typing.Protocol`, polymorphic processors, data pipelines with export plugins (CSV / JSON) |
| [The Codex](./The_Codex) | Modules and packages | Package layout, `__init__.py`, absolute vs. relative imports, circular-import pitfalls |
| [Data Deck](./Data_Deck) | Design patterns | Abstract Factory (creature factories), Strategy (battle strategies), capability mixins, a tournament runner |
| [The Matrix](./The_Matrix) | Environments, dependencies and visualization | Virtual environments, `pip` vs. Poetry (`requirements.txt` / `pyproject.toml`), data analysis and plots with numpy / pandas / matplotlib, `.env` configuration with `python-dotenv` |
| [Cosmic Data](./Cosmic_Data) | Data validation | `pydantic` models, `Enum`, validators, `datetime` |
| [Func Mage](./Func_Mage) | Functional programming | Lambdas, higher-order functions, closures and scope, `functools` (`partial`, `lru_cache`, `reduce`), decorators |
| [A-Maze-ing](https://github.com/yazeedbarakat/A-Maze-ing) | Project | Maze generation project *(submodule, with Adnan)* |
| [Pacman](https://github.com/yazeedbarakat/Pacman) | Game development | Pac-Man in Python / pygame *(submodule, with Adnan)* |

## Cloning

`A-Maze-ing` and `Pacman` are git submodules that point to their own repositories. To get them as well:

```bash
git clone --recurse-submodules https://github.com/yazeedbarakat/42-Object_Oriented_Programming.git
```

If you already cloned without that flag:

```bash
git submodule update --init --recursive
```

## Running

Requires Python 3.10+ (The_Matrix targets 3.13). Each exercise is a standalone script:

```bash
python3 Growing_Code/ex0/ft_hello_garden.py
```

Modules with third-party dependencies:

```bash
pip install pydantic                              # Cosmic_Data
pip install -r The_Matrix/ex1/requirements.txt    # The_Matrix ex1 (numpy, pandas, matplotlib)
pip install python-dotenv                         # The_Matrix ex2
cp The_Matrix/ex2/.env.example The_Matrix/ex2/.env
```
