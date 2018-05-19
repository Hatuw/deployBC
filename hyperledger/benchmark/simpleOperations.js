'use strict';

module.exports.info  = 'simple operations';

let bc, contx;
let no_accounts=0;
let account_array=[];
let accounts, txnPerBatch;
const initial_balance = 1000000;
// const operation_type = ['open', 'delete', 'query', 'transfer'];
const operation_type = ['query', 'transfer'];
let prefix;

/**
 * Generate unique account key for the transaction
 * @returns {Number} account key
 **/
function generateAccount() {
    // should be [a-z]{1,9}
    if(typeof prefix === 'undefined') {
        prefix = process.pid;
    }
    let count = account_array.length+1;
    let num = prefix.toString() + count.toString();
    return parseInt(num).toString();
}

/**
 * Generates random string.
 * @returns {string} random string from possible characters
 **/
function random_string() {
    let text = '';
    const possible = 'ABCDEFGHIJKL MNOPQRSTUVWXYZ abcdefghij klmnopqrstuvwxyz';

    for (let i = 0; i < 12; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

/**
 * Generates small bank workload with specified number of accounts
 * and operations.
 * @returns {Object} array of json objects and each denotes
 * one operations
 **/
function generateWorkload() {
    let workload = [];
    for(let i= 0; (i < txnPerBatch && no_accounts<accounts); i++,no_accounts++) {
        let acc_id = generateAccount();
        account_array.push(acc_id);
        let acc = {
            'verb': 'open',
            'account': acc_id,
            'money': initial_balance.toString()
        };
        workload.push(acc);
    }
    if(workload.length === txnPerBatch) {
        return workload;
    }
    else {
        for(let j=workload.length; j<txnPerBatch; j++) {
            let op_index =  Math.floor(Math.random() * Math.floor(operation_type.length));
            let acc_index = Math.floor(Math.random() * Math.floor(account_array.length));
            let random_op = operation_type[op_index];
            let random_acc = account_array[acc_index];
            let amount = Math.floor(Math.random() * 200);
            let op_payload;
            switch(random_op) {
            case 'query': {
                op_payload = {
                    'verb': 'query',
                    'account': random_acc
                };
                break;
            }
            case 'transfer': {
                let dest_customer_id = account_array[Math.floor(Math.random() * account_array.length)];
                let source_customer_id = account_array[Math.floor(Math.random() * account_array.length)];
                if(dest_customer_id === source_customer_id) {
                    source_customer_id = account_array[Math.floor(Math.random() * account_array.length)];
                }
                op_payload = {
                    'verb': 'transfer',
                    'account1': dest_customer_id,
                    'account2': source_customer_id,
                    'money': amount.toString()
                };
                break;
            }
            default: {
                throw new Error('Invalid operation!!!');
            }
            }
            workload.push(op_payload);
        }
    }
    return workload;
}

module.exports.init = function(blockchain, context, args) {
    if(!args.hasOwnProperty('accounts')) {
        return Promise.reject(new Error('simple.operations - \'accounts\' is missed in the arguments'));
    }
    if(!args.hasOwnProperty('txnPerBatch')) {
        return Promise.reject(new Error('simple.operations - \'txnPerBatch\' is missed in the arguments'));
    }
    accounts = args.accounts;
    if(accounts <=3) {
        return Promise.reject(new Error('simple.operations - number accounts should be more than 3'));
    }
    txnPerBatch = args.txnPerBatch;
    bc = blockchain;
    contx = context;
    return Promise.resolve();
};

module.exports.run = function() {
    let args = generateWorkload()[0];
    return bc.invokeSmartContract(contx, 'simple', 'v0', args, 30);
};

module.exports.end = function(results) {
    return Promise.resolve();
};


module.exports.account_array = account_array;
