#!/usr/bin/node

const path = require('path')
const fs = require('fs')
const process = require('process');
let filepath = path.join(__dirname, process.argv[2])

fs.readFile(filepath, 'utf-8', (error, data) => {
    if (error) {
        console.log(error)
    } else {
        console.log(data)
    }
})