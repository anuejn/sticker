default: out

out: node_modules
	npm start

node_modules:
	npm i

clean:
	rm -rf out
	rm -rf node_modules
