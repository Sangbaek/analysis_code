## analysis_code


To compile in ifarm,

```
/apps/maven/PRO/bin/mvn clean package
```
This creates a jar file in directory "target".
To run filtering,

```
./bin/filterEvents -p "polarity" /path/to/hipo/files
```
The polarity should be "inbending" or "outbending". If -p option is not used, the default is inbending.