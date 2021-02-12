## analysis_code


To compile in ifarm,

```
/apps/maven/PRO/bin/mvn clean package
```
This creates a jar file in directory "target".
To run filtering,

```
./bin/filterEvents -p "polarity" -s start -e end [-t] [-eb] /path/to/hipo/files
```
The polarity should be "inbending" or "outbending". If -p option is not used, the default is inbending. If -t is used, it requires two photons. If -eb is used, it doesn't use any enhance pid cuts, but use eb pid as is.