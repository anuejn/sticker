"use strict";
var page = require('webpage').create(),
    system = require('system'),
    address, output, size;


address = system.args[1];
output = system.args[2];
size = system.args[3].split('*');

page.viewportSize = { width: size[0] * 100, height: size[1] * 100};
page.paperSize = {width: size[0], height: size[1], margin: '0'};

page.open(address, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit(1);
    } else {
        window.setTimeout(function () {
            page.render(output);
            phantom.exit();
        }, 200);
    }
});
