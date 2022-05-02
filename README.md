# Crypto Retriever

This is a command line application to store the history of a crypto coin for a specific date (or dates) into a file.

It was developed using 
- Click for the command line.
- Poetry for package manager.
- SQLAlchemy for the ORM.

To run the application you should:
1. poetry install
2. run:


        If you only want to fetch one day, pass a date. 

            $ poetry run cryptoData.py <IDENTIFIER> 12-12-2012

        If you want to fetch a range of days, dont pass a date and pass --from and --to options

            $ poetry run cryptoData.py <IDENTIFIER> --from=10-12-2012 --to=12-12-2012

        If you want to store the retrieved data to a localhost db, you have an option:

            $ poetry run cryptoData.py <IDENTIFIER> 12-12-2012 --store=true

            IMPORTANT: For this you must change the _DATABASE_URL inside /src/database.py

        <IDENTIFIER>: The coin to fetch.

