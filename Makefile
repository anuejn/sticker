default: clean out/stickers.pdf

out/stickers.pdf: node_modules in out/stickers.html
	./node_modules/phantomjs-prebuilt/bin/phantomjs rasterize.js out/stickers.html out/stickers.pdf 29.7cm*10.5cm

out/stickers.html:
	cd in/flyer; python f2c.py > ../tr.css
	mkdir out
	cp in/tr.css out/tr.css
	cp in/index.html out/stickers.html
	perl -pe 's/\$$svg\$$/`cat in\/logo.svg`/ge' -i out/stickers.html

view: out/stickers.pdf
	evince out/stickers.pdf 2> /dev/null

node_modules:
	npm i

clean:
	rm -rf out

clean_all: clean
	rm -rf node_modules
