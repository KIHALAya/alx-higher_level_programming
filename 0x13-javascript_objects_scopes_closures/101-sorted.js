#!/usr/bin/node
const originalDictionary = require('./101-data').dict;

const entriesList = Object.entries(originalDictionary);
const valuesList = Object.values(originalDictionary);
const uniqueValues = [...new Set(valuesList)];
const modifiedDictionary = {};

for (const uniqueVal of uniqueValues) {
  const keyList = [];
  for (const entry of entriesList) {
    if (entry[1] === uniqueVal) {
      keyList.unshift(entry[0]);
    }
  }
  modifiedDictionary[uniqueVal] = keyList;
}

console.log(modifiedDictionary);
