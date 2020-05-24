import os, csv, sys

packages = {}

def InitializeFiles():
    with open ('repos', mode='w') as repos:
        repos.write("Name|Repos\n")

    os.system('apt list --installed | cut -f1 -d" " | sed -e "s/\//|/" >> repos')
    os.system('bin/dpkg-licenses/dpkg-licenses -c >> licenses')

def ParseLicenses(licenses, repos):

    licenses = csv.DictReader(licenses)
    repos = csv.DictReader(repos, delimiter="|") 

    for license in licenses:
        package = packages[license["Name"].split(":")[0]] = {}
        package["Licenses"] = license["Licenses"]
        package["Version"] = license["Version"]
        package["Name"] = license["Name"]

    for repo in repos:
        if repo["Name"] == "Listing...":
            continue
        try:
            packages[repo["Name"]]["Repos"] = repo["Repos"]
        except:
            continue

    with open('Packages.csv', mode='w') as packages_csv:
        packages_csv.write("Name,Licenses,Version,Repos\n")
        for package in packages:
            package = packages[package]
            try:
                package["Repos"]
            except:
                package["Repos"] = "NULL"

            packages_csv.write(package["Name"]+","+
                               package["Licenses"].replace(" ","|")+","+
                               package["Version"]+","+
                               package["Repos"].replace(",","|")+"\n")

if __name__ == "__main__":
    
    InitializeFiles()

    with open('licenses', mode='r') as licenses:
        with open('repos', mode='r') as repos:
            ParseLicenses(licenses, repos)

