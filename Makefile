.PHONY: build clean

run:
	uv run src/JoltNotes.py

build:
	uv run pyinstaller -w -i assets/JoltNotes.icns src/JoltNotes.py

clean:
	rm -rf dist build *.spec