# AFL++ Fuzzing Project

Если вы хотите провести самостоятельное исследование с помощью **AFL++**, то:

1. Загрузите этот проект
2. Перейдите в директорию `Test2`
3. Выполните очистку сборки:

```bash
make clean


Затем запустите компиляцию с AFL++:
AFL_USE_ASAN=1 CC=afl-clang-lto CXX=afl-clang-lto++ AR=llvm-ar RANLIB=llvm-ranlib AS=llvm-as CFLAGS="-O0 -g -fprofile-instr-generate -fcoverage-mapping" make fuzz_harness
После этого следуйте инструкциям из отчёта
Во время запуска фаззинг-тестирования не забудьте указать директорию с входными данными и директорию для сохранения выходных данных AFL =)
