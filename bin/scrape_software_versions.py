#!/usr/bin/env python
from __future__ import print_function
import os

results = {}
version_files = [x for x in os.listdir(".") if x.endswith(".version.txt")]
for version_file in version_files:

    software = version_file.replace(".version.txt", "")
    if software == "pipeline":
        software = "nf-core/fetchfastq"

    with open(version_file) as fin:
        version = fin.read().strip()
    results[software] = version

# Dump to YAML
print(
    """
id: 'software_versions'
section_name: 'nf-core/fetchfastq Software Versions'
section_href: 'https://github.com/nf-core/fetchfastq'
plot_type: 'html'
description: 'are collected at run time from the software output.'
data: |
    <dl class="dl-horizontal">
"""
)
for k, v in sorted(results.items()):
    print("        <dt>{}</dt><dd><samp>{}</samp></dd>".format(k, v))
print("    </dl>")

# Write out regexes as csv file:
with open("software_versions.csv", "w") as f:
    for k, v in sorted(results.items()):
        f.write("{}\t{}\n".format(k, v))
