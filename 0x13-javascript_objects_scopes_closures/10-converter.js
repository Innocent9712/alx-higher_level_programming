#!/usr/bin/node
exports.converter = function (base) {
  return function (val) {
    return parseInt(val + '', 10).toString(base);
  };
};
