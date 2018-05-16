'use strict';

module.exports.info  = 'querying accounts';


let bc, contx;
let accounts;
module.exports.init = function(blockchain, context, args) {
    let acc = require('./simpleOperations.js');
    bc       = blockchain;
    contx    = context;
    accounts = acc.account_array;
    return Promise.resolve();
};

module.exports.run = function() {
    const acc  = accounts[Math.floor(Math.random()*(accounts.length))];

    return bc.queryState(contx, 'simple', 'v0', acc);
};

module.exports.end = function(results) {
    // do nothing
    return Promise.resolve();
};
