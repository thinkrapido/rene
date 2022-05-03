#!/usr/bin/env python3

import os
from pathlib import Path
import argparse as ap
import rene

def main():
    parser = ap.ArgumentParser(description="Logt alle Tage von 01.01.0001 bis 01.01.2500")
    parser.add_argument("date", 
                        help="geburtsdatum",
                        )
    parser.add_argument("value", 
                        help="zahl",
                        )
    
    args = parser.parse_args()
    
    rene.main(args)
    
if __name__ == '__main__':
    main()
