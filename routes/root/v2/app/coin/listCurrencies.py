from flask import request, render_template_string
from src.common.template import centeredHtml

def main():
    return {
    "status": "SUCCESS",
    "currencies": [
        {
            "currency": "0xa3Af5Ff33CE21a989f5b7Bb0E6982068b777A1c7",
          	"coin": {
                "name": "MetaKeep Demo Currency 1",
                "symbol": "MKDC1",
            },
            "transactionStatus": "COMPLETED"
        },
        {
            "currency": "0x57288F082c506cc19e695E72a0419348374f0175",
          	"coin": {
                "name": "MetaKeep Demo Currency 2",
                "symbol": "MKDC2",
            },
            "transactionStatus": "FAILED"
        },
        {
            "currency": "0x14649F5eb05AA41E9Ca2F834Cd8C88b1f0A9b538",
          	"coin": {
                "name": "MetaKeep Demo Currency 3",
                "symbol": "MKDC3",
            },
            "transactionStatus": "FAILED"
        },
        {
            "currency": "0x733Dcf85FaaF85119568110e5e926F7ec19dE28d",
          	"coin": {
                "name": "MetaKeep Demo Currency 4",
                "symbol": "MKDC4",
            },
            "transactionStatus": "COMPLETED"
        },
        {
            "currency": "0x14649F5eb05AA41E9Ca2F834Cd8C88b1f0A9b538",
          	"coin": {
                "name": "MetaKeep Demo Currency 5",
                "symbol": "MKDC5",
            },
            "transactionStatus": "QUEUED"
        },
    ]
}