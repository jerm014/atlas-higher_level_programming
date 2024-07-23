#!/usr/bin/node

function occurance (list, search) {
    let count = 0;
    list.forEach(element => {
        if (element === search) count++;
    });
    return count;
  };

  exports.nbOccurences = occurance;
