# 42 — Object Oriented Programming

*Projects completed as part of the 42 curriculum by **ybarakat** at 42 Irbid.*

## About this module

This module goes deep into Python and modern software design: building clean, maintainable applications with classes, inheritance and design patterns. Along the way it covers data manipulation and visualization, functional programming and game development, ending with interactive projects. The goal is to think in objects and write solutions that are both powerful and Pythonic.

## Projects

Listed in curriculum order.

| Project | Topic | Highlights |
|---|---|---|
| [Growing Code](./Growing_Code) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/7a62d887-12d0-4560-9ed9-00b9c523200e) | Python basics | Functions, input, loops, and recursion vs. iteration |
| [Code Cultivation](./Code_Cultivation) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/89ff3426-b2e2-49af-8272-13be2eaeb9b5) | Classes and OOP | `Plant` → `FloweringPlant` → `PrizeFlower` inheritance, encapsulation, factories, a `GardenManager` |
| [Garden Guardian](./Garden_Guardian) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/45047a96-901d-4a89-b1cb-ee9a7f5e5fce) | Exceptions | `try` / `except` / `finally`, `raise`, custom exception hierarchies (`GardenError`, `PlantError`, `WaterError`) |
| [Data Quest](./Data_Quest) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/2e9998c7-a91e-4d28-bcaa-b2dd711d8206) | Built-in data structures | Lists, tuples, sets, dicts, comprehensions, generators, `sys.argv` |
| [Data Archivist](./Data_Archivist) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/137a983f-650c-4dd5-8998-b09362d81373) | File I/O | Reading and writing files, context managers, stdin/stdout/stderr, handling `FileNotFoundError` and `PermissionError` |
| [Code Nexus](./Code_Nexus) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/f0429eb2-6d8b-45b3-aab0-d1ff991aa196) | Abstraction and interfaces | `ABC`, `typing.Protocol`, polymorphic processors, data pipelines with export plugins (CSV / JSON) |
| [The Codex](./The_Codex) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/fc0c1757-6a2d-4a37-ba04-e34545acd9da) | Modules and packages | Package layout, `__init__.py`, absolute vs. relative imports, circular-import pitfalls |
| [Data Deck](./Data_Deck) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/2cab3c34-11c5-4fd2-a8a3-5caa64e839f7) | Design patterns | Abstract Factory (creature factories), Strategy (battle strategies), capability mixins, a tournament runner |
| [The Matrix](./The_Matrix) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/39a30f54-3d1d-4d54-bbf7-91530dc61db6) | Environments, dependencies and visualization | Virtual environments, `pip` vs. Poetry (`requirements.txt` / `pyproject.toml`), data analysis and plots with numpy / pandas / matplotlib, `.env` configuration with `python-dotenv` |
| [Cosmic Data](./Cosmic_Data) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/9d7e2c95-0c39-467f-81f6-b1aeee8f2641) | Data validation | `pydantic` models, `Enum`, validators, `datetime` |
| [Func Mage](./Func_Mage) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/33555d78-bbb9-4c9c-8bbd-61d7b0cecd7f) | Functional programming | Lambdas, higher-order functions, closures and scope, `functools` (`partial`, `lru_cache`, `reduce`), decorators |
| [A-Maze-ing](https://github.com/yazeedbarakat/A-Maze-ing) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/c945e872-0716-46ea-908f-6a69231bc0a7) | Project | Maze generation project *(submodule, with Adnan)* |
| [Pacman](https://github.com/yazeedbarakat/Pacman) · [subject](https://code.42.tech/modules/f793ba7d-d0d7-4bc4-b599-6ff4281e9bfb/projects/c8d6661e-0436-4d4d-b997-d33b24cf979a) | Game development | Pac-Man in Python / pygame *(submodule, with Adnan)* |

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
