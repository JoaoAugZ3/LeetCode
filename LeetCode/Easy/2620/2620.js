/*
Concluído
Runtime: 48ms
Memory: 41.8MB
*/

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let add = 0
    let vlr = n
    return function() {
        vlr = n + add
        add++
        return vlr
    };
};