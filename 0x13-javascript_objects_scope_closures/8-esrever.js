#!/snap/bin/node
exports.esrever = function (list) {
  const revArr = [];
  for (let i = list.length - 1; i > -1; i--) {
    revArr.push(list[i]);
  }
  return (revArr);
};
