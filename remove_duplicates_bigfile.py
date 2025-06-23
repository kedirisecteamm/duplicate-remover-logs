import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}{Style.BRIGHT}
╔════════════════════════════════════════════╗
║     🔥 RISSEC1337 DUPLICATE REMOVER 🔥     ║
║     ⚡ KEDIRISECTEAM 2021 ⚡               ║
╚════════════════════════════════════════════╝
"""

def remove_duplicates(input_file, output_file):
    seen = set()
    line_count = 0
    unique_count = 0

    print(f"{Fore.YELLOW}▶ Starting processing...")

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
            line = line.rstrip('\n')
            line_count += 1
            if line not in seen:
                seen.add(line)
                outfile.write(line + '\n')
                unique_count += 1

            if line_count % 1_000_000 == 0:
                print(f"{Fore.CYAN}⏳ Processed: {line_count:,} lines | Unique: {unique_count:,}")

    print(f"\n{Fore.GREEN}✅ Done!")
    print(f"{Fore.GREEN}📄 Total lines: {line_count:,}")
    print(f"{Fore.GREEN}🆕 Unique lines: {unique_count:,}")
    print(f"{Fore.GREEN}📁 Output saved to: {output_file}")

if __name__ == "__main__":
    print(BANNER)

    if len(sys.argv) != 3:
        print(f"{Fore.RED}Usage: python remove_duplicates_bigfile.py input.txt output.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        if not os.path.isfile(input_file):
            print(f"{Fore.RED}❌ File not found: {input_file}")
            sys.exit(1)

        remove_duplicates(input_file, output_file)
