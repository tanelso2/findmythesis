# A simple website for generating thesis topics

Uses a google spreadsheet that my friend maintains as its source of phrases

# Getting Started 
First, install Docker using the instructions in their [docs](https://docs.docker.com/install/)

## Building
After Docker is installed and running, you should be able to build the code using the provided `build.sh` script or run the following from the root of this project:
```bash
docker build -t your-thesis-statement:latest .
```

## Running
To run, run the `run.sh` script.

You should now be able to go to [http://localhost:5000/test](http://localhost:5000/test) in your browser and view the site using a pre-generated test thesis

# How to contribute
Pull requests are welcome!
If you've never created one before, you can try [this guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github)


