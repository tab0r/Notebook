# Assignment: SQL on simple tables

## Objectives

Setting up PostgreSQL. You should follow the instructions below to install. There are no answers to return, just make sure you have PostgreSQL ready to go!

_______________________________________

## Resources

Here's the [postgres docs](http://www.postgresql.org/docs/9.3/interactive/).

_______________________________________

# Setup Postgres

Here's the [postgres docs](http://www.postgresql.org/docs/9.3/interactive/), which can be useful for setting stuff up.

## Install Postgres on a Mac

1. Install brew cask if you haven't already.

    * Install brew. Instructions [here](http://brew.sh/)
    * Install brew cask with: `brew install caskroom/cask/brew-cask`
    
    If you already have them, update: `brew update && brew upgrade brew-cask`

1. Install your Postgres database. The easiest way to to install the pre-build application (with an adorable icon) using the following command:

     ```
     brew cask install postgres
     ```

    If you don't have homebrew, go [here](http://brew.sh/).

2. After the installation is complete, use Spotlight to search for `postgres` and open the Application. It will ask you if you want to move it to the Applications folder, say "Move it"


## Setting up psql on a Mac

1. Open spotlight (click on magnifying class in upper right) and type in "Postgres" to open the postgres server. Click "Yes" to move to Applications folder. You should now have an elephant symbol in the top bar.

2. Go to the home directory by running `cd` in the terminal

3. Open your terminal configuration file in your favorite text editor:

      `atom ~/.bash_profile`

3. Insert the following line at the end of the file and save the file.

      ```export PATH=/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH``` 

4. Open a new terminal and run `psql`  

## Install psycopg2

1. Install with pip: `pip install psycopg2`

2. You might get this error message when you try to import the module: `Library not loaded: libssl.1.0.0.dylib`

      Here’s a [stack overflow post](http://stackoverflow.com/questions/27264574/import-psycopg2-library-not-loaded-libssl-1-0-0-dylib) with the solution. Basically psycopg2 is looking for a module that's in a different space on your computer and you need to setup a symbolic link (shortcut) to the module. Use these commands (replace YOURUSERNAME with your actual username).

      ```
      sudo ln -s /Users/YOURUSERNAME/anaconda/lib/libssl.1.0.0.dylib /usr/lib
      sudo ln -s /Users/YOURUSERNAME/anaconda/lib/libcrypto.1.0.0.dylib /usr/lib
      ```


## Setting up postgres, psql, and psycopg2 on Ubuntu

### Postgres & psql
1. In a terminal, type `sudo apt-get install postgresql`

2. Run the following commands, replacing `$USER` with your system username

   ```sudo -u postgres createuser --superuser $USER```

   ```sudo -u postgres createdb $USER```

3. Open a new terminal and run `psql`

### psycopg2
1. In a new terminal, type `conda install psycopg2`
2. By default, psycopg2 looks for postgres in the wrong place, so we'll create a symbolic link pointing it to the correct postgres server. Enter this command: `sudo ln -s /var/run/postgresql/.s.PGSQL.5432 /tmp/.s.PGSQL.5432`
3. Now, when using the `psycopg2.connect()` function in python, you only need to specify the `database` keyword, and not `user` or `host`
