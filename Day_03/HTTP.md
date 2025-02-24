| **Factors**              |             **HTTP 2**              |                                                 **HTTP 2**                                                 |
| ------------------------ | :---------------------------------: | :--------------------------------------------------------------------------------------------------------: |
| connection setup         |                `TCP`                |                                           QUIC (based on `UDP`)                                            |
| connection establishment |        can result in delays         |                             faster due to `QUIC`'S combined handshake process                              |
| _head-of-line_ issues    | potential for _head-of-line_ issues |                                      _head-of-line_ issues eliminated                                      |
| network conditions       | performs well in stable conditions  | performs well in unstable network conditions (`QUIC` easily reestablish connections with minimal overhead) |
