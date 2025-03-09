from uuid import uuid4

import subprocess

text = """Requirement Levels
RFCs are classified into five requirement levels: required, recommended, elective, lim-
ited use, and not recommended.
Required. An RFC is labeled required if it must be implemented by all Internet
systems to achieve minimum conformance. For example, IP and ICMP (Chapter 19)
are required protocols.
Recommended. An RFC labeled recommended is not required for minimum
conformance; it is recommended because of its usefulness. For example, FTP
(Chapter 26) and TELNET (Chapter 26) are recommended protocols.
Elective. An RFC labeled elective is not required and not recommended. However,
a system can use it for its own benefit.
Limited Use. An RFC labeled limited use should be used only in limited situations.
Most of the experimental RFCs fall under this category.
Not Recommended. An RFC labeled not recommended is inappropriate for gen-
eral use. Normally a historic (deprecated) RFC may fall under this category.
"""

mappings = [
    (".\n", str(uuid4()), ".\n"),
    ("-\n", str(uuid4()), ""),
    ("\n", str(uuid4()), " "),
]

for old, new, _ in mappings:
    text = text.replace(old, new)

for _, old, new in mappings:
    text = text.replace(old, new)

subprocess.run(['wl-copy'], input=text.encode(), check=True)
print(text)
