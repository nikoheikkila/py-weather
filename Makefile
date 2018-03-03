build:
	pipenv run pyinstaller --noconfirm --log-level WARN --onefile --nowindow weather.py

install:
	cp dist/weather /usr/local/bin

clean:
	rm -rf build dist
