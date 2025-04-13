
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract InvoiceAuth {
    struct Invoice {
        string invoiceNumber;
        string clientName;
        uint amount;
        string phoneNumber;
        uint timestamp;
    }

    mapping(string => Invoice) public invoices;

    function recordInvoice(string memory invoiceNumber, string memory clientName, uint amount, string memory phoneNumber) public {
        invoices[invoiceNumber] = Invoice(invoiceNumber, clientName, amount, phoneNumber, block.timestamp);
    }
}
