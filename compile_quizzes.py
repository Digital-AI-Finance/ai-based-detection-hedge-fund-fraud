#!/usr/bin/env python3
"""Compile all quiz .tex files to PDF using latexmk."""
import glob
import subprocess
import sys
import os

def compile_quiz(tex_file):
    """Compile a single quiz .tex file."""
    directory = os.path.dirname(tex_file)
    filename = os.path.basename(tex_file)
    result = subprocess.run(
        ['latexmk', '-pdf', '-interaction=nonstopmode', filename],
        capture_output=True, text=True, cwd=directory
    )
    if result.returncode != 0:
        print(f"FAIL: {tex_file}")
        return False
    print(f"OK: {tex_file}")
    return True

if __name__ == '__main__':
    quiz_files = sorted(glob.glob('[0-9][0-9]_*/*_quiz.tex') + glob.glob('A[0-2]_*/*_quiz.tex'))
    print(f"Found {len(quiz_files)} quiz files")

    failures = 0
    for f in quiz_files:
        if not compile_quiz(f):
            failures += 1

    if failures:
        print(f"\n{failures} compilation failures")
        sys.exit(1)
    print(f"\nAll {len(quiz_files)} quizzes compiled successfully")
