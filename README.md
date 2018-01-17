# ScaledDFS
A file distribution system for a scalable system, implementing all basic concepts for a healthy system.

Desired functionality of the code - 

The code implements a few elements of a file distribution system, namely the Client side, The server side, The locking server and the file naming server. 
All the servers are created as pseudo classes, and are initiated by running individual initialisation files, also available in the repository.
All the services need a central source which provides information regarding the addresses, the port assignments, the file system heirarchy (in case of file server) and the different preset requests to be processed (in case of client server). These are all available in the relevant json files. 

The utils pseudo class file has been imported everywhere since it consists of the various methods that are used extensively with any server, (eg. checking authenticity of a request, check lock status to prevent accidental write).

As can be seen, due to time constraints, not all files could be completed, and there might be some methods which are only given in the structure, and not defined completely. I intend to complete these codes once the evaluation is finalised, while trying to improve the code at the same time. 


