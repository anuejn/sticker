"use strict";
var page = require('webpage').create();

var address = "index.html";
var output = "index.pdf";

page.viewportSize = { width: 600, height: 600 };
page.paperSize = {format: "A4", orientation: 'portrait', margin: '0cm'};

page.open(address, () => {
    page.render(output);
    phantom.exit();
});

