#!/usr/bin/env python3

import os
from pathlib import Path
import argparse as ap
import rene

def main():
    parser = ap.ArgumentParser(description="Dumps a symbol")
    parser.add_argument("symbol", 
                        help="the symbol to dump",
                        )
    parser.add_argument("-d", "--destination",
                        required=False,
                        default=os.path.join('..', 'archive')
                        )
    
    args = parser.parse_args()
    
    rene.main(args)
    
if __name__ == '__main__':
    main()
