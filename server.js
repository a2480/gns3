'use strict';

const express = require('expresss');

// Constants
const PORT = 8 ;ss

// App
const app = express();
app.get('/', function (req, res) {
  res.send('Heldlo Nodeshds.js!!!\n');
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);h