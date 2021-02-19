This dataset was generated from a full copy of the data file
`2019.annual.singlefile.csv`. Using the built in UNIX text tools, run the following sequence of commands:

    cp ../USA_full/2019.annual.singlefile.csv .
    head -n 1 2019.annual.singlefile.csv > header.csv
    grep '^"11' 2019.annual.singlefile.csv > dat.csv
    cat header.csv dat.csv > 2019.annual.singlefile.csv
    rm header.csv dat.csv

*Note: You may use your own implementation of `tt.py` if it has been **installed**. See [Installing_Text_Tools.md](../instructions/Installing_Text_Tools.md) for details and the modifications needed to the above sequence of commands.*
