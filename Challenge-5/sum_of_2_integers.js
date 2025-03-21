/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
    while(b){
      let temp=a
      a=temp^b
      b=(temp&b)<<1 
    }
    return a
  };