import face_recognition as fr # type: ignore
import numpy as np
import argparse
from yaspin import yaspin # type: ignore
from rich import print # type: ignore
import os

parser = argparse.ArgumentParser()
parser.add_argument("image1", type=str, help="first image to compare")
parser.add_argument("image2", type=str, help="second image to compare")

args = parser.parse_args()

with yaspin(text="Calculating...", color="cyan") as spinner:

    name1 = args.image1
    if not os.path.exists(name1):
        spinner.fail("💥")
        print("[red bold]" + name1 + " does not exist[/]")
        exit()
    name2 = args.image2
    if not os.path.exists(name2):
        spinner.fail("💥")
        print("[red bold]" + name2 + " does not exist[/]")
        exit()

    img1 = fr.load_image_file(name1)
    img2 = fr.load_image_file(name2)

    faces1 = fr.face_encodings(img1)
    faces2 = fr.face_encodings(img2)
    if not faces1:
        spinner.fail("💥")
        print("[red bold]" + name1 + " has no faces[/]")
        exit()
    if not faces2:
        spinner.fail("💥")
        print("[red bold]" + name2 + " has no faces[/]")
        exit()

    v1 = np.array(fr.face_encodings(img1)[0])
    v2 = np.array(fr.face_encodings(img2)[0])

    same = fr.compare_faces([v1], v2)[0]

    D = np.linalg.norm(v1 - v2)

    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    result = round((cos + 1) / 2 * 100, 2)

    spinner.ok("✅")
    
    print(f"Same {result}%" if D <= 0.5 else f"Different {100 - result}%")