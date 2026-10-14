from pathlib import Path
import shutil

def move_jpg_files():
    source_text = input("Folder containing JPG files: ").strip()
    source = Path(source_text).expanduser()

    if not source.exists() or not source.is_dir():
        print("That folder does not exist.")
        return

    destination_text = input("Destination folder: ").strip()
    destination = Path(destination_text).expanduser()

    # Avoid moving a folder into itself.
    if destination.resolve() == source.resolve() or source.resolve() in destination.resolve().parents:
        print("Choose a destination outside the source folder.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    moved = 0

    for item in source.iterdir():
        if item.is_file() and item.suffix.lower() in {".jpg", ".jpeg"}:
            target = destination / item.name
            if target.exists():
                print(f"Skipped {item.name}: destination already contains that name.")
                continue
            shutil.move(str(item), str(target))
            moved += 1

    print(f"Done. Moved {moved} JPG/JPEG file(s) to {destination}")

if __name__ == "__main__":
    print("=== JPG File Organizer ===")
    move_jpg_files()
