#!/usr/bin/env python3
"""Extract chart metadata and verify chart outputs exist."""
import json
import os
import sys

def verify_charts():
    """Verify all charts in charts.json have outputs."""
    with open('charts.json') as f:
        charts = json.load(f)

    missing = 0
    for chart in charts:
        script = chart['script_path']
        output = chart['output_path']
        thumb = os.path.join(os.path.dirname(output), 'thumb.png')

        if not os.path.exists(script):
            print(f"MISSING SCRIPT: {script}")
            missing += 1
        if not os.path.exists(output):
            print(f"MISSING OUTPUT: {output}")
            missing += 1
        if not os.path.exists(thumb):
            print(f"MISSING THUMB: {thumb}")
            missing += 1

    if missing:
        print(f"\n{missing} missing files")
        return False
    print(f"All {len(charts)} charts verified ({len(charts)*3} files)")
    return True

if __name__ == '__main__':
    if not verify_charts():
        sys.exit(1)
