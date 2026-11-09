# Лабораторная работа №1: Языки программирования, терминал и Git

**Студент:** [Столыпин Александр]  
**Группа:** [М3О-111БВ-26]  
**Номер в списке:** [23]  
**ОС:** Windows

## Цель
Изучить различия между языками программирования и их инструментальными экосистемами, научиться запускать программы из терминала и организовывать разработку средствами Git.

## Языки
- C, C++, Python, JavaScript, TypeScript
- Java, C#, F#, Go, Rust
- Bash, Prolog, Assembler

## Инструменты
| Язык | Версия | Команда сборки |
|------|--------|----------------|
| C | GCC 16.2 | `gcc -Wall -Wextra -pedantic main.c -o main` |
| C++ | G++ 16.2 | `g++ -Wall -Wextra -pedantic main.cpp -o main` |
| Python | 3.x | `python3 main.py` |
| JavaScript | Node.js | `node main.js` |
| TypeScript | tsc | `tsc main.ts && node dist/main.js` |
| Java | JDK | `javac Main.java && java Main` |
| C# | .NET SDK | `dotnet run` |
| F# | .NET SDK | `dotnet run` |
| Go | Go toolchain | `go run main.go` |
| Rust | rustc | `rustc main.rs -o main && ./main` |
| Bash | Bash | `bash main.sh` |
| Prolog | SWI-Prolog | `swipl -q -s main.pl -g main -t halt` |
| Assembler | GNU Assembler (GAS) | `as assembler.s -o assembler.o && gcc assembler.o -o assembler.exe` |

## Кодировка
Все исходные файлы сохранены в UTF-8. Для C и C++ в начале `main()` добавлены вызовы `SetConsoleCP(CP_UTF8)` и `SetConsoleOutputCP(CP_UTF8)` для корректного вывода кириллицы в Windows.

## Assembler
- **ОС:** Windows
- **Архитектура:** x86-64
- **Язык ассемблера:** x86-64 (Intel syntax)
- **Toolchain:** GNU Assembler (GAS) из состава MinGW-w64
- **Команды сборки и запуска:** as asm/assembler.s -o asm/assembler.o
  gcc asm/assembler.o -o asm/assembler.exe
  .\asm\assembler.exe

  