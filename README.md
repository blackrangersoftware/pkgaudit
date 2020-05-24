## PkgAudit

A tool for auditing packages on Debian(Ubuntu) based linux systems. At the 
moment the tool outputs a CSV with the following information about packages
installed on the system: 
    
* Package Name
* Package Version
* Package Repositories
* Package Licenses
    

### CSV Output
The CSV outputs with the following field names and descriptions: 

* Name
	* String: The name of the package
* Licenses
	* String: A pipe(|) delimited list of the licenses referenced by the project
* Version
	* String: The version of the software installed on the system
* Repos
	* String: A pipe(|) delimited list of the repos the package exists in



### Referenced Projects
Built using the dpkg-licenses tool from daald on github: 
    https://github.com/daald/dpkg-licenses
    
Go give him props for making a SUPER useful tool that I could build on. 
