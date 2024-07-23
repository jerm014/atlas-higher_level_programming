#!/usr/bin/node

function occurance (list, search) {
    let count = 0;
    list.array.forEach(element => {
        if (element === search) count++;
    });
    return count;
  };

  exports.nbOccurences = occurance;
