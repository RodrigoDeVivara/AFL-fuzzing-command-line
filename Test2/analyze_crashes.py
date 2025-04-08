import subprocess
from pathlib import Path

# Пути
target = Path("/home/ivan/secure-shell-interpreter/Test2/fuzz_harness")
crash_dir = Path("/home/ivan/afl_outputs/out/default/crashes")
log_file = Path("crash_log.txt")

# Начало лога
with open(log_file, "w") as log:
    log.write("[*] Анализ крашей начат\n\n")

# Прогон всех крашей
for crash in sorted(crash_dir.glob("id:*")):
    with open(crash, "rb") as input_file:
        try:
            result = subprocess.run(
                [str(target)],
                stdin=input_file,
                capture_output=True,
                timeout=5  # на всякий случай
            )

            with open(log_file, "a") as log:
                log.write("="*40 + "\n")
                log.write(f"[*] Файл: {crash.name}\n")
                log.write("-"*40 + "\n")
                log.write(result.stdout.decode(errors="ignore"))
                log.write(result.stderr.decode(errors="ignore"))
                log.write("\n")

        except subprocess.TimeoutExpired:
            with open(log_file, "a") as log:
                log.write(f"[!] {crash.name} — TIMEOUT\n\n")

# Конец лога
with open(log_file, "a") as log:
    log.write("[*] Анализ завершён\n")
